'''
# AWS Auto Scaling Construct Library

**Application AutoScaling** is used to configure autoscaling for all
services other than scaling EC2 instances. For example, you will use this to
scale ECS tasks, DynamoDB capacity, Spot Fleet sizes, Comprehend document classification endpoints, Lambda function provisioned concurrency and more.

As a CDK user, you will probably not have to interact with this library
directly; instead, it will be used by other construct libraries to
offer AutoScaling features for their own constructs.

This document will describe the general autoscaling features and concepts;
your particular service may offer only a subset of these.

## AutoScaling basics

Resources can offer one or more **attributes** to autoscale, typically
representing some capacity dimension of the underlying service. For example,
a DynamoDB Table offers autoscaling of the read and write capacity of the
table proper and its Global Secondary Indexes, an ECS Service offers
autoscaling of its task count, an RDS Aurora cluster offers scaling of its
replica count, and so on.

When you enable autoscaling for an attribute, you specify a minimum and a
maximum value for the capacity. AutoScaling policies that respond to metrics
will never go higher or lower than the indicated capacity (but scheduled
scaling actions might, see below).

There are three ways to scale your capacity:

* **In response to a metric** (also known as step scaling); for example, you
  might want to scale out if the CPU usage across your cluster starts to rise,
  and scale in when it drops again.
* **By trying to keep a certain metric around a given value** (also known as
  target tracking scaling); you might want to automatically scale out an in to
  keep your CPU usage around 50%.
* **On a schedule**; you might want to organize your scaling around traffic
  flows you expect, by scaling out in the morning and scaling in in the
  evening.

The general pattern of autoscaling will look like this:

```python
# resource is of type SomeScalableResource


capacity = resource.auto_scale_capacity(
    min_capacity=5,
    max_capacity=100
)
```

## Step Scaling

This type of scaling scales in and out in deterministic steps that you
configure, in response to metric values. For example, your scaling strategy
to scale in response to CPU usage might look like this:

```plaintext
 Scaling        -1          (no change)          +1       +3
            │        │                       │        │        │
            ├────────┼───────────────────────┼────────┼────────┤
            │        │                       │        │        │
CPU usage   0%      10%                     50%       70%     100%
```

(Note that this is not necessarily a recommended scaling strategy, but it's
a possible one. You will have to determine what thresholds are right for you).

You would configure it like this:

```python
# capacity is of type ScalableAttribute
# cpu_utilization is of type Metric


capacity.scale_on_metric("ScaleToCPU",
    metric=cpu_utilization,
    scaling_steps=[ec2.aws_applicationautoscaling.ScalingInterval(upper=10, change=-1), ec2.aws_applicationautoscaling.ScalingInterval(lower=50, change=+1), ec2.aws_applicationautoscaling.ScalingInterval(lower=70, change=+3)
    ],

    # Change this to AdjustmentType.PercentChangeInCapacity to interpret the
    # 'change' numbers before as percentages instead of capacity counts.
    adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY
)
```

The AutoScaling construct library will create the required CloudWatch alarms and
AutoScaling policies for you.

### Scaling based on multiple datapoints

The Step Scaling configuration above will initiate a scaling event when a single
datapoint of the scaling metric is breaching a scaling step breakpoint. In cases
where you might want to initiate scaling actions on a larger number of datapoints
(ie in order to smooth out randomness in the metric data), you can use the
optional `evaluationPeriods` and `datapointsToAlarm` properties:

```python
# capacity is of type ScalableAttribute
# cpu_utilization is of type Metric


capacity.scale_on_metric("ScaleToCPUWithMultipleDatapoints",
    metric=cpu_utilization,
    scaling_steps=[ec2.aws_applicationautoscaling.ScalingInterval(upper=10, change=-1), ec2.aws_applicationautoscaling.ScalingInterval(lower=50, change=+1), ec2.aws_applicationautoscaling.ScalingInterval(lower=70, change=+3)
    ],

    # if the cpuUtilization metric has a period of 1 minute, then data points
    # in the last 10 minutes will be evaluated
    evaluation_periods=10,

    # Only trigger a scaling action when 6 datapoints out of the last 10 are
    # breaching. If this is left unspecified, then ALL datapoints in the
    # evaluation period must be breaching to trigger a scaling action
    datapoints_to_alarm=6
)
```

## Target Tracking Scaling

This type of scaling scales in and out in order to keep a metric (typically
representing utilization) around a value you prefer. This type of scaling is
typically heavily service-dependent in what metric you can use, and so
different services will have different methods here to set up target tracking
scaling.

The following example configures the read capacity of a DynamoDB table
to be around 60% utilization:

```python
import monocdk as dynamodb

# table is of type Table


read_capacity = table.auto_scale_read_capacity(
    min_capacity=10,
    max_capacity=1000
)
read_capacity.scale_on_utilization(
    target_utilization_percent=60
)
```

## Scheduled Scaling

This type of scaling is used to change capacities based on time. It works
by changing the `minCapacity` and `maxCapacity` of the attribute, and so
can be used for two purposes:

* Scale in and out on a schedule by setting the `minCapacity` high or
  the `maxCapacity` low.
* Still allow the regular scaling actions to do their job, but restrict
  the range they can scale over (by setting both `minCapacity` and
  `maxCapacity` but changing their range over time).

The following schedule expressions can be used:

* `at(yyyy-mm-ddThh:mm:ss)` -- scale at a particular moment in time
* `rate(value unit)` -- scale every minute/hour/day
* `cron(mm hh dd mm dow)` -- scale on arbitrary schedules

Of these, the cron expression is the most useful but also the most
complicated. A schedule is expressed as a cron expression. The `Schedule` class has a `cron` method to help build cron expressions.

The following example scales the fleet out in the morning, and lets natural
scaling take over at night:

```python
# resource is of type SomeScalableResource


capacity = resource.auto_scale_capacity(
    min_capacity=1,
    max_capacity=50
)

capacity.scale_on_schedule("PrescaleInTheMorning",
    schedule=appscaling.Schedule.cron(hour="8", minute="0"),
    min_capacity=20
)

capacity.scale_on_schedule("AllowDownscalingAtNight",
    schedule=appscaling.Schedule.cron(hour="20", minute="0"),
    min_capacity=1
)
```

## Examples

### Lambda Provisioned Concurrency Auto Scaling

```python
import monocdk as lambda_

# code is of type Code


handler = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.PYTHON_3_7,
    handler="index.handler",
    code=code,

    reserved_concurrent_executions=2
)

fn_ver = handler.add_version("CDKLambdaVersion", undefined, "demo alias", 10)

target = appscaling.ScalableTarget(self, "ScalableTarget",
    service_namespace=appscaling.ServiceNamespace.LAMBDA,
    max_capacity=100,
    min_capacity=10,
    resource_id=f"function:{handler.functionName}:{fnVer.version}",
    scalable_dimension="lambda:function:ProvisionedConcurrency"
)

target.scale_to_track_metric("PceTracking",
    target_value=0.9,
    predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
)
```

### ElastiCache Redis shards scaling with target value

```python
shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
    service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
    scalable_dimension="elasticache:replication-group:NodeGroups",
    min_capacity=2,
    max_capacity=10,
    resource_id="replication-group/main-cluster"
)

shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
    target_value=20,
    predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
)
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_e0a482dc,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    Resource as _Resource_abff4495,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_cloudwatch import Alarm as _Alarm_a55fe34b, IMetric as _IMetric_5db43d61
from ..aws_iam import (
    IRole as _IRole_59af6f50, PolicyStatement as _PolicyStatement_296fe8a3
)


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.AdjustmentTier",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "lower_bound": "lowerBound",
        "upper_bound": "upperBound",
    },
)
class AdjustmentTier:
    def __init__(
        self,
        *,
        adjustment: jsii.Number,
        lower_bound: typing.Optional[jsii.Number] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) An adjustment.

        :param adjustment: (experimental) What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
        :param lower_bound: (experimental) Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        :param upper_bound: (experimental) Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            
            adjustment_tier = applicationautoscaling.AdjustmentTier(
                adjustment=123,
            
                # the properties below are optional
                lower_bound=123,
                upper_bound=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "adjustment": adjustment,
        }
        if lower_bound is not None:
            self._values["lower_bound"] = lower_bound
        if upper_bound is not None:
            self._values["upper_bound"] = upper_bound

    @builtins.property
    def adjustment(self) -> jsii.Number:
        '''(experimental) What number to adjust the capacity with.

        The number is interpeted as an added capacity, a new fixed capacity or an
        added percentage depending on the AdjustmentType value of the
        StepScalingPolicy.

        Can be positive or negative.

        :stability: experimental
        '''
        result = self._values.get("adjustment")
        assert result is not None, "Required property 'adjustment' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lower_bound(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Lower bound where this scaling tier applies.

        The scaling tier applies if the difference between the metric
        value and its alarm threshold is higher than this value.

        :default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier

        :stability: experimental
        '''
        result = self._values.get("lower_bound")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upper_bound(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Upper bound where this scaling tier applies.

        The scaling tier applies if the difference between the metric
        value and its alarm threshold is lower than this value.

        :default: +Infinity

        :stability: experimental
        '''
        result = self._values.get("upper_bound")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdjustmentTier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.AdjustmentType")
class AdjustmentType(enum.Enum):
    '''(experimental) How adjustment numbers are interpreted.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # capacity is of type ScalableAttribute
        # cpu_utilization is of type Metric
        
        
        capacity.scale_on_metric("ScaleToCPU",
            metric=cpu_utilization,
            scaling_steps=[ec2.aws_applicationautoscaling.ScalingInterval(upper=10, change=-1), ec2.aws_applicationautoscaling.ScalingInterval(lower=50, change=+1), ec2.aws_applicationautoscaling.ScalingInterval(lower=70, change=+3)
            ],
        
            # Change this to AdjustmentType.PercentChangeInCapacity to interpret the
            # 'change' numbers before as percentages instead of capacity counts.
            adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY
        )
    '''

    CHANGE_IN_CAPACITY = "CHANGE_IN_CAPACITY"
    '''(experimental) Add the adjustment number to the current capacity.

    A positive number increases capacity, a negative number decreases capacity.

    :stability: experimental
    '''
    PERCENT_CHANGE_IN_CAPACITY = "PERCENT_CHANGE_IN_CAPACITY"
    '''(experimental) Add this percentage of the current capacity to itself.

    The number must be between -100 and 100; a positive number increases
    capacity and a negative number decreases it.

    :stability: experimental
    '''
    EXACT_CAPACITY = "EXACT_CAPACITY"
    '''(experimental) Make the capacity equal to the exact number given.

    :stability: experimental
    '''


class BaseScalableAttribute(
    _Construct_e78e779f,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_applicationautoscaling.BaseScalableAttribute",
):
    '''(experimental) Represent an attribute for which autoscaling can be configured.

    This class is basically a light wrapper around ScalableTarget, but with
    all methods protected instead of public so they can be selectively
    exposed and/or more specific versions of them can be exposed by derived
    classes for individual services support autoscaling.

    Typical use cases:

    - Hide away the PredefinedMetric enum for target tracking policies.
    - Don't expose all scaling methods (for example Dynamo tables don't support
      Step Scaling, so the Dynamo subclass won't expose this method).

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: _IRole_59af6f50,
        service_namespace: "ServiceNamespace",
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dimension: (experimental) Scalable dimension of the attribute.
        :param resource_id: (experimental) Resource ID of the attribute.
        :param role: (experimental) Role to use for scaling.
        :param service_namespace: (experimental) Service namespace of the scalable attribute.
        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1

        :stability: experimental
        '''
        props = BaseScalableAttributeProps(
            dimension=dimension,
            resource_id=resource_id,
            role=role,
            service_namespace=service_namespace,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="doScaleOnMetric")
    def _do_scale_on_metric(
        self,
        id: builtins.str,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.Sequence["ScalingInterval"],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional["MetricAggregationType"] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Scale out or in based on a metric value.

        :param id: -
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: (experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: ``evaluationPeriods``
        :param evaluation_periods: (experimental) How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: (experimental) Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        '''
        props = BasicStepScalingPolicyProps(
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluation_periods=evaluation_periods,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        return typing.cast(None, jsii.invoke(self, "doScaleOnMetric", [id, props]))

    @jsii.member(jsii_name="doScaleOnSchedule")
    def _do_scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''(experimental) Scale out or in based on time.

        :param id: -
        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        '''
        props = ScalingSchedule(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "doScaleOnSchedule", [id, props]))

    @jsii.member(jsii_name="doScaleToTrackMetric")
    def _do_scale_to_track_metric(
        self,
        id: builtins.str,
        *,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional["PredefinedMetric"] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        '''(experimental) Scale out or in in order to keep a metric around a target value.

        :param id: -
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        '''
        props = BasicTargetTrackingScalingPolicyProps(
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast(None, jsii.invoke(self, "doScaleToTrackMetric", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def _props(self) -> "BaseScalableAttributeProps":
        '''
        :stability: experimental
        '''
        return typing.cast("BaseScalableAttributeProps", jsii.get(self, "props"))


class _BaseScalableAttributeProxy(BaseScalableAttribute):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseScalableAttribute).__jsii_proxy_class__ = lambda : _BaseScalableAttributeProxy


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BaseTargetTrackingProps",
    jsii_struct_bases=[],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
    },
)
class BaseTargetTrackingProps:
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        '''(experimental) Base interface for target tracking props.

        Contains the attributes that are common to target tracking policies,
        except the ones relating to the metric and to the scalable target.

        This interface is reused by more specific target tracking props objects
        in other services.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            
            # duration is of type Duration
            
            base_target_tracking_props = applicationautoscaling.BaseTargetTrackingProps(
                disable_scale_in=False,
                policy_name="policyName",
                scale_in_cooldown=duration,
                scale_out_cooldown=duration
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the scaling policy.

        :default: - Automatically generated name.

        :stability: experimental
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseTargetTrackingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BasicStepScalingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric": "metric",
        "scaling_steps": "scalingSteps",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluation_periods": "evaluationPeriods",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
    },
)
class BasicStepScalingPolicyProps:
    def __init__(
        self,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.Sequence["ScalingInterval"],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional["MetricAggregationType"] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: (experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: ``evaluationPeriods``
        :param evaluation_periods: (experimental) How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: (experimental) Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # capacity is of type ScalableAttribute
            # cpu_utilization is of type Metric
            
            
            capacity.scale_on_metric("ScaleToCPU",
                metric=cpu_utilization,
                scaling_steps=[ec2.aws_applicationautoscaling.ScalingInterval(upper=10, change=-1), ec2.aws_applicationautoscaling.ScalingInterval(lower=50, change=+1), ec2.aws_applicationautoscaling.ScalingInterval(lower=70, change=+3)
                ],
            
                # Change this to AdjustmentType.PercentChangeInCapacity to interpret the
                # 'change' numbers before as percentages instead of capacity counts.
                adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "scaling_steps": scaling_steps,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude

    @builtins.property
    def metric(self) -> _IMetric_5db43d61:
        '''(experimental) Metric to scale on.

        :stability: experimental
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(_IMetric_5db43d61, result)

    @builtins.property
    def scaling_steps(self) -> typing.List["ScalingInterval"]:
        '''(experimental) The intervals for scaling.

        Maps a range of metric values to a particular scaling behavior.

        :stability: experimental
        '''
        result = self._values.get("scaling_steps")
        assert result is not None, "Required property 'scaling_steps' is missing"
        return typing.cast(typing.List["ScalingInterval"], result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        '''(experimental) How the adjustment numbers inside 'intervals' are interpreted.

        :default: ChangeInCapacity

        :stability: experimental
        '''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[AdjustmentType], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Grace period after scaling activity.

        Subsequent scale outs during the cooldown period are squashed so that only
        the biggest scale out happens.

        Subsequent scale ins during the cooldown period are ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        :stability: experimental
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action.

        Creates an "M out of N" alarm, where this property is the M and the value set for
        ``evaluationPeriods`` is the N value.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: ``evaluationPeriods``

        :stability: experimental
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''(experimental) How many evaluation periods of the metric to wait before triggering a scaling action.

        Raising this value can be used to smooth out the metric, at the expense
        of slower response times.

        If ``datapointsToAlarm`` is not set, then all data points in the evaluation period
        must meet the criteria to trigger a scaling action.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional["MetricAggregationType"]:
        '''(experimental) Aggregation to apply to all data points over the evaluation periods.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.

        :stability: experimental
        '''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional["MetricAggregationType"], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect

        :stability: experimental
        '''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicStepScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BasicTargetTrackingScalingPolicyProps",
    jsii_struct_bases=[BaseTargetTrackingProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_value": "targetValue",
        "custom_metric": "customMetric",
        "predefined_metric": "predefinedMetric",
        "resource_label": "resourceLabel",
    },
)
class BasicTargetTrackingScalingPolicyProps(BaseTargetTrackingProps):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional["PredefinedMetric"] = None,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for a Target Tracking policy that include the metric but exclude the target.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import monocdk as lambda_
            
            # code is of type Code
            
            
            handler = lambda_.Function(self, "MyFunction",
                runtime=lambda_.Runtime.PYTHON_3_7,
                handler="index.handler",
                code=code,
            
                reserved_concurrent_executions=2
            )
            
            fn_ver = handler.add_version("CDKLambdaVersion", undefined, "demo alias", 10)
            
            target = appscaling.ScalableTarget(self, "ScalableTarget",
                service_namespace=appscaling.ServiceNamespace.LAMBDA,
                max_capacity=100,
                min_capacity=10,
                resource_id=f"function:{handler.functionName}:{fnVer.version}",
                scalable_dimension="lambda:function:ProvisionedConcurrency"
            )
            
            target.scale_to_track_metric("PceTracking",
                target_value=0.9,
                predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if predefined_metric is not None:
            self._values["predefined_metric"] = predefined_metric
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the scaling policy.

        :default: - Automatically generated name.

        :stability: experimental
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''(experimental) The target value for the metric.

        :stability: experimental
        '''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def custom_metric(self) -> typing.Optional[_IMetric_5db43d61]:
        '''(experimental) A custom metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No custom metric.

        :stability: experimental
        '''
        result = self._values.get("custom_metric")
        return typing.cast(typing.Optional[_IMetric_5db43d61], result)

    @builtins.property
    def predefined_metric(self) -> typing.Optional["PredefinedMetric"]:
        '''(experimental) A predefined metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No predefined metrics.

        :stability: experimental
        '''
        result = self._values.get("predefined_metric")
        return typing.cast(typing.Optional["PredefinedMetric"], result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Identify the resource associated with the metric type.

        Only used for predefined metric ALBRequestCountPerTarget.

        Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>``

        :default: - No resource label.

        :stability: experimental
        '''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicTargetTrackingScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnScalableTarget(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget",
):
    '''A CloudFormation ``AWS::ApplicationAutoScaling::ScalableTarget``.

    The ``AWS::ApplicationAutoScaling::ScalableTarget`` resource specifies a resource that Application Auto Scaling can scale, such as an AWS::DynamoDB::Table or AWS::ECS::Service resource.
    .. epigraph::

       If the resource that you want Application Auto Scaling to scale is not yet created in your account, add a dependency on the resource when registering it as a scalable target using the `DependsOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ attribute.

    For more information, see `RegisterScalableTarget <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html>`_ in the *Application Auto Scaling API Reference* .

    :cloudformationResource: AWS::ApplicationAutoScaling::ScalableTarget
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_applicationautoscaling as applicationautoscaling
        
        cfn_scalable_target = applicationautoscaling.CfnScalableTarget(self, "MyCfnScalableTarget",
            max_capacity=123,
            min_capacity=123,
            resource_id="resourceId",
            role_arn="roleArn",
            scalable_dimension="scalableDimension",
            service_namespace="serviceNamespace",
        
            # the properties below are optional
            scheduled_actions=[applicationautoscaling.CfnScalableTarget.ScheduledActionProperty(
                schedule="schedule",
                scheduled_action_name="scheduledActionName",
        
                # the properties below are optional
                end_time=Date(),
                scalable_target_action=applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty(
                    max_capacity=123,
                    min_capacity=123
                ),
                start_time=Date(),
                timezone="timezone"
            )],
            suspended_state=applicationautoscaling.CfnScalableTarget.SuspendedStateProperty(
                dynamic_scaling_in_suspended=False,
                dynamic_scaling_out_suspended=False,
                scheduled_scaling_suspended=False
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        role_arn: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        scheduled_actions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]] = None,
        suspended_state: typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::ApplicationAutoScaling::ScalableTarget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param max_capacity: The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.
        :param min_capacity: The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.
        :param resource_id: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .
        :param role_arn: Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf. This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* . To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.
        :param scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param scheduled_actions: The scheduled actions for the scalable target. Duplicates aren't allowed. For more information about using scheduled scaling, see `Scheduled scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html>`_ in the *Application Auto Scaling User Guide* .
        :param suspended_state: An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities. *Suspension Outcomes* - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended. - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended. - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended. For more information, see `Suspending and resuming scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`_ in the *Application Auto Scaling User Guide* .
        '''
        props = CfnScalableTargetProps(
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            resource_id=resource_id,
            role_arn=role_arn,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            scheduled_actions=scheduled_actions,
            suspended_state=suspended_state,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        '''The maximum value that you plan to scale out to.

        When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        jsii.set(self, "maxCapacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        '''The minimum value that you plan to scale in to.

        When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        jsii.set(self, "minCapacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        '''The identifier of the resource associated with the scalable target.

        This string consists of the resource type and unique identifier.

        - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` .
        - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
        - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .
        - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` .
        - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` .
        - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` .
        - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
        - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ .
        - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .
        - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` .
        - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .
        - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` .
        - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` .
        - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` .
        - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        jsii.set(self, "resourceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.

        This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* .

        To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> builtins.str:
        '''The scalable dimension associated with the scalable target.

        This string consists of the service namespace, resource type, and scaling property.

        - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
        - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
        - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
        - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
        - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
        - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
        - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
        - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
        - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
        - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
        - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
        - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
        - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
        - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
        - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
        - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
        - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
        - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
        - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
        - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: builtins.str) -> None:
        jsii.set(self, "scalableDimension", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: builtins.str) -> None:
        jsii.set(self, "serviceNamespace", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduledActions")
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]]:
        '''The scheduled actions for the scalable target. Duplicates aren't allowed.

        For more information about using scheduled scaling, see `Scheduled scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html>`_ in the *Application Auto Scaling User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "scheduledActions"))

    @scheduled_actions.setter
    def scheduled_actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalableTarget.ScheduledActionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "scheduledActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="suspendedState")
    def suspended_state(
        self,
    ) -> typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]]:
        '''An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling.

        Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities.

        *Suspension Outcomes*

        - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.
        - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.
        - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.

        For more information, see `Suspending and resuming scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`_ in the *Application Auto Scaling User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate
        '''
        return typing.cast(typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]], jsii.get(self, "suspendedState"))

    @suspended_state.setter
    def suspended_state(
        self,
        value: typing.Optional[typing.Union["CfnScalableTarget.SuspendedStateProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "suspendedState", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalableTargetActionProperty:
        def __init__(
            self,
            *,
            max_capacity: typing.Optional[jsii.Number] = None,
            min_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``ScalableTargetAction`` specifies the minimum and maximum capacity for the ``ScalableTargetAction`` property of the `AWS::ApplicationAutoScaling::ScalableTarget ScheduledAction <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html>`_ property type.

            :param max_capacity: The maximum capacity.
            :param min_capacity: The minimum capacity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                scalable_target_action_property = applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty(
                    max_capacity=123,
                    min_capacity=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_capacity is not None:
                self._values["max_capacity"] = max_capacity
            if min_capacity is not None:
                self._values["min_capacity"] = min_capacity

        @builtins.property
        def max_capacity(self) -> typing.Optional[jsii.Number]:
            '''The maximum capacity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity
            '''
            result = self._values.get("max_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_capacity(self) -> typing.Optional[jsii.Number]:
            '''The minimum capacity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity
            '''
            result = self._values.get("min_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalableTargetActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget.ScheduledActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule": "schedule",
            "scheduled_action_name": "scheduledActionName",
            "end_time": "endTime",
            "scalable_target_action": "scalableTargetAction",
            "start_time": "startTime",
            "timezone": "timezone",
        },
    )
    class ScheduledActionProperty:
        def __init__(
            self,
            *,
            schedule: builtins.str,
            scheduled_action_name: builtins.str,
            end_time: typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]] = None,
            scalable_target_action: typing.Optional[typing.Union["CfnScalableTarget.ScalableTargetActionProperty", _IResolvable_a771d0ef]] = None,
            start_time: typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``ScheduledAction`` is a property of the `AWS::ApplicationAutoScaling::ScalableTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html>`_ resource that specifies a scheduled action for a scalable target.

            For more information, see `PutScheduledAction <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html>`_ in the *Application Auto Scaling API Reference* . For more information about scheduled scaling, including the format for cron expressions, see `Scheduled scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html>`_ in the *Application Auto Scaling User Guide* .

            :param schedule: The schedule for this action. The following formats are supported:. - At expressions - " ``at( *yyyy* - *mm* - *dd* T *hh* : *mm* : *ss* )`` " - Rate expressions - " ``rate( *value* *unit* )`` " - Cron expressions - " ``cron( *fields* )`` " At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval. At and cron expressions use Universal Coordinated Time (UTC) by default. The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day_of_Month] [Month] [Day_of_Week] [Year]. For rate expressions, *value* is a positive integer and *unit* is ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .
            :param scheduled_action_name: The name of the scheduled action. This name must be unique among all other scheduled actions on the specified scalable target.
            :param end_time: The date and time that the action is scheduled to end, in UTC.
            :param scalable_target_action: The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.
            :param start_time: The date and time that the action is scheduled to begin, in UTC.
            :param timezone: The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                scheduled_action_property = applicationautoscaling.CfnScalableTarget.ScheduledActionProperty(
                    schedule="schedule",
                    scheduled_action_name="scheduledActionName",
                
                    # the properties below are optional
                    end_time=Date(),
                    scalable_target_action=applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    start_time=Date(),
                    timezone="timezone"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "schedule": schedule,
                "scheduled_action_name": scheduled_action_name,
            }
            if end_time is not None:
                self._values["end_time"] = end_time
            if scalable_target_action is not None:
                self._values["scalable_target_action"] = scalable_target_action
            if start_time is not None:
                self._values["start_time"] = start_time
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule(self) -> builtins.str:
            '''The schedule for this action. The following formats are supported:.

            - At expressions - " ``at( *yyyy* - *mm* - *dd* T *hh* : *mm* : *ss* )`` "
            - Rate expressions - " ``rate( *value* *unit* )`` "
            - Cron expressions - " ``cron( *fields* )`` "

            At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval.

            At and cron expressions use Universal Coordinated Time (UTC) by default.

            The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day_of_Month] [Month] [Day_of_Week] [Year].

            For rate expressions, *value* is a positive integer and *unit* is ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-schedule
            '''
            result = self._values.get("schedule")
            assert result is not None, "Required property 'schedule' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scheduled_action_name(self) -> builtins.str:
            '''The name of the scheduled action.

            This name must be unique among all other scheduled actions on the specified scalable target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scheduledactionname
            '''
            result = self._values.get("scheduled_action_name")
            assert result is not None, "Required property 'scheduled_action_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]]:
            '''The date and time that the action is scheduled to end, in UTC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-endtime
            '''
            result = self._values.get("end_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]], result)

        @builtins.property
        def scalable_target_action(
            self,
        ) -> typing.Optional[typing.Union["CfnScalableTarget.ScalableTargetActionProperty", _IResolvable_a771d0ef]]:
            '''The new minimum and maximum capacity.

            You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scalabletargetaction
            '''
            result = self._values.get("scalable_target_action")
            return typing.cast(typing.Optional[typing.Union["CfnScalableTarget.ScalableTargetActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]]:
            '''The date and time that the action is scheduled to begin, in UTC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTarget.SuspendedStateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dynamic_scaling_in_suspended": "dynamicScalingInSuspended",
            "dynamic_scaling_out_suspended": "dynamicScalingOutSuspended",
            "scheduled_scaling_suspended": "scheduledScalingSuspended",
        },
    )
    class SuspendedStateProperty:
        def __init__(
            self,
            *,
            dynamic_scaling_in_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            dynamic_scaling_out_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            scheduled_scaling_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''``SuspendedState`` is a property of the `AWS::ApplicationAutoScaling::ScalableTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html>`_ resource that specifies whether the scaling activities for a scalable target are in a suspended state.

            :param dynamic_scaling_in_suspended: Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set the value to ``true`` if you don't want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is ``false`` .
            :param dynamic_scaling_out_suspended: Whether scale out by a target tracking scaling policy or a step scaling policy is suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is ``false`` .
            :param scheduled_scaling_suspended: Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                suspended_state_property = applicationautoscaling.CfnScalableTarget.SuspendedStateProperty(
                    dynamic_scaling_in_suspended=False,
                    dynamic_scaling_out_suspended=False,
                    scheduled_scaling_suspended=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dynamic_scaling_in_suspended is not None:
                self._values["dynamic_scaling_in_suspended"] = dynamic_scaling_in_suspended
            if dynamic_scaling_out_suspended is not None:
                self._values["dynamic_scaling_out_suspended"] = dynamic_scaling_out_suspended
            if scheduled_scaling_suspended is not None:
                self._values["scheduled_scaling_suspended"] = scheduled_scaling_suspended

        @builtins.property
        def dynamic_scaling_in_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether scale in by a target tracking scaling policy or a step scaling policy is suspended.

            Set the value to ``true`` if you don't want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalinginsuspended
            '''
            result = self._values.get("dynamic_scaling_in_suspended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def dynamic_scaling_out_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether scale out by a target tracking scaling policy or a step scaling policy is suspended.

            Set the value to ``true`` if you don't want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalingoutsuspended
            '''
            result = self._values.get("dynamic_scaling_out_suspended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def scheduled_scaling_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether scheduled scaling is suspended.

            Set the value to ``true`` if you don't want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-scheduledscalingsuspended
            '''
            result = self._values.get("scheduled_scaling_suspended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuspendedStateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalableTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "role_arn": "roleArn",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "scheduled_actions": "scheduledActions",
        "suspended_state": "suspendedState",
    },
)
class CfnScalableTargetProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        role_arn: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        scheduled_actions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnScalableTarget.ScheduledActionProperty, _IResolvable_a771d0ef]]]] = None,
        suspended_state: typing.Optional[typing.Union[CfnScalableTarget.SuspendedStateProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScalableTarget``.

        :param max_capacity: The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.
        :param min_capacity: The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.
        :param resource_id: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .
        :param role_arn: Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf. This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* . To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.
        :param scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param scheduled_actions: The scheduled actions for the scalable target. Duplicates aren't allowed. For more information about using scheduled scaling, see `Scheduled scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html>`_ in the *Application Auto Scaling User Guide* .
        :param suspended_state: An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities. *Suspension Outcomes* - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended. - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended. - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended. For more information, see `Suspending and resuming scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`_ in the *Application Auto Scaling User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            
            cfn_scalable_target_props = applicationautoscaling.CfnScalableTargetProps(
                max_capacity=123,
                min_capacity=123,
                resource_id="resourceId",
                role_arn="roleArn",
                scalable_dimension="scalableDimension",
                service_namespace="serviceNamespace",
            
                # the properties below are optional
                scheduled_actions=[applicationautoscaling.CfnScalableTarget.ScheduledActionProperty(
                    schedule="schedule",
                    scheduled_action_name="scheduledActionName",
            
                    # the properties below are optional
                    end_time=Date(),
                    scalable_target_action=applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    start_time=Date(),
                    timezone="timezone"
                )],
                suspended_state=applicationautoscaling.CfnScalableTarget.SuspendedStateProperty(
                    dynamic_scaling_in_suspended=False,
                    dynamic_scaling_out_suspended=False,
                    scheduled_scaling_suspended=False
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "role_arn": role_arn,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }
        if scheduled_actions is not None:
            self._values["scheduled_actions"] = scheduled_actions
        if suspended_state is not None:
            self._values["suspended_state"] = suspended_state

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''The maximum value that you plan to scale out to.

        When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity
        '''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''The minimum value that you plan to scale in to.

        When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity
        '''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The identifier of the resource associated with the scalable target.

        This string consists of the resource type and unique identifier.

        - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` .
        - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
        - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .
        - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` .
        - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` .
        - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` .
        - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
        - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ .
        - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .
        - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` .
        - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .
        - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` .
        - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` .
        - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` .
        - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.

        This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* .

        To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''The scalable dimension associated with the scalable target.

        This string consists of the service namespace, resource type, and scaling property.

        - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
        - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
        - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
        - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
        - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
        - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
        - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
        - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
        - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
        - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
        - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
        - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
        - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
        - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
        - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
        - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
        - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
        - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
        - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
        - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension
        '''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace
        '''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnScalableTarget.ScheduledActionProperty, _IResolvable_a771d0ef]]]]:
        '''The scheduled actions for the scalable target. Duplicates aren't allowed.

        For more information about using scheduled scaling, see `Scheduled scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html>`_ in the *Application Auto Scaling User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions
        '''
        result = self._values.get("scheduled_actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnScalableTarget.ScheduledActionProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def suspended_state(
        self,
    ) -> typing.Optional[typing.Union[CfnScalableTarget.SuspendedStateProperty, _IResolvable_a771d0ef]]:
        '''An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling.

        Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities.

        *Suspension Outcomes*

        - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.
        - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.
        - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.

        For more information, see `Suspending and resuming scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`_ in the *Application Auto Scaling User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate
        '''
        result = self._values.get("suspended_state")
        return typing.cast(typing.Optional[typing.Union[CfnScalableTarget.SuspendedStateProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalableTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnScalingPolicy(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy",
):
    '''A CloudFormation ``AWS::ApplicationAutoScaling::ScalingPolicy``.

    The ``AWS::ApplicationAutoScaling::ScalingPolicy`` resource defines a scaling policy that Application Auto Scaling uses to adjust the capacity of a scalable target.

    For more information, see `PutScalingPolicy <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html>`_ in the *Application Auto Scaling API Reference* . For more information about Application Auto Scaling scaling policies, see `Target tracking scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html>`_ and `Step scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html>`_ in the *Application Auto Scaling User Guide* .

    :cloudformationResource: AWS::ApplicationAutoScaling::ScalingPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_applicationautoscaling as applicationautoscaling
        
        cfn_scaling_policy = applicationautoscaling.CfnScalingPolicy(self, "MyCfnScalingPolicy",
            policy_name="policyName",
            policy_type="policyType",
        
            # the properties below are optional
            resource_id="resourceId",
            scalable_dimension="scalableDimension",
            scaling_target_id="scalingTargetId",
            service_namespace="serviceNamespace",
            step_scaling_policy_configuration=applicationautoscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty(
                adjustment_type="adjustmentType",
                cooldown=123,
                metric_aggregation_type="metricAggregationType",
                min_adjustment_magnitude=123,
                step_adjustments=[applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty(
                    scaling_adjustment=123,
        
                    # the properties below are optional
                    metric_interval_lower_bound=123,
                    metric_interval_upper_bound=123
                )]
            ),
            target_tracking_scaling_policy_configuration=applicationautoscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty(
                target_value=123,
        
                # the properties below are optional
                customized_metric_specification=applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                    metric_name="metricName",
                    namespace="namespace",
                    statistic="statistic",
        
                    # the properties below are optional
                    dimensions=[applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    unit="unit"
                ),
                disable_scale_in=False,
                predefined_metric_specification=applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                    predefined_metric_type="predefinedMetricType",
        
                    # the properties below are optional
                    resource_label="resourceLabel"
                ),
                scale_in_cooldown=123,
                scale_out_cooldown=123
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        policy_type: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        scalable_dimension: typing.Optional[builtins.str] = None,
        scaling_target_id: typing.Optional[builtins.str] = None,
        service_namespace: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::ApplicationAutoScaling::ScalingPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_name: The name of the scaling policy.
        :param policy_type: The scaling policy type. The following policy types are supported: ``TargetTrackingScaling`` —Not supported for Amazon EMR ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
        :param resource_id: The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .
        :param scalable_dimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
        :param scaling_target_id: The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource. .. epigraph:: You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param step_scaling_policy_configuration: A step scaling policy.
        :param target_tracking_scaling_policy_configuration: A target tracking scaling policy.
        '''
        props = CfnScalingPolicyProps(
            policy_name=policy_name,
            policy_type=policy_type,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            scaling_target_id=scaling_target_id,
            service_namespace=service_namespace,
            step_scaling_policy_configuration=step_scaling_policy_configuration,
            target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        jsii.set(self, "policyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        '''The scaling policy type.

        The following policy types are supported:

        ``TargetTrackingScaling`` —Not supported for Amazon EMR

        ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        jsii.set(self, "policyType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the resource associated with the scaling policy.

        This string consists of the resource type and unique identifier.

        - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` .
        - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
        - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .
        - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` .
        - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` .
        - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` .
        - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
        - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ .
        - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .
        - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` .
        - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .
        - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` .
        - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` .
        - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` .
        - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> typing.Optional[builtins.str]:
        '''The scalable dimension. This string consists of the service namespace, resource type, and scaling property.

        - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
        - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
        - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
        - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
        - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
        - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
        - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
        - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
        - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
        - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
        - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
        - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
        - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
        - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
        - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
        - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
        - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
        - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
        - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
        - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scalableDimension", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalingTargetId")
    def scaling_target_id(self) -> typing.Optional[builtins.str]:
        '''The CloudFormation-generated ID of an Application Auto Scaling scalable target.

        For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource.
        .. epigraph::

           You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalingTargetId"))

    @scaling_target_id.setter
    def scaling_target_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scalingTargetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceNamespace", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]]:
        '''A step scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "stepScalingPolicyConfiguration"))

    @step_scaling_policy_configuration.setter
    def step_scaling_policy_configuration(
        self,
        value: typing.Optional[typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "stepScalingPolicyConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]]:
        '''A target tracking scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "targetTrackingScalingPolicyConfiguration"))

    @target_tracking_scaling_policy_configuration.setter
    def target_tracking_scaling_policy_configuration(
        self,
        value: typing.Optional[typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "targetTrackingScalingPolicyConfiguration", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "statistic": "statistic",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class CustomizedMetricSpecificationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            statistic: builtins.str,
            dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnScalingPolicy.MetricDimensionProperty", _IResolvable_a771d0ef]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains customized metric specification information for a target tracking scaling policy for Application Auto Scaling.

            For information about the available metrics for a service, see `AWS services that publish CloudWatch metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_ in the *Amazon CloudWatch User Guide* .

            To create your customized metric specification:

            - Add values for each required parameter from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see `Publish custom metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`_ in the *Amazon CloudWatch User Guide* .
            - Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases, and increase when capacity decreases.

            For more information about CloudWatch, see `Amazon CloudWatch concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`_ .

            ``CustomizedMetricSpecification`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingScalingPolicyConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html>`_ property type.

            :param metric_name: The name of the metric.
            :param namespace: The namespace of the metric.
            :param statistic: The statistic of the metric.
            :param dimensions: The dimensions of the metric. Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
            :param unit: The unit of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                customized_metric_specification_property = applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                    metric_name="metricName",
                    namespace="namespace",
                    statistic="statistic",
                
                    # the properties below are optional
                    dimensions=[applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    unit="unit"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
                "statistic": statistic,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def statistic(self) -> builtins.str:
            '''The statistic of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic
            '''
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.MetricDimensionProperty", _IResolvable_a771d0ef]]]]:
            '''The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.MetricDimensionProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''``MetricDimension`` specifies a name/value pair that is part of the identity of a CloudWatch metric for the ``Dimensions`` property of the `AWS::ApplicationAutoScaling::ScalingPolicy CustomizedMetricSpecification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html>`_ property type. Duplicate dimensions are not allowed.

            :param name: The name of the dimension.
            :param value: The value of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                metric_dimension_property = applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_metric_type": "predefinedMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains predefined metric specification information for a target tracking scaling policy for Application Auto Scaling.

            ``PredefinedMetricSpecification`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingScalingPolicyConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html>`_ property type.

            :param predefined_metric_type: The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot fleet requests and ECS services.
            :param resource_label: Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached to the Spot Fleet or ECS service. You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is: ``app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`` . Where: - app// is the final portion of the load balancer ARN - targetgroup// is the final portion of the target group ARN. To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                predefined_metric_specification_property = applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                    predefined_metric_type="predefinedMetricType",
                
                    # the properties below are optional
                    resource_label="resourceLabel"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "predefined_metric_type": predefined_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_metric_type(self) -> builtins.str:
            '''The metric type.

            The ``ALBRequestCountPerTarget`` metric type applies only to Spot fleet requests and ECS services.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype
            '''
            result = self._values.get("predefined_metric_type")
            assert result is not None, "Required property 'predefined_metric_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            '''Identifies the resource associated with the metric type.

            You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached to the Spot Fleet or ECS service.

            You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is:

            ``app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`` .

            Where:

            - app// is the final portion of the load balancer ARN
            - targetgroup// is the final portion of the target group ARN.

            To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel
            '''
            result = self._values.get("resource_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "metric_interval_lower_bound": "metricIntervalLowerBound",
            "metric_interval_upper_bound": "metricIntervalUpperBound",
        },
    )
    class StepAdjustmentProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            metric_interval_lower_bound: typing.Optional[jsii.Number] = None,
            metric_interval_upper_bound: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``StepAdjustment`` specifies a step adjustment for the ``StepAdjustments`` property of the `AWS::ApplicationAutoScaling::ScalingPolicy StepScalingPolicyConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html>`_ property type.

            For the following examples, suppose that you have an alarm with a breach threshold of 50:

            - To trigger a step adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
            - To trigger a step adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

            For more information, see `Step adjustments <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html#as-scaling-steps>`_ in the *Application Auto Scaling User Guide* .

            You can find a sample template snippet in the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#aws-resource-applicationautoscaling-scalingpolicy--examples>`_ section of the ``AWS::ApplicationAutoScaling::ScalingPolicy`` documentation.

            :param scaling_adjustment: The amount by which to scale. The adjustment is based on the value that you specified in the ``AdjustmentType`` property (either an absolute number or a percentage). A positive value adds to the current capacity and a negative number subtracts from the current capacity.
            :param metric_interval_lower_bound: The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity. You must specify at least one upper or lower bound.
            :param metric_interval_upper_bound: The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity. You must specify at least one upper or lower bound.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                step_adjustment_property = applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty(
                    scaling_adjustment=123,
                
                    # the properties below are optional
                    metric_interval_lower_bound=123,
                    metric_interval_upper_bound=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if metric_interval_lower_bound is not None:
                self._values["metric_interval_lower_bound"] = metric_interval_lower_bound
            if metric_interval_upper_bound is not None:
                self._values["metric_interval_upper_bound"] = metric_interval_upper_bound

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            '''The amount by which to scale.

            The adjustment is based on the value that you specified in the ``AdjustmentType`` property (either an absolute number or a percentage). A positive value adds to the current capacity and a negative number subtracts from the current capacity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def metric_interval_lower_bound(self) -> typing.Optional[jsii.Number]:
            '''The lower bound for the difference between the alarm threshold and the CloudWatch metric.

            If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

            You must specify at least one upper or lower bound.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervallowerbound
            '''
            result = self._values.get("metric_interval_lower_bound")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def metric_interval_upper_bound(self) -> typing.Optional[jsii.Number]:
            '''The upper bound for the difference between the alarm threshold and the CloudWatch metric.

            If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.

            You must specify at least one upper or lower bound.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervalupperbound
            '''
            result = self._values.get("metric_interval_upper_bound")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepAdjustmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adjustment_type": "adjustmentType",
            "cooldown": "cooldown",
            "metric_aggregation_type": "metricAggregationType",
            "min_adjustment_magnitude": "minAdjustmentMagnitude",
            "step_adjustments": "stepAdjustments",
        },
    )
    class StepScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            adjustment_type: typing.Optional[builtins.str] = None,
            cooldown: typing.Optional[jsii.Number] = None,
            metric_aggregation_type: typing.Optional[builtins.str] = None,
            min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
            step_adjustments: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnScalingPolicy.StepAdjustmentProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''``StepScalingPolicyConfiguration`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`_ resource that specifies a step scaling policy configuration for Application Auto Scaling.

            For more information, see `PutScalingPolicy <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html>`_ in the *Application Auto Scaling API Reference* . For more information about step scaling policies, see `Step scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html>`_ in the *Application Auto Scaling User Guide* .

            :param adjustment_type: Specifies whether the ``ScalingAdjustment`` value in the ``StepAdjustment`` property is an absolute number or a percentage of the current capacity.
            :param cooldown: The amount of time, in seconds, to wait for a previous scaling activity to take effect. With scale-out policies, the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a step scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends. While the cooldown period is in effect, capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity. For example, when an alarm triggers a step scaling policy to increase the capacity by 2, the scaling activity completes successfully, and a cooldown period starts. If the alarm triggers again during the cooldown period but at a more aggressive step adjustment of 3, the previous increase of 2 is considered part of the current capacity. Therefore, only 1 is added to the capacity. With scale-in policies, the intention is to scale in conservatively to protect your application’s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the cooldown period after a scale-in activity, Application Auto Scaling scales out the target immediately. In this case, the cooldown period for the scale-in activity stops and doesn't complete. Application Auto Scaling provides a default value of 600 for Amazon ElastiCache replication groups and a default value of 300 for the following scalable targets: - AppStream 2.0 fleets - Aurora DB clusters - ECS services - EMR clusters - Neptune clusters - SageMaker endpoint variants - Spot Fleets - Custom resources For all other scalable targets, the default value is 0: - Amazon Comprehend document classification and entity recognizer endpoints - DynamoDB tables and global secondary indexes - Amazon Keyspaces tables - Lambda provisioned concurrency - Amazon MSK broker storage
            :param metric_aggregation_type: The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .
            :param min_adjustment_magnitude: The minimum value to scale by when the adjustment type is ``PercentChangeInCapacity`` . For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out the service by 2 tasks.
            :param step_adjustments: A set of adjustments that enable you to scale based on the size of the alarm breach. At least one step adjustment is required if you are adding a new step scaling policy configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                step_scaling_policy_configuration_property = applicationautoscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty(
                    adjustment_type="adjustmentType",
                    cooldown=123,
                    metric_aggregation_type="metricAggregationType",
                    min_adjustment_magnitude=123,
                    step_adjustments=[applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty(
                        scaling_adjustment=123,
                
                        # the properties below are optional
                        metric_interval_lower_bound=123,
                        metric_interval_upper_bound=123
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cooldown is not None:
                self._values["cooldown"] = cooldown
            if metric_aggregation_type is not None:
                self._values["metric_aggregation_type"] = metric_aggregation_type
            if min_adjustment_magnitude is not None:
                self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
            if step_adjustments is not None:
                self._values["step_adjustments"] = step_adjustments

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the ``ScalingAdjustment`` value in the ``StepAdjustment`` property is an absolute number or a percentage of the current capacity.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype
            '''
            result = self._values.get("adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, to wait for a previous scaling activity to take effect.

            With scale-out policies, the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a step scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends. While the cooldown period is in effect, capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity. For example, when an alarm triggers a step scaling policy to increase the capacity by 2, the scaling activity completes successfully, and a cooldown period starts. If the alarm triggers again during the cooldown period but at a more aggressive step adjustment of 3, the previous increase of 2 is considered part of the current capacity. Therefore, only 1 is added to the capacity.

            With scale-in policies, the intention is to scale in conservatively to protect your application’s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the cooldown period after a scale-in activity, Application Auto Scaling scales out the target immediately. In this case, the cooldown period for the scale-in activity stops and doesn't complete.

            Application Auto Scaling provides a default value of 600 for Amazon ElastiCache replication groups and a default value of 300 for the following scalable targets:

            - AppStream 2.0 fleets
            - Aurora DB clusters
            - ECS services
            - EMR clusters
            - Neptune clusters
            - SageMaker endpoint variants
            - Spot Fleets
            - Custom resources

            For all other scalable targets, the default value is 0:

            - Amazon Comprehend document classification and entity recognizer endpoints
            - DynamoDB tables and global secondary indexes
            - Amazon Keyspaces tables
            - Lambda provisioned concurrency
            - Amazon MSK broker storage

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown
            '''
            result = self._values.get("cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
            '''The aggregation type for the CloudWatch metrics.

            Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype
            '''
            result = self._values.get("metric_aggregation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
            '''The minimum value to scale by when the adjustment type is ``PercentChangeInCapacity`` .

            For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out the service by 2 tasks.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude
            '''
            result = self._values.get("min_adjustment_magnitude")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def step_adjustments(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.StepAdjustmentProperty", _IResolvable_a771d0ef]]]]:
            '''A set of adjustments that enable you to scale based on the size of the alarm breach.

            At least one step adjustment is required if you are adding a new step scaling policy configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments
            '''
            result = self._values.get("step_adjustments")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnScalingPolicy.StepAdjustmentProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_value": "targetValue",
            "customized_metric_specification": "customizedMetricSpecification",
            "disable_scale_in": "disableScaleIn",
            "predefined_metric_specification": "predefinedMetricSpecification",
            "scale_in_cooldown": "scaleInCooldown",
            "scale_out_cooldown": "scaleOutCooldown",
        },
    )
    class TargetTrackingScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            target_value: jsii.Number,
            customized_metric_specification: typing.Optional[typing.Union["CfnScalingPolicy.CustomizedMetricSpecificationProperty", _IResolvable_a771d0ef]] = None,
            disable_scale_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            predefined_metric_specification: typing.Optional[typing.Union["CfnScalingPolicy.PredefinedMetricSpecificationProperty", _IResolvable_a771d0ef]] = None,
            scale_in_cooldown: typing.Optional[jsii.Number] = None,
            scale_out_cooldown: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``TargetTrackingScalingPolicyConfiguration`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`_ resource that specifies a target tracking scaling policy configuration for Application Auto Scaling. Use a target tracking scaling policy to adjust the capacity of the specified scalable target in response to actual workloads, so that resource utilization remains at or near the target utilization value.

            For more information, see `PutScalingPolicy <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html>`_ in the *Application Auto Scaling API Reference* . For more information about target tracking scaling policies, see `Target tracking scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html>`_ in the *Application Auto Scaling User Guide* .

            :param target_value: The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360. The value must be a valid number based on the choice of metric. For example, if the metric is CPU utilization, then the target value is a percent value that represents how much of the CPU can be used before scaling out.
            :param customized_metric_specification: A customized metric. You can specify either a predefined metric or a customized metric.
            :param disable_scale_in: Indicates whether scale in by the target tracking scaling policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking scaling policy won't remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is ``false`` .
            :param predefined_metric_specification: A predefined metric. You can specify either a predefined metric or a customized metric.
            :param scale_in_cooldown: The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. With the *scale-in cooldown period* , the intention is to scale in conservatively to protect your application’s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Application Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn't complete. Application Auto Scaling provides a default value of 600 for Amazon ElastiCache replication groups and a default value of 300 for the following scalable targets: - AppStream 2.0 fleets - Aurora DB clusters - ECS services - EMR clusters - Neptune clusters - SageMaker endpoint variants - Spot Fleets - Custom resources For all other scalable targets, the default value is 0: - Amazon Comprehend document classification and entity recognizer endpoints - DynamoDB tables and global secondary indexes - Amazon Keyspaces tables - Lambda provisioned concurrency - Amazon MSK broker storage
            :param scale_out_cooldown: The amount of time, in seconds, to wait for a previous scale-out activity to take effect. With the *scale-out cooldown period* , the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a target tracking scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends. While the cooldown period is in effect, the capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity. Application Auto Scaling provides a default value of 600 for Amazon ElastiCache replication groups and a default value of 300 for the following scalable targets: - AppStream 2.0 fleets - Aurora DB clusters - ECS services - EMR clusters - Neptune clusters - SageMaker endpoint variants - Spot Fleets - Custom resources For all other scalable targets, the default value is 0: - Amazon Comprehend document classification and entity recognizer endpoints - DynamoDB tables and global secondary indexes - Amazon Keyspaces tables - Lambda provisioned concurrency - Amazon MSK broker storage

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_applicationautoscaling as applicationautoscaling
                
                target_tracking_scaling_policy_configuration_property = applicationautoscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty(
                    target_value=123,
                
                    # the properties below are optional
                    customized_metric_specification=applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                        metric_name="metricName",
                        namespace="namespace",
                        statistic="statistic",
                
                        # the properties below are optional
                        dimensions=[applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        unit="unit"
                    ),
                    disable_scale_in=False,
                    predefined_metric_specification=applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                        predefined_metric_type="predefinedMetricType",
                
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target_value": target_value,
            }
            if customized_metric_specification is not None:
                self._values["customized_metric_specification"] = customized_metric_specification
            if disable_scale_in is not None:
                self._values["disable_scale_in"] = disable_scale_in
            if predefined_metric_specification is not None:
                self._values["predefined_metric_specification"] = predefined_metric_specification
            if scale_in_cooldown is not None:
                self._values["scale_in_cooldown"] = scale_in_cooldown
            if scale_out_cooldown is not None:
                self._values["scale_out_cooldown"] = scale_out_cooldown

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''The target value for the metric.

            Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360. The value must be a valid number based on the choice of metric. For example, if the metric is CPU utilization, then the target value is a percent value that represents how much of the CPU can be used before scaling out.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def customized_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPolicy.CustomizedMetricSpecificationProperty", _IResolvable_a771d0ef]]:
            '''A customized metric.

            You can specify either a predefined metric or a customized metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification
            '''
            result = self._values.get("customized_metric_specification")
            return typing.cast(typing.Optional[typing.Union["CfnScalingPolicy.CustomizedMetricSpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def disable_scale_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Indicates whether scale in by the target tracking scaling policy is disabled.

            If the value is ``true`` , scale in is disabled and the target tracking scaling policy won't remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein
            '''
            result = self._values.get("disable_scale_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def predefined_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPolicy.PredefinedMetricSpecificationProperty", _IResolvable_a771d0ef]]:
            '''A predefined metric.

            You can specify either a predefined metric or a customized metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification
            '''
            result = self._values.get("predefined_metric_specification")
            return typing.cast(typing.Optional[typing.Union["CfnScalingPolicy.PredefinedMetricSpecificationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start.

            With the *scale-in cooldown period* , the intention is to scale in conservatively to protect your application’s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Application Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn't complete.

            Application Auto Scaling provides a default value of 600 for Amazon ElastiCache replication groups and a default value of 300 for the following scalable targets:

            - AppStream 2.0 fleets
            - Aurora DB clusters
            - ECS services
            - EMR clusters
            - Neptune clusters
            - SageMaker endpoint variants
            - Spot Fleets
            - Custom resources

            For all other scalable targets, the default value is 0:

            - Amazon Comprehend document classification and entity recognizer endpoints
            - DynamoDB tables and global secondary indexes
            - Amazon Keyspaces tables
            - Lambda provisioned concurrency
            - Amazon MSK broker storage

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown
            '''
            result = self._values.get("scale_in_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, to wait for a previous scale-out activity to take effect.

            With the *scale-out cooldown period* , the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a target tracking scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends. While the cooldown period is in effect, the capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity.

            Application Auto Scaling provides a default value of 600 for Amazon ElastiCache replication groups and a default value of 300 for the following scalable targets:

            - AppStream 2.0 fleets
            - Aurora DB clusters
            - ECS services
            - EMR clusters
            - Neptune clusters
            - SageMaker endpoint variants
            - Spot Fleets
            - Custom resources

            For all other scalable targets, the default value is 0:

            - Amazon Comprehend document classification and entity recognizer endpoints
            - DynamoDB tables and global secondary indexes
            - Amazon Keyspaces tables
            - Lambda provisioned concurrency
            - Amazon MSK broker storage

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown
            '''
            result = self._values.get("scale_out_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.CfnScalingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_name": "policyName",
        "policy_type": "policyType",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "scaling_target_id": "scalingTargetId",
        "service_namespace": "serviceNamespace",
        "step_scaling_policy_configuration": "stepScalingPolicyConfiguration",
        "target_tracking_scaling_policy_configuration": "targetTrackingScalingPolicyConfiguration",
    },
)
class CfnScalingPolicyProps:
    def __init__(
        self,
        *,
        policy_name: builtins.str,
        policy_type: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        scalable_dimension: typing.Optional[builtins.str] = None,
        scaling_target_id: typing.Optional[builtins.str] = None,
        service_namespace: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScalingPolicy``.

        :param policy_name: The name of the scaling policy.
        :param policy_type: The scaling policy type. The following policy types are supported: ``TargetTrackingScaling`` —Not supported for Amazon EMR ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
        :param resource_id: The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .
        :param scalable_dimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
        :param scaling_target_id: The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource. .. epigraph:: You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param step_scaling_policy_configuration: A step scaling policy.
        :param target_tracking_scaling_policy_configuration: A target tracking scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            
            cfn_scaling_policy_props = applicationautoscaling.CfnScalingPolicyProps(
                policy_name="policyName",
                policy_type="policyType",
            
                # the properties below are optional
                resource_id="resourceId",
                scalable_dimension="scalableDimension",
                scaling_target_id="scalingTargetId",
                service_namespace="serviceNamespace",
                step_scaling_policy_configuration=applicationautoscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty(
                    adjustment_type="adjustmentType",
                    cooldown=123,
                    metric_aggregation_type="metricAggregationType",
                    min_adjustment_magnitude=123,
                    step_adjustments=[applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty(
                        scaling_adjustment=123,
            
                        # the properties below are optional
                        metric_interval_lower_bound=123,
                        metric_interval_upper_bound=123
                    )]
                ),
                target_tracking_scaling_policy_configuration=applicationautoscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty(
                    target_value=123,
            
                    # the properties below are optional
                    customized_metric_specification=applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                        metric_name="metricName",
                        namespace="namespace",
                        statistic="statistic",
            
                        # the properties below are optional
                        dimensions=[applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        unit="unit"
                    ),
                    disable_scale_in=False,
                    predefined_metric_specification=applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                        predefined_metric_type="predefinedMetricType",
            
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "policy_name": policy_name,
            "policy_type": policy_type,
        }
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if scalable_dimension is not None:
            self._values["scalable_dimension"] = scalable_dimension
        if scaling_target_id is not None:
            self._values["scaling_target_id"] = scaling_target_id
        if service_namespace is not None:
            self._values["service_namespace"] = service_namespace
        if step_scaling_policy_configuration is not None:
            self._values["step_scaling_policy_configuration"] = step_scaling_policy_configuration
        if target_tracking_scaling_policy_configuration is not None:
            self._values["target_tracking_scaling_policy_configuration"] = target_tracking_scaling_policy_configuration

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''The scaling policy type.

        The following policy types are supported:

        ``TargetTrackingScaling`` —Not supported for Amazon EMR

        ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype
        '''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the resource associated with the scaling policy.

        This string consists of the resource type and unique identifier.

        - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` .
        - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
        - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .
        - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` .
        - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` .
        - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` .
        - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
        - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ .
        - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .
        - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` .
        - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .
        - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` .
        - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` .
        - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` .
        - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scalable_dimension(self) -> typing.Optional[builtins.str]:
        '''The scalable dimension. This string consists of the service namespace, resource type, and scaling property.

        - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
        - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
        - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
        - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
        - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
        - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
        - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
        - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
        - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
        - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
        - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
        - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
        - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
        - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
        - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
        - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
        - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
        - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
        - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
        - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension
        '''
        result = self._values.get("scalable_dimension")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_target_id(self) -> typing.Optional[builtins.str]:
        '''The CloudFormation-generated ID of an Application Auto Scaling scalable target.

        For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource.
        .. epigraph::

           You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid
        '''
        result = self._values.get("scaling_target_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace
        '''
        result = self._values.get("service_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]]:
        '''A step scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration
        '''
        result = self._values.get("step_scaling_policy_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]]:
        '''A target tracking scaling policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration
        '''
        result = self._values.get("target_tracking_scaling_policy_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.CronOptions",
    jsii_struct_bases=[],
    name_mapping={
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "week_day": "weekDay",
        "year": "year",
    },
)
class CronOptions:
    def __init__(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options to configure a cron expression.

        All fields are strings so you can use complex expressions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: (experimental) The day of the month to run this rule at. Default: - Every day of the month
        :param hour: (experimental) The hour to run this rule at. Default: - Every hour
        :param minute: (experimental) The minute to run this rule at. Default: - Every minute
        :param month: (experimental) The month to run this rule at. Default: - Every month
        :param week_day: (experimental) The day of the week to run this rule at. Default: - Any day of the week
        :param year: (experimental) The year to run this rule at. Default: - Every year

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
        :stability: experimental
        :exampleMetadata: infused

        Example::

            # resource is of type SomeScalableResource
            
            
            capacity = resource.auto_scale_capacity(
                min_capacity=1,
                max_capacity=50
            )
            
            capacity.scale_on_schedule("PrescaleInTheMorning",
                schedule=appscaling.Schedule.cron(hour="8", minute="0"),
                min_capacity=20
            )
            
            capacity.scale_on_schedule("AllowDownscalingAtNight",
                schedule=appscaling.Schedule.cron(hour="20", minute="0"),
                min_capacity=1
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if hour is not None:
            self._values["hour"] = hour
        if minute is not None:
            self._values["minute"] = minute
        if month is not None:
            self._values["month"] = month
        if week_day is not None:
            self._values["week_day"] = week_day
        if year is not None:
            self._values["year"] = year

    @builtins.property
    def day(self) -> typing.Optional[builtins.str]:
        '''(experimental) The day of the month to run this rule at.

        :default: - Every day of the month

        :stability: experimental
        '''
        result = self._values.get("day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hour(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hour to run this rule at.

        :default: - Every hour

        :stability: experimental
        '''
        result = self._values.get("hour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute(self) -> typing.Optional[builtins.str]:
        '''(experimental) The minute to run this rule at.

        :default: - Every minute

        :stability: experimental
        '''
        result = self._values.get("minute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def month(self) -> typing.Optional[builtins.str]:
        '''(experimental) The month to run this rule at.

        :default: - Every month

        :stability: experimental
        '''
        result = self._values.get("month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def week_day(self) -> typing.Optional[builtins.str]:
        '''(experimental) The day of the week to run this rule at.

        :default: - Any day of the week

        :stability: experimental
        '''
        result = self._values.get("week_day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def year(self) -> typing.Optional[builtins.str]:
        '''(experimental) The year to run this rule at.

        :default: - Every year

        :stability: experimental
        '''
        result = self._values.get("year")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.EnableScalingProps",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class EnableScalingProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for enabling Application Auto Scaling.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # cluster is of type Cluster
            
            load_balanced_fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "Service",
                cluster=cluster,
                memory_limit_mi_b=1024,
                desired_count=1,
                cpu=512,
                task_image_options=ecs.aws_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                    image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
                )
            )
            
            scalable_target = load_balanced_fargate_service.service.auto_scale_task_count(
                min_capacity=1,
                max_capacity=20
            )
            
            scalable_target.scale_on_cpu_utilization("CpuScaling",
                target_utilization_percent=50
            )
            
            scalable_target.scale_on_memory_utilization("MemoryScaling",
                target_utilization_percent=50
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
        }
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''(experimental) Maximum capacity to scale to.

        :stability: experimental
        '''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Minimum capacity to scale to.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnableScalingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_applicationautoscaling.IScalableTarget")
class IScalableTarget(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        '''
        :stability: experimental
        :attribute: true
        '''
        ...


class _IScalableTargetProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore[misc]
):
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_applicationautoscaling.IScalableTarget"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        '''
        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalableTargetId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalableTarget).__jsii_proxy_class__ = lambda : _IScalableTargetProxy


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.MetricAggregationType")
class MetricAggregationType(enum.Enum):
    '''(experimental) How the scaling metric is going to be aggregated.

    :stability: experimental
    '''

    AVERAGE = "AVERAGE"
    '''(experimental) Average.

    :stability: experimental
    '''
    MINIMUM = "MINIMUM"
    '''(experimental) Minimum.

    :stability: experimental
    '''
    MAXIMUM = "MAXIMUM"
    '''(experimental) Maximum.

    :stability: experimental
    '''


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.PredefinedMetric")
class PredefinedMetric(enum.Enum):
    '''(experimental) One of the predefined autoscaling metrics.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as lambda_
        
        # code is of type Code
        
        
        handler = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="index.handler",
            code=code,
        
            reserved_concurrent_executions=2
        )
        
        fn_ver = handler.add_version("CDKLambdaVersion", undefined, "demo alias", 10)
        
        target = appscaling.ScalableTarget(self, "ScalableTarget",
            service_namespace=appscaling.ServiceNamespace.LAMBDA,
            max_capacity=100,
            min_capacity=10,
            resource_id=f"function:{handler.functionName}:{fnVer.version}",
            scalable_dimension="lambda:function:ProvisionedConcurrency"
        )
        
        target.scale_to_track_metric("PceTracking",
            target_value=0.9,
            predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
        )
    '''

    DYNAMODB_READ_CAPACITY_UTILIZATION = "DYNAMODB_READ_CAPACITY_UTILIZATION"
    '''(experimental) DYNAMODB_READ_CAPACITY_UTILIZATIO.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    DYANMODB_WRITE_CAPACITY_UTILIZATION = "DYANMODB_WRITE_CAPACITY_UTILIZATION"
    '''(experimental) DYANMODB_WRITE_CAPACITY_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    ALB_REQUEST_COUNT_PER_TARGET = "ALB_REQUEST_COUNT_PER_TARGET"
    '''(experimental) ALB_REQUEST_COUNT_PER_TARGET.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    RDS_READER_AVERAGE_CPU_UTILIZATION = "RDS_READER_AVERAGE_CPU_UTILIZATION"
    '''(experimental) RDS_READER_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    RDS_READER_AVERAGE_DATABASE_CONNECTIONS = "RDS_READER_AVERAGE_DATABASE_CONNECTIONS"
    '''(experimental) RDS_READER_AVERAGE_DATABASE_CONNECTIONS.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION = "EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION"
    '''(experimental) EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN = "EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN"
    '''(experimental) EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT = "EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT"
    '''(experimental) EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE = "SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE"
    '''(experimental) SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    ECS_SERVICE_AVERAGE_CPU_UTILIZATION = "ECS_SERVICE_AVERAGE_CPU_UTILIZATION"
    '''(experimental) ECS_SERVICE_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION = "ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION"
    '''(experimental) ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION = "LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION"
    '''(experimental) LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION.

    :see: https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-concurrency
    :stability: experimental
    '''
    KAFKA_BROKER_STORAGE_UTILIZATION = "KAFKA_BROKER_STORAGE_UTILIZATION"
    '''(experimental) KAFKA_BROKER_STORAGE_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION = "ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION"
    '''(experimental) ELASTIC_CACHE_PRIMARY_ENGINE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    ELASTICACHE_REPLICA_ENGINE_CPU_UTILIZATION = "ELASTICACHE_REPLICA_ENGINE_CPU_UTILIZATION"
    '''(experimental) ELASTIC_CACHE_REPLICA_ENGINE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''
    ELASTICACHE_DATABASE_MEMORY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE = "ELASTICACHE_DATABASE_MEMORY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE"
    '''(experimental) ELASTIC_CACHE_REPLICA_ENGINE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: experimental
    '''


@jsii.implements(IScalableTarget)
class ScalableTarget(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.ScalableTarget",
):
    '''(experimental) Define a scalable target.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as lambda_
        
        # code is of type Code
        
        
        handler = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="index.handler",
            code=code,
        
            reserved_concurrent_executions=2
        )
        
        fn_ver = handler.add_version("CDKLambdaVersion", undefined, "demo alias", 10)
        
        target = appscaling.ScalableTarget(self, "ScalableTarget",
            service_namespace=appscaling.ServiceNamespace.LAMBDA,
            max_capacity=100,
            min_capacity=10,
            resource_id=f"function:{handler.functionName}:{fnVer.version}",
            scalable_dimension="lambda:function:ProvisionedConcurrency"
        )
        
        target.scale_to_track_metric("PceTracking",
            target_value=0.9,
            predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: "ServiceNamespace",
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param max_capacity: (experimental) The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param min_capacity: (experimental) The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param resource_id: (experimental) The resource identifier to associate with this scalable target. This string consists of the resource type and unique identifier. Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH``
        :param scalable_dimension: (experimental) The scalable dimension that's associated with the scalable target. Specify the service namespace, resource type, and scaling property. Example value: ``ecs:service:DesiredCount``
        :param service_namespace: (experimental) The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service. For valid AWS service namespace values, see the RegisterScalableTarget action in the Application Auto Scaling API Reference.
        :param role: (experimental) Role that allows Application Auto Scaling to modify your scalable target. Default: A role is automatically created

        :stability: experimental
        '''
        props = ScalableTargetProps(
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromScalableTargetId") # type: ignore[misc]
    @builtins.classmethod
    def from_scalable_target_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        scalable_target_id: builtins.str,
    ) -> IScalableTarget:
        '''
        :param scope: -
        :param id: -
        :param scalable_target_id: -

        :stability: experimental
        '''
        return typing.cast(IScalableTarget, jsii.sinvoke(cls, "fromScalableTargetId", [scope, id, scalable_target_id]))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_296fe8a3) -> None:
        '''(experimental) Add a policy statement to the role's policy.

        :param statement: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @jsii.member(jsii_name="scaleOnMetric")
    def scale_on_metric(
        self,
        id: builtins.str,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.Sequence["ScalingInterval"],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> "StepScalingPolicy":
        '''(experimental) Scale out or in, in response to a metric.

        :param id: -
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: (experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: ``evaluationPeriods``
        :param evaluation_periods: (experimental) How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: (experimental) Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        '''
        props = BasicStepScalingPolicyProps(
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluation_periods=evaluation_periods,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        return typing.cast("StepScalingPolicy", jsii.invoke(self, "scaleOnMetric", [id, props]))

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''(experimental) Scale out or in based on time.

        :param id: -
        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        '''
        action = ScalingSchedule(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "scaleOnSchedule", [id, action]))

    @jsii.member(jsii_name="scaleToTrackMetric")
    def scale_to_track_metric(
        self,
        id: builtins.str,
        *,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> "TargetTrackingScalingPolicy":
        '''(experimental) Scale out or in in order to keep a metric around a target value.

        :param id: -
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        '''
        props = BasicTargetTrackingScalingPolicyProps(
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast("TargetTrackingScalingPolicy", jsii.invoke(self, "scaleToTrackMetric", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_59af6f50:
        '''(experimental) The role used to give AutoScaling permissions to your resource.

        :stability: experimental
        '''
        return typing.cast(_IRole_59af6f50, jsii.get(self, "role"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        '''(experimental) ID of the Scalable Target.

        Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH|ecs:service:DesiredCount|ecs``

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalableTargetId"))


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.ScalableTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "role": "role",
    },
)
class ScalableTargetProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: "ServiceNamespace",
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        '''(experimental) Properties for a scalable target.

        :param max_capacity: (experimental) The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param min_capacity: (experimental) The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param resource_id: (experimental) The resource identifier to associate with this scalable target. This string consists of the resource type and unique identifier. Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH``
        :param scalable_dimension: (experimental) The scalable dimension that's associated with the scalable target. Specify the service namespace, resource type, and scaling property. Example value: ``ecs:service:DesiredCount``
        :param service_namespace: (experimental) The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service. For valid AWS service namespace values, see the RegisterScalableTarget action in the Application Auto Scaling API Reference.
        :param role: (experimental) Role that allows Application Auto Scaling to modify your scalable target. Default: A role is automatically created

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import monocdk as lambda_
            
            # code is of type Code
            
            
            handler = lambda_.Function(self, "MyFunction",
                runtime=lambda_.Runtime.PYTHON_3_7,
                handler="index.handler",
                code=code,
            
                reserved_concurrent_executions=2
            )
            
            fn_ver = handler.add_version("CDKLambdaVersion", undefined, "demo alias", 10)
            
            target = appscaling.ScalableTarget(self, "ScalableTarget",
                service_namespace=appscaling.ServiceNamespace.LAMBDA,
                max_capacity=100,
                min_capacity=10,
                resource_id=f"function:{handler.functionName}:{fnVer.version}",
                scalable_dimension="lambda:function:ProvisionedConcurrency"
            )
            
            target.scale_to_track_metric("PceTracking",
                target_value=0.9,
                predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''(experimental) The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.

        :stability: experimental
        '''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''(experimental) The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.

        :stability: experimental
        '''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''(experimental) The resource identifier to associate with this scalable target.

        This string consists of the resource type and unique identifier.

        Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH``

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html
        :stability: experimental
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''(experimental) The scalable dimension that's associated with the scalable target.

        Specify the service namespace, resource type, and scaling property.

        Example value: ``ecs:service:DesiredCount``

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingPolicy.html
        :stability: experimental
        '''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> "ServiceNamespace":
        '''(experimental) The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service.

        For valid AWS service namespace values, see the RegisterScalableTarget
        action in the Application Auto Scaling API Reference.

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html
        :stability: experimental
        '''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast("ServiceNamespace", result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        '''(experimental) Role that allows Application Auto Scaling to modify your scalable target.

        :default: A role is automatically created

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_59af6f50], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalableTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.ScalingInterval",
    jsii_struct_bases=[],
    name_mapping={"change": "change", "lower": "lower", "upper": "upper"},
)
class ScalingInterval:
    def __init__(
        self,
        *,
        change: jsii.Number,
        lower: typing.Optional[jsii.Number] = None,
        upper: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) A range of metric values in which to apply a certain scaling operation.

        :param change: (experimental) The capacity adjustment to apply in this interval. The number is interpreted differently based on AdjustmentType: - ChangeInCapacity: add the adjustment to the current capacity. The number can be positive or negative. - PercentChangeInCapacity: add or remove the given percentage of the current capacity to itself. The number can be in the range [-100..100]. - ExactCapacity: set the capacity to this number. The number must be positive.
        :param lower: (experimental) The lower bound of the interval. The scaling adjustment will be applied if the metric is higher than this value. Default: Threshold automatically derived from neighbouring intervals
        :param upper: (experimental) The upper bound of the interval. The scaling adjustment will be applied if the metric is lower than this value. Default: Threshold automatically derived from neighbouring intervals

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            
            scaling_interval = applicationautoscaling.ScalingInterval(
                change=123,
            
                # the properties below are optional
                lower=123,
                upper=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "change": change,
        }
        if lower is not None:
            self._values["lower"] = lower
        if upper is not None:
            self._values["upper"] = upper

    @builtins.property
    def change(self) -> jsii.Number:
        '''(experimental) The capacity adjustment to apply in this interval.

        The number is interpreted differently based on AdjustmentType:

        - ChangeInCapacity: add the adjustment to the current capacity.
          The number can be positive or negative.
        - PercentChangeInCapacity: add or remove the given percentage of the current
          capacity to itself. The number can be in the range [-100..100].
        - ExactCapacity: set the capacity to this number. The number must
          be positive.

        :stability: experimental
        '''
        result = self._values.get("change")
        assert result is not None, "Required property 'change' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lower(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The lower bound of the interval.

        The scaling adjustment will be applied if the metric is higher than this value.

        :default: Threshold automatically derived from neighbouring intervals

        :stability: experimental
        '''
        result = self._values.get("lower")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upper(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The upper bound of the interval.

        The scaling adjustment will be applied if the metric is lower than this value.

        :default: Threshold automatically derived from neighbouring intervals

        :stability: experimental
        '''
        result = self._values.get("upper")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.ScalingSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "schedule": "schedule",
        "end_time": "endTime",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "start_time": "startTime",
    },
)
class ScalingSchedule:
    def __init__(
        self,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''(experimental) A scheduled scaling action.

        :param schedule: (experimental) When to perform this action.
        :param end_time: (experimental) When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: (experimental) The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: (experimental) The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: (experimental) When this scheduled action becomes active. Default: The rule is activate immediately

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # resource is of type SomeScalableResource
            
            
            capacity = resource.auto_scale_capacity(
                min_capacity=1,
                max_capacity=50
            )
            
            capacity.scale_on_schedule("PrescaleInTheMorning",
                schedule=appscaling.Schedule.cron(hour="8", minute="0"),
                min_capacity=20
            )
            
            capacity.scale_on_schedule("AllowDownscalingAtNight",
                schedule=appscaling.Schedule.cron(hour="20", minute="0"),
                min_capacity=1
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "schedule": schedule,
        }
        if end_time is not None:
            self._values["end_time"] = end_time
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def schedule(self) -> "Schedule":
        '''(experimental) When to perform this action.

        :stability: experimental
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("Schedule", result)

    @builtins.property
    def end_time(self) -> typing.Optional[datetime.datetime]:
        '''(experimental) When this scheduled action expires.

        :default: The rule never expires.

        :stability: experimental
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The new maximum capacity.

        During the scheduled time, the current capacity is above the maximum
        capacity, Application Auto Scaling scales in to the maximum capacity.

        At least one of maxCapacity and minCapacity must be supplied.

        :default: No new maximum capacity

        :stability: experimental
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The new minimum capacity.

        During the scheduled time, if the current capacity is below the minimum
        capacity, Application Auto Scaling scales out to the minimum capacity.

        At least one of maxCapacity and minCapacity must be supplied.

        :default: No new minimum capacity

        :stability: experimental
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[datetime.datetime]:
        '''(experimental) When this scheduled action becomes active.

        :default: The rule is activate immediately

        :stability: experimental
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Schedule(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_applicationautoscaling.Schedule",
):
    '''(experimental) Schedule for scheduled scaling actions.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as autoscaling
        
        # fn is of type Function
        
        alias = lambda_.Alias(self, "Alias",
            alias_name="prod",
            version=fn.latest_version
        )
        
        # Create AutoScaling target
        as = alias.add_auto_scaling(max_capacity=50)
        
        # Configure Target Tracking
        as.scale_on_utilization(
            utilization_target=0.5
        )
        
        # Configure Scheduled Scaling
        as.scale_on_schedule("ScaleUpInTheMorning",
            schedule=autoscaling.Schedule.cron(hour="8", minute="0"),
            min_capacity=20
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="at") # type: ignore[misc]
    @builtins.classmethod
    def at(cls, moment: datetime.datetime) -> "Schedule":
        '''(experimental) Construct a Schedule from a moment in time.

        :param moment: -

        :stability: experimental
        '''
        return typing.cast("Schedule", jsii.sinvoke(cls, "at", [moment]))

    @jsii.member(jsii_name="cron") # type: ignore[misc]
    @builtins.classmethod
    def cron(
        cls,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> "Schedule":
        '''(experimental) Create a schedule from a set of cron fields.

        :param day: (experimental) The day of the month to run this rule at. Default: - Every day of the month
        :param hour: (experimental) The hour to run this rule at. Default: - Every hour
        :param minute: (experimental) The minute to run this rule at. Default: - Every minute
        :param month: (experimental) The month to run this rule at. Default: - Every month
        :param week_day: (experimental) The day of the week to run this rule at. Default: - Any day of the week
        :param year: (experimental) The year to run this rule at. Default: - Every year

        :stability: experimental
        '''
        options = CronOptions(
            day=day,
            hour=hour,
            minute=minute,
            month=month,
            week_day=week_day,
            year=year,
        )

        return typing.cast("Schedule", jsii.sinvoke(cls, "cron", [options]))

    @jsii.member(jsii_name="expression") # type: ignore[misc]
    @builtins.classmethod
    def expression(cls, expression: builtins.str) -> "Schedule":
        '''(experimental) Construct a schedule from a literal schedule expression.

        :param expression: The expression to use. Must be in a format that Application AutoScaling will recognize

        :stability: experimental
        '''
        return typing.cast("Schedule", jsii.sinvoke(cls, "expression", [expression]))

    @jsii.member(jsii_name="rate") # type: ignore[misc]
    @builtins.classmethod
    def rate(cls, duration: _Duration_070aa057) -> "Schedule":
        '''(experimental) Construct a schedule from an interval and a time unit.

        :param duration: -

        :stability: experimental
        '''
        return typing.cast("Schedule", jsii.sinvoke(cls, "rate", [duration]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> builtins.str:
        '''(experimental) Retrieve the expression for this schedule.

        :stability: experimental
        '''
        ...


class _ScheduleProxy(Schedule):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> builtins.str:
        '''(experimental) Retrieve the expression for this schedule.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "expressionString"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Schedule).__jsii_proxy_class__ = lambda : _ScheduleProxy


@jsii.enum(jsii_type="monocdk.aws_applicationautoscaling.ServiceNamespace")
class ServiceNamespace(enum.Enum):
    '''(experimental) The service that supports Application AutoScaling.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as lambda_
        
        # code is of type Code
        
        
        handler = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="index.handler",
            code=code,
        
            reserved_concurrent_executions=2
        )
        
        fn_ver = handler.add_version("CDKLambdaVersion", undefined, "demo alias", 10)
        
        target = appscaling.ScalableTarget(self, "ScalableTarget",
            service_namespace=appscaling.ServiceNamespace.LAMBDA,
            max_capacity=100,
            min_capacity=10,
            resource_id=f"function:{handler.functionName}:{fnVer.version}",
            scalable_dimension="lambda:function:ProvisionedConcurrency"
        )
        
        target.scale_to_track_metric("PceTracking",
            target_value=0.9,
            predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
        )
    '''

    ECS = "ECS"
    '''(experimental) Elastic Container Service.

    :stability: experimental
    '''
    ELASTIC_MAP_REDUCE = "ELASTIC_MAP_REDUCE"
    '''(experimental) Elastic Map Reduce.

    :stability: experimental
    '''
    EC2 = "EC2"
    '''(experimental) Elastic Compute Cloud.

    :stability: experimental
    '''
    APPSTREAM = "APPSTREAM"
    '''(experimental) App Stream.

    :stability: experimental
    '''
    DYNAMODB = "DYNAMODB"
    '''(experimental) Dynamo DB.

    :stability: experimental
    '''
    RDS = "RDS"
    '''(experimental) Relational Database Service.

    :stability: experimental
    '''
    SAGEMAKER = "SAGEMAKER"
    '''(experimental) SageMaker.

    :stability: experimental
    '''
    CUSTOM_RESOURCE = "CUSTOM_RESOURCE"
    '''(experimental) Custom Resource.

    :stability: experimental
    '''
    LAMBDA = "LAMBDA"
    '''(experimental) Lambda.

    :stability: experimental
    '''
    COMPREHEND = "COMPREHEND"
    '''(experimental) Comprehend.

    :stability: experimental
    '''
    KAFKA = "KAFKA"
    '''(experimental) Kafka.

    :stability: experimental
    '''
    ELASTICACHE = "ELASTICACHE"
    '''(experimental) ElastiCache.

    :stability: experimental
    '''


class StepScalingAction(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingAction",
):
    '''(experimental) Define a step scaling action.

    This kind of scaling policy adjusts the target capacity in configurable
    steps. The size of the step is configurable based on the metric's distance
    to its alarm threshold.

    This Action must be used as the target of a CloudWatch alarm to take effect.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import monocdk as monocdk
        from monocdk import aws_applicationautoscaling as applicationautoscaling
        
        # duration is of type Duration
        # scalable_target is of type ScalableTarget
        
        step_scaling_action = applicationautoscaling.StepScalingAction(self, "MyStepScalingAction",
            scaling_target=scalable_target,
        
            # the properties below are optional
            adjustment_type=applicationautoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
            cooldown=duration,
            metric_aggregation_type=applicationautoscaling.MetricAggregationType.AVERAGE,
            min_adjustment_magnitude=123,
            policy_name="policyName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param scaling_target: (experimental) The scalable target.
        :param adjustment_type: (experimental) How the adjustment numbers are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. For scale out policies, multiple scale outs during the cooldown period are squashed so that only the biggest scale out happens. For scale in policies, subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param metric_aggregation_type: (experimental) The aggregation type for the CloudWatch metrics. Default: Average
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param policy_name: (experimental) A name for the scaling policy. Default: Automatically generated name

        :stability: experimental
        '''
        props = StepScalingActionProps(
            scaling_target=scaling_target,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            policy_name=policy_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addAdjustment")
    def add_adjustment(
        self,
        *,
        adjustment: jsii.Number,
        lower_bound: typing.Optional[jsii.Number] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Add an adjusment interval to the ScalingAction.

        :param adjustment: (experimental) What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
        :param lower_bound: (experimental) Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        :param upper_bound: (experimental) Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity

        :stability: experimental
        '''
        adjustment_ = AdjustmentTier(
            adjustment=adjustment, lower_bound=lower_bound, upper_bound=upper_bound
        )

        return typing.cast(None, jsii.invoke(self, "addAdjustment", [adjustment_]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> builtins.str:
        '''(experimental) ARN of the scaling policy.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalingPolicyArn"))


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_target": "scalingTarget",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "policy_name": "policyName",
    },
)
class StepScalingActionProps:
    def __init__(
        self,
        *,
        scaling_target: IScalableTarget,
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for a scaling policy.

        :param scaling_target: (experimental) The scalable target.
        :param adjustment_type: (experimental) How the adjustment numbers are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. For scale out policies, multiple scale outs during the cooldown period are squashed so that only the biggest scale out happens. For scale in policies, subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param metric_aggregation_type: (experimental) The aggregation type for the CloudWatch metrics. Default: Average
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param policy_name: (experimental) A name for the scaling policy. Default: Automatically generated name

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            
            # duration is of type Duration
            # scalable_target is of type ScalableTarget
            
            step_scaling_action_props = applicationautoscaling.StepScalingActionProps(
                scaling_target=scalable_target,
            
                # the properties below are optional
                adjustment_type=applicationautoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
                cooldown=duration,
                metric_aggregation_type=applicationautoscaling.MetricAggregationType.AVERAGE,
                min_adjustment_magnitude=123,
                policy_name="policyName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "scaling_target": scaling_target,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        '''(experimental) The scalable target.

        :stability: experimental
        '''
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return typing.cast(IScalableTarget, result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        '''(experimental) How the adjustment numbers are interpreted.

        :default: ChangeInCapacity

        :stability: experimental
        '''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[AdjustmentType], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Grace period after scaling activity.

        For scale out policies, multiple scale outs during the cooldown period are
        squashed so that only the biggest scale out happens.

        For scale in policies, subsequent scale ins during the cooldown period are
        ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        :stability: experimental
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[MetricAggregationType]:
        '''(experimental) The aggregation type for the CloudWatch metrics.

        :default: Average

        :stability: experimental
        '''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[MetricAggregationType], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect

        :stability: experimental
        '''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the scaling policy.

        :default: Automatically generated name

        :stability: experimental
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepScalingActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StepScalingPolicy(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingPolicy",
):
    '''(experimental) Define a scaling strategy which scales depending on absolute values of some metric.

    You can specify the scaling behavior for various values of the metric.

    Implemented using one or more CloudWatch alarms and Step Scaling Policies.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import monocdk as monocdk
        from monocdk import aws_applicationautoscaling as applicationautoscaling
        from monocdk import aws_cloudwatch as cloudwatch
        
        # duration is of type Duration
        # metric is of type Metric
        # scalable_target is of type ScalableTarget
        
        step_scaling_policy = applicationautoscaling.StepScalingPolicy(self, "MyStepScalingPolicy",
            metric=metric,
            scaling_steps=[applicationautoscaling.ScalingInterval(
                change=123,
        
                # the properties below are optional
                lower=123,
                upper=123
            )],
            scaling_target=scalable_target,
        
            # the properties below are optional
            adjustment_type=applicationautoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
            cooldown=duration,
            datapoints_to_alarm=123,
            evaluation_periods=123,
            metric_aggregation_type=applicationautoscaling.MetricAggregationType.AVERAGE,
            min_adjustment_magnitude=123
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.Sequence[ScalingInterval],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param scaling_target: (experimental) The scaling target.
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: (experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: ``evaluationPeriods``
        :param evaluation_periods: (experimental) How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: (experimental) Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :stability: experimental
        '''
        props = StepScalingPolicyProps(
            scaling_target=scaling_target,
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluation_periods=evaluation_periods,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lowerAction")
    def lower_action(self) -> typing.Optional[StepScalingAction]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[StepScalingAction], jsii.get(self, "lowerAction"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lowerAlarm")
    def lower_alarm(self) -> typing.Optional[_Alarm_a55fe34b]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[_Alarm_a55fe34b], jsii.get(self, "lowerAlarm"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="upperAction")
    def upper_action(self) -> typing.Optional[StepScalingAction]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[StepScalingAction], jsii.get(self, "upperAction"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="upperAlarm")
    def upper_alarm(self) -> typing.Optional[_Alarm_a55fe34b]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[_Alarm_a55fe34b], jsii.get(self, "upperAlarm"))


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.StepScalingPolicyProps",
    jsii_struct_bases=[BasicStepScalingPolicyProps],
    name_mapping={
        "metric": "metric",
        "scaling_steps": "scalingSteps",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluation_periods": "evaluationPeriods",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "scaling_target": "scalingTarget",
    },
)
class StepScalingPolicyProps(BasicStepScalingPolicyProps):
    def __init__(
        self,
        *,
        metric: _IMetric_5db43d61,
        scaling_steps: typing.Sequence[ScalingInterval],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_070aa057] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        scaling_target: IScalableTarget,
    ) -> None:
        '''
        :param metric: (experimental) Metric to scale on.
        :param scaling_steps: (experimental) The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
        :param adjustment_type: (experimental) How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: (experimental) Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: (experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: ``evaluationPeriods``
        :param evaluation_periods: (experimental) How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: (experimental) Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: (experimental) Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param scaling_target: (experimental) The scaling target.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            from monocdk import aws_cloudwatch as cloudwatch
            
            # duration is of type Duration
            # metric is of type Metric
            # scalable_target is of type ScalableTarget
            
            step_scaling_policy_props = applicationautoscaling.StepScalingPolicyProps(
                metric=metric,
                scaling_steps=[applicationautoscaling.ScalingInterval(
                    change=123,
            
                    # the properties below are optional
                    lower=123,
                    upper=123
                )],
                scaling_target=scalable_target,
            
                # the properties below are optional
                adjustment_type=applicationautoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
                cooldown=duration,
                datapoints_to_alarm=123,
                evaluation_periods=123,
                metric_aggregation_type=applicationautoscaling.MetricAggregationType.AVERAGE,
                min_adjustment_magnitude=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
            "scaling_steps": scaling_steps,
            "scaling_target": scaling_target,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude

    @builtins.property
    def metric(self) -> _IMetric_5db43d61:
        '''(experimental) Metric to scale on.

        :stability: experimental
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(_IMetric_5db43d61, result)

    @builtins.property
    def scaling_steps(self) -> typing.List[ScalingInterval]:
        '''(experimental) The intervals for scaling.

        Maps a range of metric values to a particular scaling behavior.

        :stability: experimental
        '''
        result = self._values.get("scaling_steps")
        assert result is not None, "Required property 'scaling_steps' is missing"
        return typing.cast(typing.List[ScalingInterval], result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        '''(experimental) How the adjustment numbers inside 'intervals' are interpreted.

        :default: ChangeInCapacity

        :stability: experimental
        '''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[AdjustmentType], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Grace period after scaling activity.

        Subsequent scale outs during the cooldown period are squashed so that only
        the biggest scale out happens.

        Subsequent scale ins during the cooldown period are ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        :stability: experimental
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of data points out of the evaluation periods that must be breaching to trigger a scaling action.

        Creates an "M out of N" alarm, where this property is the M and the value set for
        ``evaluationPeriods`` is the N value.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: ``evaluationPeriods``

        :stability: experimental
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''(experimental) How many evaluation periods of the metric to wait before triggering a scaling action.

        Raising this value can be used to smooth out the metric, at the expense
        of slower response times.

        If ``datapointsToAlarm`` is not set, then all data points in the evaluation period
        must meet the criteria to trigger a scaling action.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[MetricAggregationType]:
        '''(experimental) Aggregation to apply to all data points over the evaluation periods.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.

        :stability: experimental
        '''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[MetricAggregationType], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect

        :stability: experimental
        '''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        '''(experimental) The scaling target.

        :stability: experimental
        '''
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return typing.cast(IScalableTarget, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TargetTrackingScalingPolicy(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_applicationautoscaling.TargetTrackingScalingPolicy",
):
    '''
    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import monocdk as monocdk
        from monocdk import aws_applicationautoscaling as applicationautoscaling
        from monocdk import aws_cloudwatch as cloudwatch
        
        # duration is of type Duration
        # metric is of type Metric
        # scalable_target is of type ScalableTarget
        
        target_tracking_scaling_policy = applicationautoscaling.TargetTrackingScalingPolicy(self, "MyTargetTrackingScalingPolicy",
            scaling_target=scalable_target,
            target_value=123,
        
            # the properties below are optional
            custom_metric=metric,
            disable_scale_in=False,
            policy_name="policyName",
            predefined_metric=applicationautoscaling.PredefinedMetric.DYNAMODB_READ_CAPACITY_UTILIZATION,
            resource_label="resourceLabel",
            scale_in_cooldown=duration,
            scale_out_cooldown=duration
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param scaling_target: 
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        '''
        props = TargetTrackingScalingPolicyProps(
            scaling_target=scaling_target,
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> builtins.str:
        '''(experimental) ARN of the scaling policy.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalingPolicyArn"))


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.TargetTrackingScalingPolicyProps",
    jsii_struct_bases=[BasicTargetTrackingScalingPolicyProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_value": "targetValue",
        "custom_metric": "customMetric",
        "predefined_metric": "predefinedMetric",
        "resource_label": "resourceLabel",
        "scaling_target": "scalingTarget",
    },
)
class TargetTrackingScalingPolicyProps(BasicTargetTrackingScalingPolicyProps):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_070aa057] = None,
        scale_out_cooldown: typing.Optional[_Duration_070aa057] = None,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_5db43d61] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        scaling_target: IScalableTarget,
    ) -> None:
        '''(experimental) Properties for a concrete TargetTrackingPolicy.

        Adds the scalingTarget.

        :param disable_scale_in: (experimental) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: (experimental) A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: (experimental) Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: (experimental) Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_value: (experimental) The target value for the metric.
        :param custom_metric: (experimental) A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: (experimental) A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: (experimental) Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param scaling_target: 

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            from monocdk import aws_cloudwatch as cloudwatch
            
            # duration is of type Duration
            # metric is of type Metric
            # scalable_target is of type ScalableTarget
            
            target_tracking_scaling_policy_props = applicationautoscaling.TargetTrackingScalingPolicyProps(
                scaling_target=scalable_target,
                target_value=123,
            
                # the properties below are optional
                custom_metric=metric,
                disable_scale_in=False,
                policy_name="policyName",
                predefined_metric=applicationautoscaling.PredefinedMetric.DYNAMODB_READ_CAPACITY_UTILIZATION,
                resource_label="resourceLabel",
                scale_in_cooldown=duration,
                scale_out_cooldown=duration
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
            "scaling_target": scaling_target,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if predefined_metric is not None:
            self._values["predefined_metric"] = predefined_metric
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the scaling policy.

        :default: - Automatically generated name.

        :stability: experimental
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency

        :stability: experimental
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''(experimental) The target value for the metric.

        :stability: experimental
        '''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def custom_metric(self) -> typing.Optional[_IMetric_5db43d61]:
        '''(experimental) A custom metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No custom metric.

        :stability: experimental
        '''
        result = self._values.get("custom_metric")
        return typing.cast(typing.Optional[_IMetric_5db43d61], result)

    @builtins.property
    def predefined_metric(self) -> typing.Optional[PredefinedMetric]:
        '''(experimental) A predefined metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No predefined metrics.

        :stability: experimental
        '''
        result = self._values.get("predefined_metric")
        return typing.cast(typing.Optional[PredefinedMetric], result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Identify the resource associated with the metric type.

        Only used for predefined metric ALBRequestCountPerTarget.

        Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>``

        :default: - No resource label.

        :stability: experimental
        '''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        '''
        :stability: experimental
        '''
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return typing.cast(IScalableTarget, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetTrackingScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_applicationautoscaling.BaseScalableAttributeProps",
    jsii_struct_bases=[EnableScalingProps],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "dimension": "dimension",
        "resource_id": "resourceId",
        "role": "role",
        "service_namespace": "serviceNamespace",
    },
)
class BaseScalableAttributeProps(EnableScalingProps):
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: _IRole_59af6f50,
        service_namespace: ServiceNamespace,
    ) -> None:
        '''(experimental) Properties for a ScalableTableAttribute.

        :param max_capacity: (experimental) Maximum capacity to scale to.
        :param min_capacity: (experimental) Minimum capacity to scale to. Default: 1
        :param dimension: (experimental) Scalable dimension of the attribute.
        :param resource_id: (experimental) Resource ID of the attribute.
        :param role: (experimental) Role to use for scaling.
        :param service_namespace: (experimental) Service namespace of the scalable attribute.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_applicationautoscaling as applicationautoscaling
            from monocdk import aws_iam as iam
            
            # role is of type Role
            
            base_scalable_attribute_props = applicationautoscaling.BaseScalableAttributeProps(
                dimension="dimension",
                max_capacity=123,
                resource_id="resourceId",
                role=role,
                service_namespace=applicationautoscaling.ServiceNamespace.ECS,
            
                # the properties below are optional
                min_capacity=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "dimension": dimension,
            "resource_id": resource_id,
            "role": role,
            "service_namespace": service_namespace,
        }
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''(experimental) Maximum capacity to scale to.

        :stability: experimental
        '''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Minimum capacity to scale to.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimension(self) -> builtins.str:
        '''(experimental) Scalable dimension of the attribute.

        :stability: experimental
        '''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''(experimental) Resource ID of the attribute.

        :stability: experimental
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> _IRole_59af6f50:
        '''(experimental) Role to use for scaling.

        :stability: experimental
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_59af6f50, result)

    @builtins.property
    def service_namespace(self) -> ServiceNamespace:
        '''(experimental) Service namespace of the scalable attribute.

        :stability: experimental
        '''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(ServiceNamespace, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseScalableAttributeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AdjustmentTier",
    "AdjustmentType",
    "BaseScalableAttribute",
    "BaseScalableAttributeProps",
    "BaseTargetTrackingProps",
    "BasicStepScalingPolicyProps",
    "BasicTargetTrackingScalingPolicyProps",
    "CfnScalableTarget",
    "CfnScalableTargetProps",
    "CfnScalingPolicy",
    "CfnScalingPolicyProps",
    "CronOptions",
    "EnableScalingProps",
    "IScalableTarget",
    "MetricAggregationType",
    "PredefinedMetric",
    "ScalableTarget",
    "ScalableTargetProps",
    "ScalingInterval",
    "ScalingSchedule",
    "Schedule",
    "ServiceNamespace",
    "StepScalingAction",
    "StepScalingActionProps",
    "StepScalingPolicy",
    "StepScalingPolicyProps",
    "TargetTrackingScalingPolicy",
    "TargetTrackingScalingPolicyProps",
]

publication.publish()
