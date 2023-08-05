'''
# Amazon CloudWatch Construct Library

## Metric objects

Metric objects represent a metric that is emitted by AWS services or your own
application, such as `CPUUsage`, `FailureCount` or `Bandwidth`.

Metric objects can be constructed directly or are exposed by resources as
attributes. Resources that expose metrics will have functions that look
like `metricXxx()` which will return a Metric object, initialized with defaults
that make sense.

For example, `lambda.Function` objects have the `fn.metricErrors()` method, which
represents the amount of errors reported by that Lambda function:

```python
# fn is of type Function


errors = fn.metric_errors()
```

`Metric` objects can be account and region aware. You can specify `account` and `region` as properties of the metric, or use the `metric.attachTo(Construct)` method. `metric.attachTo()` will automatically copy the `region` and `account` fields of the `Construct`, which can come from anywhere in the Construct tree.

You can also instantiate `Metric` objects to reference any
[published metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html)
that's not exposed using a convenience method on the CDK construct.
For example:

```python
hosted_zone = route53.HostedZone(self, "MyHostedZone", zone_name="example.org")
metric = cloudwatch.Metric(
    namespace="AWS/Route53",
    metric_name="DNSQueries",
    dimensions_map={
        "HostedZoneId": hosted_zone.hosted_zone_id
    }
)
```

### Instantiating a new Metric object

If you want to reference a metric that is not yet exposed by an existing construct,
you can instantiate a `Metric` object to represent it. For example:

```python
metric = cloudwatch.Metric(
    namespace="MyNamespace",
    metric_name="MyMetric",
    dimensions_map={
        "ProcessingStep": "Download"
    }
)
```

### Metric Math

Math expressions are supported by instantiating the `MathExpression` class.
For example, a math expression that sums two other metrics looks like this:

```python
# fn is of type Function


all_problems = cloudwatch.MathExpression(
    expression="errors + throttles",
    using_metrics={
        "errors": fn.metric_errors(),
        "faults": fn.metric_throttles()
    }
)
```

You can use `MathExpression` objects like any other metric, including using
them in other math expressions:

```python
# fn is of type Function
# all_problems is of type MathExpression


problem_percentage = cloudwatch.MathExpression(
    expression="(problems / invocations) * 100",
    using_metrics={
        "problems": all_problems,
        "invocations": fn.metric_invocations()
    }
)
```

### Search Expressions

Math expressions also support search expressions. For example, the following
search expression returns all CPUUtilization metrics that it finds, with the
graph showing the Average statistic with an aggregation period of 5 minutes:

```python
cpu_utilization = cloudwatch.MathExpression(
    expression="SEARCH('{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\"', 'Average', 300)"
)
```

Cross-account and cross-region search expressions are also supported. Use
the `searchAccount` and `searchRegion` properties to specify the account
and/or region to evaluate the search expression against.

### Aggregation

To graph or alarm on metrics you must aggregate them first, using a function
like `Average` or a percentile function like `P99`. By default, most Metric objects
returned by CDK libraries will be configured as `Average` over `300 seconds` (5 minutes).
The exception is if the metric represents a count of discrete events, such as
failures. In that case, the Metric object will be configured as `Sum` over `300 seconds`, i.e. it represents the number of times that event occurred over the
time period.

If you want to change the default aggregation of the Metric object (for example,
the function or the period), you can do so by passing additional parameters
to the metric function call:

```python
# fn is of type Function


minute_error_rate = fn.metric_errors(
    statistic="avg",
    period=Duration.minutes(1),
    label="Lambda failure rate"
)
```

This function also allows changing the metric label or color (which will be
useful when embedding them in graphs, see below).

> Rates versus Sums
>
> The reason for using `Sum` to count discrete events is that *some* events are
> emitted as either `0` or `1` (for example `Errors` for a Lambda) and some are
> only emitted as `1` (for example `NumberOfMessagesPublished` for an SNS
> topic).
>
> In case `0`-metrics are emitted, it makes sense to take the `Average` of this
> metric: the result will be the fraction of errors over all executions.
>
> If `0`-metrics are not emitted, the `Average` will always be equal to `1`,
> and not be very useful.
>
> In order to simplify the mental model of `Metric` objects, we default to
> aggregating using `Sum`, which will be the same for both metrics types. If you
> happen to know the Metric you want to alarm on makes sense as a rate
> (`Average`) you can always choose to change the statistic.

## Alarms

Alarms can be created on metrics in one of two ways. Either create an `Alarm`
object, passing the `Metric` object to set the alarm on:

```python
# fn is of type Function


cloudwatch.Alarm(self, "Alarm",
    metric=fn.metric_errors(),
    threshold=100,
    evaluation_periods=2
)
```

Alternatively, you can call `metric.createAlarm()`:

```python
# fn is of type Function


fn.metric_errors().create_alarm(self, "Alarm",
    threshold=100,
    evaluation_periods=2
)
```

The most important properties to set while creating an Alarms are:

* `threshold`: the value to compare the metric against.
* `comparisonOperator`: the comparison operation to use, defaults to `metric >= threshold`.
* `evaluationPeriods`: how many consecutive periods the metric has to be
  breaching the the threshold for the alarm to trigger.

To create a cross-account alarm, make sure you have enabled [cross-account functionality](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html) in CloudWatch. Then, set the `account` property in the `Metric` object either manually or via the `metric.attachTo()` method.

### Alarm Actions

To add actions to an alarm, use the integration classes from the
`@aws-cdk/aws-cloudwatch-actions` package. For example, to post a message to
an SNS topic when an alarm breaches, do the following:

```python
import monocdk as cw_actions
# alarm is of type Alarm


topic = sns.Topic(self, "Topic")
alarm.add_alarm_action(cw_actions.SnsAction(topic))
```

#### Notification formats

Alarms can be created in one of two "formats":

* With "top-level parameters" (these are the classic style of CloudWatch Alarms).
* With a list of metrics specifications (these are the modern style of CloudWatch Alarms).

For backwards compatibility, CDK will try to create classic, top-level CloudWatch alarms
as much as possible, unless you are using features that cannot be expressed in that format.
Features that require the new-style alarm format are:

* Metric math
* Cross-account metrics
* Labels

The difference between these two does not impact the functionality of the alarm
in any way, *except* that the format of the notifications the Alarm generates is
different between them. This affects both the notifications sent out over SNS,
as well as the EventBridge events generated by this Alarm. If you are writing
code to consume these notifications, be sure to handle both formats.

### Composite Alarms

[Composite Alarms](https://aws.amazon.com/about-aws/whats-new/2020/03/amazon-cloudwatch-now-allows-you-to-combine-multiple-alarms/)
can be created from existing Alarm resources.

```python
# alarm1 is of type Alarm
# alarm2 is of type Alarm
# alarm3 is of type Alarm
# alarm4 is of type Alarm


alarm_rule = cloudwatch.AlarmRule.any_of(
    cloudwatch.AlarmRule.all_of(
        cloudwatch.AlarmRule.any_of(alarm1,
            cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
        cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
    cloudwatch.AlarmRule.from_boolean(False))

cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
    alarm_rule=alarm_rule
)
```

### A note on units

In CloudWatch, Metrics datums are emitted with units, such as `seconds` or
`bytes`. When `Metric` objects are given a `unit` attribute, it will be used to
*filter* the stream of metric datums for datums emitted using the same `unit`
attribute.

In particular, the `unit` field is *not* used to rescale datums or alarm threshold
values (for example, it cannot be used to specify an alarm threshold in
*Megabytes* if the metric stream is being emitted as *bytes*).

You almost certainly don't want to specify the `unit` property when creating
`Metric` objects (which will retrieve all datums regardless of their unit),
unless you have very specific requirements. Note that in any case, CloudWatch
only supports filtering by `unit` for Alarms, not in Dashboard graphs.

Please see the following GitHub issue for a discussion on real unit
calculations in CDK: https://github.com/aws/aws-cdk/issues/5595

## Dashboards

Dashboards are set of Widgets stored server-side which can be accessed quickly
from the AWS console. Available widgets are graphs of a metric over time, the
current value of a metric, or a static piece of Markdown which explains what the
graphs mean.

The following widgets are available:

* `GraphWidget` -- shows any number of metrics on both the left and right
  vertical axes.
* `AlarmWidget` -- shows the graph and alarm line for a single alarm.
* `SingleValueWidget` -- shows the current value of a set of metrics.
* `TextWidget` -- shows some static Markdown.
* `AlarmStatusWidget` -- shows the status of your alarms in a grid view.

### Graph widget

A graph widget can display any number of metrics on either the `left` or
`right` vertical axis:

```python
# dashboard is of type Dashboard
# execution_count_metric is of type Metric
# error_count_metric is of type Metric


dashboard.add_widgets(cloudwatch.GraphWidget(
    title="Executions vs error rate",

    left=[execution_count_metric],

    right=[error_count_metric.with(
        statistic="average",
        label="Error rate",
        color=cloudwatch.Color.GREEN
    )]
))
```

Using the methods `addLeftMetric()` and `addRightMetric()` you can add metrics to a graph widget later on.

Graph widgets can also display annotations attached to the left or the right y-axis.

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    left_annotations=[cloudwatch.aws_cloudwatch.HorizontalAnnotation(value=1800, label=Duration.minutes(30).to_human_string(), color=cloudwatch.Color.RED), cloudwatch.aws_cloudwatch.HorizontalAnnotation(value=3600, label="1 hour", color="#2ca02c")
    ]
))
```

The graph legend can be adjusted from the default position at bottom of the widget.

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    legend_position=cloudwatch.LegendPosition.RIGHT
))
```

The graph can publish live data within the last minute that has not been fully aggregated.

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    live_data=True
))
```

The graph view can be changed from default 'timeSeries' to 'bar' or 'pie'.

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    view=cloudwatch.GraphWidgetView.BAR
))
```

### Alarm widget

An alarm widget shows the graph and the alarm line of a single alarm:

```python
# dashboard is of type Dashboard
# error_alarm is of type Alarm


dashboard.add_widgets(cloudwatch.AlarmWidget(
    title="Errors",
    alarm=error_alarm
))
```

### Single value widget

A single-value widget shows the latest value of a set of metrics (as opposed
to a graph of the value over time):

```python
# dashboard is of type Dashboard
# visitor_count is of type Metric
# purchase_count is of type Metric


dashboard.add_widgets(cloudwatch.SingleValueWidget(
    metrics=[visitor_count, purchase_count]
))
```

Show as many digits as can fit, before rounding.

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.SingleValueWidget(
    metrics=[],

    full_precision=True
))
```

### Text widget

A text widget shows an arbitrary piece of MarkDown. Use this to add explanations
to your dashboard:

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.TextWidget(
    markdown="# Key Performance Indicators"
))
```

### Alarm Status widget

An alarm status widget displays instantly the status of any type of alarms and gives the
ability to aggregate one or more alarms together in a small surface.

```python
# dashboard is of type Dashboard
# error_alarm is of type Alarm


dashboard.add_widgets(
    cloudwatch.AlarmStatusWidget(
        alarms=[error_alarm]
    ))
```

### Query results widget

A `LogQueryWidget` shows the results of a query from Logs Insights:

```python
# dashboard is of type Dashboard


dashboard.add_widgets(cloudwatch.LogQueryWidget(
    log_group_names=["my-log-group"],
    view=cloudwatch.LogQueryVisualizationType.TABLE,
    # The lines will be automatically combined using '\n|'.
    query_lines=["fields @message", "filter @message like /Error/"
    ]
))
```

### Dashboard Layout

The widgets on a dashboard are visually laid out in a grid that is 24 columns
wide. Normally you specify X and Y coordinates for the widgets on a Dashboard,
but because this is inconvenient to do manually, the library contains a simple
layout system to help you lay out your dashboards the way you want them to.

Widgets have a `width` and `height` property, and they will be automatically
laid out either horizontally or vertically stacked to fill out the available
space.

Widgets are added to a Dashboard by calling `add(widget1, widget2, ...)`.
Widgets given in the same call will be laid out horizontally. Widgets given
in different calls will be laid out vertically. To make more complex layouts,
you can use the following widgets to pack widgets together in different ways:

* `Column`: stack two or more widgets vertically.
* `Row`: lay out two or more widgets horizontally.
* `Spacer`: take up empty space
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
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    Duration as _Duration_070aa057,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    Resource as _Resource_abff4495,
    ResourceProps as _ResourceProps_9b554c0f,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_iam import Grant as _Grant_bcb5eae7, IGrantable as _IGrantable_4c5a91d1


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.AlarmActionConfig",
    jsii_struct_bases=[],
    name_mapping={"alarm_action_arn": "alarmActionArn"},
)
class AlarmActionConfig:
    def __init__(self, *, alarm_action_arn: builtins.str) -> None:
        '''(experimental) Properties for an alarm action.

        :param alarm_action_arn: (experimental) Return the ARN that should be used for a CloudWatch Alarm action.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            alarm_action_config = cloudwatch.AlarmActionConfig(
                alarm_action_arn="alarmActionArn"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alarm_action_arn": alarm_action_arn,
        }

    @builtins.property
    def alarm_action_arn(self) -> builtins.str:
        '''(experimental) Return the ARN that should be used for a CloudWatch Alarm action.

        :stability: experimental
        '''
        result = self._values.get("alarm_action_arn")
        assert result is not None, "Required property 'alarm_action_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlarmRule(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_cloudwatch.AlarmRule"):
    '''(experimental) Class with static functions to build AlarmRule for Composite Alarms.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # alarm1 is of type Alarm
        # alarm2 is of type Alarm
        # alarm3 is of type Alarm
        # alarm4 is of type Alarm
        
        
        alarm_rule = cloudwatch.AlarmRule.any_of(
            cloudwatch.AlarmRule.all_of(
                cloudwatch.AlarmRule.any_of(alarm1,
                    cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
            cloudwatch.AlarmRule.from_boolean(False))
        
        cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
            alarm_rule=alarm_rule
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="allOf") # type: ignore[misc]
    @builtins.classmethod
    def all_of(cls, *operands: "IAlarmRule") -> "IAlarmRule":
        '''(experimental) function to join all provided AlarmRules with AND operator.

        :param operands: IAlarmRules to be joined with AND operator.

        :stability: experimental
        '''
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "allOf", [*operands]))

    @jsii.member(jsii_name="anyOf") # type: ignore[misc]
    @builtins.classmethod
    def any_of(cls, *operands: "IAlarmRule") -> "IAlarmRule":
        '''(experimental) function to join all provided AlarmRules with OR operator.

        :param operands: IAlarmRules to be joined with OR operator.

        :stability: experimental
        '''
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "anyOf", [*operands]))

    @jsii.member(jsii_name="fromAlarm") # type: ignore[misc]
    @builtins.classmethod
    def from_alarm(cls, alarm: "IAlarm", alarm_state: "AlarmState") -> "IAlarmRule":
        '''(experimental) function to build Rule Expression for given IAlarm and AlarmState.

        :param alarm: IAlarm to be used in Rule Expression.
        :param alarm_state: AlarmState to be used in Rule Expression.

        :stability: experimental
        '''
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "fromAlarm", [alarm, alarm_state]))

    @jsii.member(jsii_name="fromBoolean") # type: ignore[misc]
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "IAlarmRule":
        '''(experimental) function to build TRUE/FALSE intent for Rule Expression.

        :param value: boolean value to be used in rule expression.

        :stability: experimental
        '''
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, alarm_rule: builtins.str) -> "IAlarmRule":
        '''(experimental) function to build Rule Expression for given Alarm Rule string.

        :param alarm_rule: string to be used in Rule Expression.

        :stability: experimental
        '''
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "fromString", [alarm_rule]))

    @jsii.member(jsii_name="not") # type: ignore[misc]
    @builtins.classmethod
    def not_(cls, operand: "IAlarmRule") -> "IAlarmRule":
        '''(experimental) function to wrap provided AlarmRule in NOT operator.

        :param operand: IAlarmRule to be wrapped in NOT operator.

        :stability: experimental
        '''
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "not", [operand]))


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.AlarmState")
class AlarmState(enum.Enum):
    '''(experimental) Enumeration indicates state of Alarm used in building Alarm Rule.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # alarm1 is of type Alarm
        # alarm2 is of type Alarm
        # alarm3 is of type Alarm
        # alarm4 is of type Alarm
        
        
        alarm_rule = cloudwatch.AlarmRule.any_of(
            cloudwatch.AlarmRule.all_of(
                cloudwatch.AlarmRule.any_of(alarm1,
                    cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
            cloudwatch.AlarmRule.from_boolean(False))
        
        cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
            alarm_rule=alarm_rule
        )
    '''

    ALARM = "ALARM"
    '''(experimental) State indicates resource is in ALARM.

    :stability: experimental
    '''
    OK = "OK"
    '''(experimental) State indicates resource is not in ALARM.

    :stability: experimental
    '''
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    '''(experimental) State indicates there is not enough data to determine is resource is in ALARM.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.AlarmStatusWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "height": "height",
        "title": "title",
        "width": "width",
    },
)
class AlarmStatusWidgetProps:
    def __init__(
        self,
        *,
        alarms: typing.Sequence["IAlarm"],
        height: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for an Alarm Status Widget.

        :param alarms: (experimental) CloudWatch Alarms to show in widget.
        :param height: (experimental) Height of the widget. Default: 3
        :param title: (experimental) The title of the widget. Default: 'Alarm Status'
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # dashboard is of type Dashboard
            # error_alarm is of type Alarm
            
            
            dashboard.add_widgets(
                cloudwatch.AlarmStatusWidget(
                    alarms=[error_alarm]
                ))
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alarms": alarms,
        }
        if height is not None:
            self._values["height"] = height
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def alarms(self) -> typing.List["IAlarm"]:
        '''(experimental) CloudWatch Alarms to show in widget.

        :stability: experimental
        '''
        result = self._values.get("alarms")
        assert result is not None, "Required property 'alarms' is missing"
        return typing.cast(typing.List["IAlarm"], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default: 3

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''(experimental) The title of the widget.

        :default: 'Alarm Status'

        :stability: experimental
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmStatusWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAlarm(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CfnAlarm",
):
    '''A CloudFormation ``AWS::CloudWatch::Alarm``.

    The ``AWS::CloudWatch::Alarm`` type specifies an alarm and associates it with the specified metric or metric math expression.

    When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA`` . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.

    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

    :cloudformationResource: AWS::CloudWatch::Alarm
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        cfn_alarm = cloudwatch.CfnAlarm(self, "MyCfnAlarm",
            comparison_operator="comparisonOperator",
            evaluation_periods=123,
        
            # the properties below are optional
            actions_enabled=False,
            alarm_actions=["alarmActions"],
            alarm_description="alarmDescription",
            alarm_name="alarmName",
            datapoints_to_alarm=123,
            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                name="name",
                value="value"
            )],
            evaluate_low_sample_count_percentile="evaluateLowSampleCountPercentile",
            extended_statistic="extendedStatistic",
            insufficient_data_actions=["insufficientDataActions"],
            metric_name="metricName",
            metrics=[cloudwatch.CfnAlarm.MetricDataQueryProperty(
                id="id",
        
                # the properties below are optional
                account_id="accountId",
                expression="expression",
                label="label",
                metric_stat=cloudwatch.CfnAlarm.MetricStatProperty(
                    metric=cloudwatch.CfnAlarm.MetricProperty(
                        dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        namespace="namespace"
                    ),
                    period=123,
                    stat="stat",
        
                    # the properties below are optional
                    unit="unit"
                ),
                period=123,
                return_data=False
            )],
            namespace="namespace",
            ok_actions=["okActions"],
            period=123,
            statistic="statistic",
            threshold=123,
            threshold_metric_id="thresholdMetricId",
            treat_missing_data="treatMissingData",
            unit="unit"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        comparison_operator: builtins.str,
        evaluation_periods: jsii.Number,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        extended_statistic: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAlarm.MetricDataQueryProperty", _IResolvable_a771d0ef]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[jsii.Number] = None,
        threshold_metric_id: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudWatch::Alarm``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand. You can specify the following values: ``GreaterThanThreshold`` , ``GreaterThanOrEqualToThreshold`` , ``LessThanThreshold`` , or ``LessThanOrEqualToThreshold`` .
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        :param alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description of the alarm.
        :param alarm_name: The name of the alarm. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.
        :param dimensions: The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .
        :param evaluate_low_sample_count_percentile: Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
        :param extended_statistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param metric_name: The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .
        :param metrics: An array that enables you to create an alarm based on the result of a metric math expression. Each item in the array either retrieves a metric or performs a math expression. If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .
        :param namespace: The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead. For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_
        :param ok_actions: The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param period: The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60. For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter. *Minimum:* 10
        :param statistic: The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .
        :param threshold: The value to compare with the specified statistic.
        :param threshold_metric_id: In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, the default behavior of ``missing`` is used.
        :param unit: The unit of the metric associated with the alarm. Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array. You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.
        '''
        props = CfnAlarmProps(
            comparison_operator=comparison_operator,
            evaluation_periods=evaluation_periods,
            actions_enabled=actions_enabled,
            alarm_actions=alarm_actions,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            datapoints_to_alarm=datapoints_to_alarm,
            dimensions=dimensions,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            extended_statistic=extended_statistic,
            insufficient_data_actions=insufficient_data_actions,
            metric_name=metric_name,
            metrics=metrics,
            namespace=namespace,
            ok_actions=ok_actions,
            period=period,
            statistic=statistic,
            threshold=threshold,
            threshold_metric_id=threshold_metric_id,
            treat_missing_data=treat_missing_data,
            unit=unit,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the CloudWatch alarm, such as ``arn:aws:cloudwatch:us-west-2:123456789012:alarm:myCloudWatchAlarm-CPUAlarm-UXMMZK36R55Z`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="comparisonOperator")
    def comparison_operator(self) -> builtins.str:
        '''The arithmetic operation to use when comparing the specified statistic and threshold.

        The specified statistic value is used as the first operand.

        You can specify the following values: ``GreaterThanThreshold`` , ``GreaterThanOrEqualToThreshold`` , ``LessThanThreshold`` , or ``LessThanOrEqualToThreshold`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-comparisonoperator
        '''
        return typing.cast(builtins.str, jsii.get(self, "comparisonOperator"))

    @comparison_operator.setter
    def comparison_operator(self, value: builtins.str) -> None:
        jsii.set(self, "comparisonOperator", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.

        If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M.

        For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluationperiods
        '''
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="actionsEnabled")
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether actions should be executed during any changes to the alarm state.

        The default is TRUE.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-actionsenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "actionsEnabled"))

    @actions_enabled.setter
    def actions_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "actionsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmActions")
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of actions to execute when this alarm transitions into an ALARM state from any other state.

        Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmactions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmActions"))

    @alarm_actions.setter
    def alarm_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "alarmActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmDescription")
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description of the alarm.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmDescription"))

    @alarm_description.setter
    def alarm_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "alarmDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alarm.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "alarmName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .

        If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-datapointstoalarm
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datapointsToAlarm"))

    @datapoints_to_alarm.setter
    def datapoints_to_alarm(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "datapointsToAlarm", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]]:
        '''The dimensions for the metric associated with the alarm.

        For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dimension
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "dimensions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="evaluateLowSampleCountPercentile")
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''Used only for alarms based on percentiles.

        If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluatelowsamplecountpercentile
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateLowSampleCountPercentile"))

    @evaluate_low_sample_count_percentile.setter
    def evaluate_low_sample_count_percentile(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "evaluateLowSampleCountPercentile", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="extendedStatistic")
    def extended_statistic(self) -> typing.Optional[builtins.str]:
        '''The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

        For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both.

        For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-extendedstatistic
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extendedStatistic"))

    @extended_statistic.setter
    def extended_statistic(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "extendedStatistic", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="insufficientDataActions")
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state.

        Each action is specified as an Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-insufficientdataactions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insufficientDataActions"))

    @insufficient_data_actions.setter
    def insufficient_data_actions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "insufficientDataActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the alarm.

        This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-metricname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "metricName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metrics")
    def metrics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.MetricDataQueryProperty", _IResolvable_a771d0ef]]]]:
        '''An array that enables you to create an alarm based on the result of a metric math expression.

        Each item in the array either retrieves a metric or performs a math expression.

        If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-metrics
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.MetricDataQueryProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "metrics"))

    @metrics.setter
    def metrics(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.MetricDataQueryProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "metrics", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the alarm.

        This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead.

        For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-namespace
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "namespace", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="okActions")
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``OK`` state from any other state.

        Each action is specified as an Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-okactions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "okActions"))

    @ok_actions.setter
    def ok_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "okActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="period")
    def period(self) -> typing.Optional[jsii.Number]:
        '''The period, in seconds, over which the statistic is applied.

        This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60.

        For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter.

        *Minimum:* 10

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-period
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "period"))

    @period.setter
    def period(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "period", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

        For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both.

        For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-statistic
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "statistic", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''The value to compare with the specified statistic.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-threshold
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "threshold", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="thresholdMetricId")
    def threshold_metric_id(self) -> typing.Optional[builtins.str]:
        '''In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dynamic-threshold
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdMetricId"))

    @threshold_metric_id.setter
    def threshold_metric_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "thresholdMetricId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="treatMissingData")
    def treat_missing_data(self) -> typing.Optional[builtins.str]:
        '''Sets how this alarm is to handle missing data points.

        Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* .

        If you omit this parameter, the default behavior of ``missing`` is used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-treatmissingdata
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatMissingData"))

    @treat_missing_data.setter
    def treat_missing_data(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "treatMissingData", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unit")
    def unit(self) -> typing.Optional[builtins.str]:
        '''The unit of the metric associated with the alarm.

        Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array.

        You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-unit
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "unit", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAlarm.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Dimension is an embedded property of the ``AWS::CloudWatch::Alarm`` type.

            Dimensions are name/value pairs that can be associated with a CloudWatch metric. You can specify a maximum of 10 dimensions for a given metric.

            :param name: The name of the dimension, from 1–255 characters in length. This dimension name must have been included when the metric was published.
            :param value: The value for the dimension, from 1–255 characters in length.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                dimension_property = cloudwatch.CfnAlarm.DimensionProperty(
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
            '''The name of the dimension, from 1–255 characters in length.

            This dimension name must have been included when the metric was published.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html#cfn-cloudwatch-alarm-dimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for the dimension, from 1–255 characters in length.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html#cfn-cloudwatch-alarm-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAlarm.MetricDataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "account_id": "accountId",
            "expression": "expression",
            "label": "label",
            "metric_stat": "metricStat",
            "period": "period",
            "return_data": "returnData",
        },
    )
    class MetricDataQueryProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            account_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            label: typing.Optional[builtins.str] = None,
            metric_stat: typing.Optional[typing.Union["CfnAlarm.MetricStatProperty", _IResolvable_a771d0ef]] = None,
            period: typing.Optional[jsii.Number] = None,
            return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The ``MetricDataQuery`` property type specifies the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data.

            Any expression used must return a single time series. For more information, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            :param id: A short name used to tie this object to the results in the response. This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            :param account_id: The ID of the account where the metrics are located, if this is a cross-account alarm.
            :param expression: The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* . Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param label: A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If ``Label`` is omitted, CloudWatch generates a default.
            :param metric_stat: The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data. Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .
            :param return_data: This option indicates whether to return the timestamps and raw data values of this metric. When you create an alarm based on a metric math expression, specify ``True`` for this value for only the one math expression that the alarm is based on. You must specify ``False`` for ``ReturnData`` for all the other metrics and expressions used in the alarm. This field is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_data_query_property = cloudwatch.CfnAlarm.MetricDataQueryProperty(
                    id="id",
                
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAlarm.MetricStatProperty(
                        metric=cloudwatch.CfnAlarm.MetricProperty(
                            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                                name="name",
                                value="value"
                            )],
                            metric_name="metricName",
                            namespace="namespace"
                        ),
                        period=123,
                        stat="stat",
                
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
            }
            if account_id is not None:
                self._values["account_id"] = account_id
            if expression is not None:
                self._values["expression"] = expression
            if label is not None:
                self._values["label"] = label
            if metric_stat is not None:
                self._values["metric_stat"] = metric_stat
            if period is not None:
                self._values["period"] = period
            if return_data is not None:
                self._values["return_data"] = return_data

        @builtins.property
        def id(self) -> builtins.str:
            '''A short name used to tie this object to the results in the response.

            This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the account where the metrics are located, if this is a cross-account alarm.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''The math expression to be performed on the returned data, if this object is performing a math expression.

            This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''A human-readable label for this metric or expression.

            This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If ``Label`` is omitted, CloudWatch generates a default.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_stat(
            self,
        ) -> typing.Optional[typing.Union["CfnAlarm.MetricStatProperty", _IResolvable_a771d0ef]]:
            '''The metric to be returned, along with statistics, period, and units.

            Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.

            Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-metricstat
            '''
            result = self._values.get("metric_stat")
            return typing.cast(typing.Optional[typing.Union["CfnAlarm.MetricStatProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def period(self) -> typing.Optional[jsii.Number]:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .
            '''
            result = self._values.get("period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def return_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''This option indicates whether to return the timestamps and raw data values of this metric.

            When you create an alarm based on a metric math expression, specify ``True`` for this value for only the one math expression that the alarm is based on. You must specify ``False`` for ``ReturnData`` for all the other metrics and expressions used in the alarm.

            This field is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-returndata
            '''
            result = self._values.get("return_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAlarm.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "namespace": "namespace",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``Metric`` property type represents a specific metric.

            ``Metric`` is a property of the `MetricStat <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html>`_ property type.

            :param dimensions: The metric dimensions that you want to be used for the metric that the alarm will watch..
            :param metric_name: The name of the metric that you want the alarm to watch. This is a required field.
            :param namespace: The namespace of the metric that the alarm will watch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_property = cloudwatch.CfnAlarm.MetricProperty(
                    dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]]:
            '''The metric dimensions that you want to be used for the metric that the alarm will watch..

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAlarm.DimensionProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric that you want the alarm to watch.

            This is a required field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric that the alarm will watch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAlarm.MetricStatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric": "metric",
            "period": "period",
            "stat": "stat",
            "unit": "unit",
        },
    )
    class MetricStatProperty:
        def __init__(
            self,
            *,
            metric: typing.Union["CfnAlarm.MetricProperty", _IResolvable_a771d0ef],
            period: jsii.Number,
            stat: builtins.str,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the metric to be returned, along with the statistics, period, and units.

            ``MetricStat`` is a property of the `MetricDataQuery <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html>`_ property type.

            :param metric: The metric to return, including the metric name, namespace, and dimensions.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second. If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned: - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
            :param stat: The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in `Statistics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic>`_ in the *Amazon CloudWatch User Guide* .
            :param unit: The unit to use for the returned data points. Valid values are: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_stat_property = cloudwatch.CfnAlarm.MetricStatProperty(
                    metric=cloudwatch.CfnAlarm.MetricProperty(
                        dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        namespace="namespace"
                    ),
                    period=123,
                    stat="stat",
                
                    # the properties below are optional
                    unit="unit"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric": metric,
                "period": period,
                "stat": stat,
            }
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric(
            self,
        ) -> typing.Union["CfnAlarm.MetricProperty", _IResolvable_a771d0ef]:
            '''The metric to return, including the metric name, namespace, and dimensions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(typing.Union["CfnAlarm.MetricProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

            If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

            - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
            - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
            - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def stat(self) -> builtins.str:
            '''The statistic to return.

            It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in `Statistics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic>`_ in the *Amazon CloudWatch User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-stat
            '''
            result = self._values.get("stat")
            assert result is not None, "Required property 'stat' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit to use for the returned data points.

            Valid values are: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CfnAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "comparison_operator": "comparisonOperator",
        "evaluation_periods": "evaluationPeriods",
        "actions_enabled": "actionsEnabled",
        "alarm_actions": "alarmActions",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "datapoints_to_alarm": "datapointsToAlarm",
        "dimensions": "dimensions",
        "evaluate_low_sample_count_percentile": "evaluateLowSampleCountPercentile",
        "extended_statistic": "extendedStatistic",
        "insufficient_data_actions": "insufficientDataActions",
        "metric_name": "metricName",
        "metrics": "metrics",
        "namespace": "namespace",
        "ok_actions": "okActions",
        "period": "period",
        "statistic": "statistic",
        "threshold": "threshold",
        "threshold_metric_id": "thresholdMetricId",
        "treat_missing_data": "treatMissingData",
        "unit": "unit",
    },
)
class CfnAlarmProps:
    def __init__(
        self,
        *,
        comparison_operator: builtins.str,
        evaluation_periods: jsii.Number,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnAlarm.DimensionProperty, _IResolvable_a771d0ef]]]] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        extended_statistic: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnAlarm.MetricDataQueryProperty, _IResolvable_a771d0ef]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[jsii.Number] = None,
        threshold_metric_id: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlarm``.

        :param comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand. You can specify the following values: ``GreaterThanThreshold`` , ``GreaterThanOrEqualToThreshold`` , ``LessThanThreshold`` , or ``LessThanOrEqualToThreshold`` .
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        :param alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description of the alarm.
        :param alarm_name: The name of the alarm. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.
        :param dimensions: The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .
        :param evaluate_low_sample_count_percentile: Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
        :param extended_statistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param metric_name: The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .
        :param metrics: An array that enables you to create an alarm based on the result of a metric math expression. Each item in the array either retrieves a metric or performs a math expression. If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .
        :param namespace: The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead. For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_
        :param ok_actions: The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param period: The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60. For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter. *Minimum:* 10
        :param statistic: The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .
        :param threshold: The value to compare with the specified statistic.
        :param threshold_metric_id: In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, the default behavior of ``missing`` is used.
        :param unit: The unit of the metric associated with the alarm. Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array. You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            cfn_alarm_props = cloudwatch.CfnAlarmProps(
                comparison_operator="comparisonOperator",
                evaluation_periods=123,
            
                # the properties below are optional
                actions_enabled=False,
                alarm_actions=["alarmActions"],
                alarm_description="alarmDescription",
                alarm_name="alarmName",
                datapoints_to_alarm=123,
                dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                    name="name",
                    value="value"
                )],
                evaluate_low_sample_count_percentile="evaluateLowSampleCountPercentile",
                extended_statistic="extendedStatistic",
                insufficient_data_actions=["insufficientDataActions"],
                metric_name="metricName",
                metrics=[cloudwatch.CfnAlarm.MetricDataQueryProperty(
                    id="id",
            
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAlarm.MetricStatProperty(
                        metric=cloudwatch.CfnAlarm.MetricProperty(
                            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                                name="name",
                                value="value"
                            )],
                            metric_name="metricName",
                            namespace="namespace"
                        ),
                        period=123,
                        stat="stat",
            
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )],
                namespace="namespace",
                ok_actions=["okActions"],
                period=123,
                statistic="statistic",
                threshold=123,
                threshold_metric_id="thresholdMetricId",
                treat_missing_data="treatMissingData",
                unit="unit"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "comparison_operator": comparison_operator,
            "evaluation_periods": evaluation_periods,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_actions is not None:
            self._values["alarm_actions"] = alarm_actions
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if evaluate_low_sample_count_percentile is not None:
            self._values["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
        if extended_statistic is not None:
            self._values["extended_statistic"] = extended_statistic
        if insufficient_data_actions is not None:
            self._values["insufficient_data_actions"] = insufficient_data_actions
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if metrics is not None:
            self._values["metrics"] = metrics
        if namespace is not None:
            self._values["namespace"] = namespace
        if ok_actions is not None:
            self._values["ok_actions"] = ok_actions
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if threshold is not None:
            self._values["threshold"] = threshold
        if threshold_metric_id is not None:
            self._values["threshold_metric_id"] = threshold_metric_id
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def comparison_operator(self) -> builtins.str:
        '''The arithmetic operation to use when comparing the specified statistic and threshold.

        The specified statistic value is used as the first operand.

        You can specify the following values: ``GreaterThanThreshold`` , ``GreaterThanOrEqualToThreshold`` , ``LessThanThreshold`` , or ``LessThanOrEqualToThreshold`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-comparisonoperator
        '''
        result = self._values.get("comparison_operator")
        assert result is not None, "Required property 'comparison_operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.

        If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M.

        For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluationperiods
        '''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether actions should be executed during any changes to the alarm state.

        The default is TRUE.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-actionsenabled
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of actions to execute when this alarm transitions into an ALARM state from any other state.

        Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmactions
        '''
        result = self._values.get("alarm_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description of the alarm.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmdescription
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alarm.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmname
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .

        If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-datapointstoalarm
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAlarm.DimensionProperty, _IResolvable_a771d0ef]]]]:
        '''The dimensions for the metric associated with the alarm.

        For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dimension
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAlarm.DimensionProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''Used only for alarms based on percentiles.

        If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluatelowsamplecountpercentile
        '''
        result = self._values.get("evaluate_low_sample_count_percentile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extended_statistic(self) -> typing.Optional[builtins.str]:
        '''The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

        For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both.

        For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-extendedstatistic
        '''
        result = self._values.get("extended_statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state.

        Each action is specified as an Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-insufficientdataactions
        '''
        result = self._values.get("insufficient_data_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the alarm.

        This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-metricname
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAlarm.MetricDataQueryProperty, _IResolvable_a771d0ef]]]]:
        '''An array that enables you to create an alarm based on the result of a metric math expression.

        Each item in the array either retrieves a metric or performs a math expression.

        If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAlarm.MetricDataQueryProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the alarm.

        This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead.

        For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``OK`` state from any other state.

        Each action is specified as an Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-okactions
        '''
        result = self._values.get("ok_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''The period, in seconds, over which the statistic is applied.

        This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60.

        For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter.

        *Minimum:* 10

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-period
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

        For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both.

        For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-statistic
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''The value to compare with the specified statistic.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_metric_id(self) -> typing.Optional[builtins.str]:
        '''In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dynamic-threshold
        '''
        result = self._values.get("threshold_metric_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional[builtins.str]:
        '''Sets how this alarm is to handle missing data points.

        Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* .

        If you omit this parameter, the default behavior of ``missing`` is used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-treatmissingdata
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''The unit of the metric associated with the alarm.

        Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array.

        You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAnomalyDetector(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector",
):
    '''A CloudFormation ``AWS::CloudWatch::AnomalyDetector``.

    The ``AWS::CloudWatch::AnomalyDetector`` type specifies an anomaly detection band for a certain metric and statistic. The band represents the expected "normal" range for the metric values. Anomaly detection bands can be used for visualization of a metric's expected values, and for alarms.

    :cloudformationResource: AWS::CloudWatch::AnomalyDetector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        cfn_anomaly_detector = cloudwatch.CfnAnomalyDetector(self, "MyCfnAnomalyDetector",
            configuration=cloudwatch.CfnAnomalyDetector.ConfigurationProperty(
                excluded_time_ranges=[cloudwatch.CfnAnomalyDetector.RangeProperty(
                    end_time="endTime",
                    start_time="startTime"
                )],
                metric_time_zone="metricTimeZone"
            ),
            dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                name="name",
                value="value"
            )],
            metric_math_anomaly_detector=cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty(
                metric_data_queries=[cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                    id="id",
        
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                        metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                            metric_name="metricName",
                            namespace="namespace",
        
                            # the properties below are optional
                            dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                name="name",
                                value="value"
                            )]
                        ),
                        period=123,
                        stat="stat",
        
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )]
            ),
            metric_name="metricName",
            namespace="namespace",
            single_metric_anomaly_detector=cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty(
                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                    name="name",
                    value="value"
                )],
                metric_name="metricName",
                namespace="namespace",
                stat="stat"
            ),
            stat="stat"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        configuration: typing.Optional[typing.Union["CfnAnomalyDetector.ConfigurationProperty", _IResolvable_a771d0ef]] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]] = None,
        metric_math_anomaly_detector: typing.Optional[typing.Union["CfnAnomalyDetector.MetricMathAnomalyDetectorProperty", _IResolvable_a771d0ef]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        single_metric_anomaly_detector: typing.Optional[typing.Union["CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty", _IResolvable_a771d0ef]] = None,
        stat: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudWatch::AnomalyDetector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration: Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. The configuration can also include the time zone to use for the metric.
        :param dimensions: The dimensions of the metric associated with the anomaly detection band.
        :param metric_math_anomaly_detector: The CloudWatch metric math expression for this anomaly detector.
        :param metric_name: The name of the metric associated with the anomaly detection band.
        :param namespace: The namespace of the metric associated with the anomaly detection band.
        :param single_metric_anomaly_detector: The CloudWatch metric and statistic for this anomaly detector.
        :param stat: The statistic of the metric associated with the anomaly detection band.
        '''
        props = CfnAnomalyDetectorProps(
            configuration=configuration,
            dimensions=dimensions,
            metric_math_anomaly_detector=metric_math_anomaly_detector,
            metric_name=metric_name,
            namespace=namespace,
            single_metric_anomaly_detector=single_metric_anomaly_detector,
            stat=stat,
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
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnAnomalyDetector.ConfigurationProperty", _IResolvable_a771d0ef]]:
        '''Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model.

        The configuration can also include the time zone to use for the metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-configuration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.ConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union["CfnAnomalyDetector.ConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "configuration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]]:
        '''The dimensions of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-dimensions
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "dimensions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricMathAnomalyDetector")
    def metric_math_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union["CfnAnomalyDetector.MetricMathAnomalyDetectorProperty", _IResolvable_a771d0ef]]:
        '''The CloudWatch metric math expression for this anomaly detector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.MetricMathAnomalyDetectorProperty", _IResolvable_a771d0ef]], jsii.get(self, "metricMathAnomalyDetector"))

    @metric_math_anomaly_detector.setter
    def metric_math_anomaly_detector(
        self,
        value: typing.Optional[typing.Union["CfnAnomalyDetector.MetricMathAnomalyDetectorProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "metricMathAnomalyDetector", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "metricName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-namespace
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "namespace", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="singleMetricAnomalyDetector")
    def single_metric_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union["CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty", _IResolvable_a771d0ef]]:
        '''The CloudWatch metric and statistic for this anomaly detector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty", _IResolvable_a771d0ef]], jsii.get(self, "singleMetricAnomalyDetector"))

    @single_metric_anomaly_detector.setter
    def single_metric_anomaly_detector(
        self,
        value: typing.Optional[typing.Union["CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "singleMetricAnomalyDetector", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stat")
    def stat(self) -> typing.Optional[builtins.str]:
        '''The statistic of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-stat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "stat", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "excluded_time_ranges": "excludedTimeRanges",
            "metric_time_zone": "metricTimeZone",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            excluded_time_ranges: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.RangeProperty", _IResolvable_a771d0ef]]]] = None,
            metric_time_zone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model.

            The configuration can also include the time zone to use for the metric.

            :param excluded_time_ranges: Specifies an array of time ranges to exclude from use when the anomaly detection model is trained and updated. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates or updates the model.
            :param metric_time_zone: The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes. To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see `tz database <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Tz_database>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                configuration_property = cloudwatch.CfnAnomalyDetector.ConfigurationProperty(
                    excluded_time_ranges=[cloudwatch.CfnAnomalyDetector.RangeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )],
                    metric_time_zone="metricTimeZone"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_time_ranges is not None:
                self._values["excluded_time_ranges"] = excluded_time_ranges
            if metric_time_zone is not None:
                self._values["metric_time_zone"] = metric_time_zone

        @builtins.property
        def excluded_time_ranges(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.RangeProperty", _IResolvable_a771d0ef]]]]:
            '''Specifies an array of time ranges to exclude from use when the anomaly detection model is trained and updated.

            Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates or updates the model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-excludedtimeranges
            '''
            result = self._values.get("excluded_time_ranges")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.RangeProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def metric_time_zone(self) -> typing.Optional[builtins.str]:
            '''The time zone to use for the metric.

            This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.

            To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see `tz database <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Tz_database>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-metrictimezone
            '''
            result = self._values.get("metric_time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''A dimension is a name/value pair that is part of the identity of a metric.

            You can assign up to 10 dimensions to a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric.

            :param name: The name of the dimension.
            :param value: The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                dimension_property = cloudwatch.CfnAnomalyDetector.DimensionProperty(
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

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the dimension.

            Dimension values must contain only ASCII characters and must include at least one non-whitespace character.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "account_id": "accountId",
            "expression": "expression",
            "label": "label",
            "metric_stat": "metricStat",
            "period": "period",
            "return_data": "returnData",
        },
    )
    class MetricDataQueryProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            account_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            label: typing.Optional[builtins.str] = None,
            metric_stat: typing.Optional[typing.Union["CfnAnomalyDetector.MetricStatProperty", _IResolvable_a771d0ef]] = None,
            period: typing.Optional[jsii.Number] = None,
            return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` .

            The supported use of this structure is different for those two operations.

            When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a Metrics Insights query or a math expression. A single ``GetMetricData`` call can include up to 500 ``MetricDataQuery`` structures.

            When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The result of this expression is the value the alarm watches.

            Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For more information, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Some of the parameters of this structure also have different uses whether you are using this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These differences are explained in the following parameter list.

            :param id: A short name used to tie this object to the results in the response. This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            :param account_id: The ID of the account where the metrics are located, if this is a cross-account alarm. Use this field only for ``PutMetricAlarm`` operations. It is not used in ``GetMetricData`` operations.
            :param expression: This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data. For more information about Metrics Insights queries, see `Metrics Insights query components and syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage>`_ in the *Amazon CloudWatch User Guide* . A math expression can use the ``Id`` of the other metrics or queries to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* . Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param label: A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default. You can put dynamic expressions into a label, so that it is more descriptive. For more information, see `Using Dynamic Labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ .
            :param metric_stat: The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data. Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .
            :param return_data: When used in ``GetMetricData`` , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify ``False`` . If you omit this, the default of ``True`` is used. When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_data_query_property = cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                    id="id",
                
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                        metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                            metric_name="metricName",
                            namespace="namespace",
                
                            # the properties below are optional
                            dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                name="name",
                                value="value"
                            )]
                        ),
                        period=123,
                        stat="stat",
                
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
            }
            if account_id is not None:
                self._values["account_id"] = account_id
            if expression is not None:
                self._values["expression"] = expression
            if label is not None:
                self._values["label"] = label
            if metric_stat is not None:
                self._values["metric_stat"] = metric_stat
            if period is not None:
                self._values["period"] = period
            if return_data is not None:
                self._values["return_data"] = return_data

        @builtins.property
        def id(self) -> builtins.str:
            '''A short name used to tie this object to the results in the response.

            This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the account where the metrics are located, if this is a cross-account alarm.

            Use this field only for ``PutMetricAlarm`` operations. It is not used in ``GetMetricData`` operations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data.

            For more information about Metrics Insights queries, see `Metrics Insights query components and syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage>`_ in the *Amazon CloudWatch User Guide* .

            A math expression can use the ``Id`` of the other metrics or queries to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''A human-readable label for this metric or expression.

            This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.

            You can put dynamic expressions into a label, so that it is more descriptive. For more information, see `Using Dynamic Labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_stat(
            self,
        ) -> typing.Optional[typing.Union["CfnAnomalyDetector.MetricStatProperty", _IResolvable_a771d0ef]]:
            '''The metric to be returned, along with statistics, period, and units.

            Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.

            Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-metricstat
            '''
            result = self._values.get("metric_stat")
            return typing.cast(typing.Optional[typing.Union["CfnAnomalyDetector.MetricStatProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def period(self) -> typing.Optional[jsii.Number]:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-period
            '''
            result = self._values.get("period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def return_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When used in ``GetMetricData`` , this option indicates whether to return the timestamps and raw data values of this metric.

            If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify ``False`` . If you omit this, the default of ``True`` is used.

            When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-returndata
            '''
            result = self._values.get("return_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty",
        jsii_struct_bases=[],
        name_mapping={"metric_data_queries": "metricDataQueries"},
    )
    class MetricMathAnomalyDetectorProperty:
        def __init__(
            self,
            *,
            metric_data_queries: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.MetricDataQueryProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''Indicates the CloudWatch math expression that provides the time series the anomaly detector uses as input.

            The designated math expression must return a single time series.

            :param metric_data_queries: An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression. Each item in ``MetricDataQueries`` gets a metric or performs a math expression. One item in ``MetricDataQueries`` is the expression that provides the time series that the anomaly detector uses as input. Designate the expression by setting ``ReturnData`` to ``True`` for this object in the array. For all other expressions and metrics, set ``ReturnData`` to ``False`` . The designated expression must return a single time series.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_math_anomaly_detector_property = cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty(
                    metric_data_queries=[cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                        id="id",
                
                        # the properties below are optional
                        account_id="accountId",
                        expression="expression",
                        label="label",
                        metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                            metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                                metric_name="metricName",
                                namespace="namespace",
                
                                # the properties below are optional
                                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                    name="name",
                                    value="value"
                                )]
                            ),
                            period=123,
                            stat="stat",
                
                            # the properties below are optional
                            unit="unit"
                        ),
                        period=123,
                        return_data=False
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if metric_data_queries is not None:
                self._values["metric_data_queries"] = metric_data_queries

        @builtins.property
        def metric_data_queries(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricDataQueryProperty", _IResolvable_a771d0ef]]]]:
            '''An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression.

            Each item in ``MetricDataQueries`` gets a metric or performs a math expression. One item in ``MetricDataQueries`` is the expression that provides the time series that the anomaly detector uses as input. Designate the expression by setting ``ReturnData`` to ``True`` for this object in the array. For all other expressions and metrics, set ``ReturnData`` to ``False`` . The designated expression must return a single time series.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries
            '''
            result = self._values.get("metric_data_queries")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.MetricDataQueryProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricMathAnomalyDetectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "dimensions": "dimensions",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''Represents a specific metric.

            :param metric_name: The name of the metric. This is a required field.
            :param namespace: The namespace of the metric.
            :param dimensions: The dimensions for the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_property = cloudwatch.CfnAnomalyDetector.MetricProperty(
                    metric_name="metricName",
                    namespace="namespace",
                
                    # the properties below are optional
                    dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            This is a required field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]]:
            '''The dimensions for the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.MetricStatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric": "metric",
            "period": "period",
            "stat": "stat",
            "unit": "unit",
        },
    )
    class MetricStatProperty:
        def __init__(
            self,
            *,
            metric: typing.Union["CfnAnomalyDetector.MetricProperty", _IResolvable_a771d0ef],
            period: jsii.Number,
            stat: builtins.str,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the metric to be returned, along with the statistics, period, and units.

            :param metric: The metric to return, including the metric name, namespace, and dimensions.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second. If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned: - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
            :param stat: The statistic to return. It can include any CloudWatch statistic or extended statistic.
            :param unit: When you are using a ``Put`` operation, this defines what unit you want to use when storing the metric. In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_stat_property = cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                    metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                        metric_name="metricName",
                        namespace="namespace",
                
                        # the properties below are optional
                        dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    period=123,
                    stat="stat",
                
                    # the properties below are optional
                    unit="unit"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric": metric,
                "period": period,
                "stat": stat,
            }
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric(
            self,
        ) -> typing.Union["CfnAnomalyDetector.MetricProperty", _IResolvable_a771d0ef]:
            '''The metric to return, including the metric name, namespace, and dimensions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(typing.Union["CfnAnomalyDetector.MetricProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

            If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

            - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
            - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
            - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def stat(self) -> builtins.str:
            '''The statistic to return.

            It can include any CloudWatch statistic or extended statistic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-stat
            '''
            result = self._values.get("stat")
            assert result is not None, "Required property 'stat' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''When you are using a ``Put`` operation, this defines what unit you want to use when storing the metric.

            In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.RangeProperty",
        jsii_struct_bases=[],
        name_mapping={"end_time": "endTime", "start_time": "startTime"},
    )
    class RangeProperty:
        def __init__(self, *, end_time: builtins.str, start_time: builtins.str) -> None:
            '''Each ``Range`` specifies one range of days or times to exclude from use for training or updating an anomaly detection model.

            :param end_time: The end time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .
            :param start_time: The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                range_property = cloudwatch.CfnAnomalyDetector.RangeProperty(
                    end_time="endTime",
                    start_time="startTime"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The end time of the range to exclude.

            The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''The start time of the range to exclude.

            The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "namespace": "namespace",
            "stat": "stat",
        },
    )
    class SingleMetricAnomalyDetectorProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
            stat: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Designates the CloudWatch metric and statistic that provides the time series the anomaly detector uses as input.

            :param dimensions: The metric dimensions to create the anomaly detection model for.
            :param metric_name: The name of the metric to create the anomaly detection model for.
            :param namespace: The namespace of the metric to create the anomaly detection model for.
            :param stat: The statistic to use for the metric and anomaly detection model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                single_metric_anomaly_detector_property = cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty(
                    dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace",
                    stat="stat"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if namespace is not None:
                self._values["namespace"] = namespace
            if stat is not None:
                self._values["stat"] = stat

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]]:
            '''The metric dimensions to create the anomaly detection model for.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnAnomalyDetector.DimensionProperty", _IResolvable_a771d0ef]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric to create the anomaly detection model for.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric to create the anomaly detection model for.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stat(self) -> typing.Optional[builtins.str]:
            '''The statistic to use for the metric and anomaly detection model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat
            '''
            result = self._values.get("stat")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleMetricAnomalyDetectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CfnAnomalyDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "dimensions": "dimensions",
        "metric_math_anomaly_detector": "metricMathAnomalyDetector",
        "metric_name": "metricName",
        "namespace": "namespace",
        "single_metric_anomaly_detector": "singleMetricAnomalyDetector",
        "stat": "stat",
    },
)
class CfnAnomalyDetectorProps:
    def __init__(
        self,
        *,
        configuration: typing.Optional[typing.Union[CfnAnomalyDetector.ConfigurationProperty, _IResolvable_a771d0ef]] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnAnomalyDetector.DimensionProperty, _IResolvable_a771d0ef]]]] = None,
        metric_math_anomaly_detector: typing.Optional[typing.Union[CfnAnomalyDetector.MetricMathAnomalyDetectorProperty, _IResolvable_a771d0ef]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        single_metric_anomaly_detector: typing.Optional[typing.Union[CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty, _IResolvable_a771d0ef]] = None,
        stat: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnomalyDetector``.

        :param configuration: Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. The configuration can also include the time zone to use for the metric.
        :param dimensions: The dimensions of the metric associated with the anomaly detection band.
        :param metric_math_anomaly_detector: The CloudWatch metric math expression for this anomaly detector.
        :param metric_name: The name of the metric associated with the anomaly detection band.
        :param namespace: The namespace of the metric associated with the anomaly detection band.
        :param single_metric_anomaly_detector: The CloudWatch metric and statistic for this anomaly detector.
        :param stat: The statistic of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            cfn_anomaly_detector_props = cloudwatch.CfnAnomalyDetectorProps(
                configuration=cloudwatch.CfnAnomalyDetector.ConfigurationProperty(
                    excluded_time_ranges=[cloudwatch.CfnAnomalyDetector.RangeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )],
                    metric_time_zone="metricTimeZone"
                ),
                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                    name="name",
                    value="value"
                )],
                metric_math_anomaly_detector=cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty(
                    metric_data_queries=[cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                        id="id",
            
                        # the properties below are optional
                        account_id="accountId",
                        expression="expression",
                        label="label",
                        metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                            metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                                metric_name="metricName",
                                namespace="namespace",
            
                                # the properties below are optional
                                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                    name="name",
                                    value="value"
                                )]
                            ),
                            period=123,
                            stat="stat",
            
                            # the properties below are optional
                            unit="unit"
                        ),
                        period=123,
                        return_data=False
                    )]
                ),
                metric_name="metricName",
                namespace="namespace",
                single_metric_anomaly_detector=cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty(
                    dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace",
                    stat="stat"
                ),
                stat="stat"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if configuration is not None:
            self._values["configuration"] = configuration
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if metric_math_anomaly_detector is not None:
            self._values["metric_math_anomaly_detector"] = metric_math_anomaly_detector
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if namespace is not None:
            self._values["namespace"] = namespace
        if single_metric_anomaly_detector is not None:
            self._values["single_metric_anomaly_detector"] = single_metric_anomaly_detector
        if stat is not None:
            self._values["stat"] = stat

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnAnomalyDetector.ConfigurationProperty, _IResolvable_a771d0ef]]:
        '''Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model.

        The configuration can also include the time zone to use for the metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[CfnAnomalyDetector.ConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnomalyDetector.DimensionProperty, _IResolvable_a771d0ef]]]]:
        '''The dimensions of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnAnomalyDetector.DimensionProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def metric_math_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union[CfnAnomalyDetector.MetricMathAnomalyDetectorProperty, _IResolvable_a771d0ef]]:
        '''The CloudWatch metric math expression for this anomaly detector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector
        '''
        result = self._values.get("metric_math_anomaly_detector")
        return typing.cast(typing.Optional[typing.Union[CfnAnomalyDetector.MetricMathAnomalyDetectorProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricname
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_metric_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union[CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty, _IResolvable_a771d0ef]]:
        '''The CloudWatch metric and statistic for this anomaly detector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector
        '''
        result = self._values.get("single_metric_anomaly_detector")
        return typing.cast(typing.Optional[typing.Union[CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def stat(self) -> typing.Optional[builtins.str]:
        '''The statistic of the metric associated with the anomaly detection band.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-stat
        '''
        result = self._values.get("stat")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalyDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnCompositeAlarm(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CfnCompositeAlarm",
):
    '''A CloudFormation ``AWS::CloudWatch::CompositeAlarm``.

    The ``AWS::CloudWatch::CompositeAlarm`` type creates or updates a composite alarm. When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.

    The alarms specified in a composite alarm's rule expression can include metric alarms and other composite alarms.

    Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.

    Currently, the only alarm actions that can be taken by composite alarms are notifying SNS topics.

    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in INSUFFICIENT_DATA state.

    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

    :cloudformationResource: AWS::CloudWatch::CompositeAlarm
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        cfn_composite_alarm = cloudwatch.CfnCompositeAlarm(self, "MyCfnCompositeAlarm",
            alarm_name="alarmName",
            alarm_rule="alarmRule",
        
            # the properties below are optional
            actions_enabled=False,
            alarm_actions=["alarmActions"],
            alarm_description="alarmDescription",
            insufficient_data_actions=["insufficientDataActions"],
            ok_actions=["okActions"]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        alarm_name: builtins.str,
        alarm_rule: builtins.str,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::CloudWatch::CompositeAlarm``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param alarm_name: The name for the composite alarm. This name must be unique within your AWS account.
        :param alarm_rule: An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression. You can use either alarm names or ARNs to reference the other alarms that are to be evaluated. Functions can include the following: - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state. - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state. - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state. - TRUE always evaluates to TRUE. - FALSE always evaluates to FALSE. TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions. For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is TRUE.
        :param alarm_actions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description for the composite alarm.
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param ok_actions: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        '''
        props = CfnCompositeAlarmProps(
            alarm_name=alarm_name,
            alarm_rule=alarm_rule,
            actions_enabled=actions_enabled,
            alarm_actions=alarm_actions,
            alarm_description=alarm_description,
            insufficient_data_actions=insufficient_data_actions,
            ok_actions=ok_actions,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the composite alarm, such as ``arn:aws:cloudwatch:us-west-2:123456789012:alarm/CompositeAlarmName`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''The name for the composite alarm.

        This name must be unique within your AWS account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmname
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: builtins.str) -> None:
        jsii.set(self, "alarmName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmRule")
    def alarm_rule(self) -> builtins.str:
        '''An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.

        For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.

        You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.

        Functions can include the following:

        - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state.
        - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state.
        - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state.
        - TRUE always evaluates to TRUE.
        - FALSE always evaluates to FALSE.

        TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions.

        For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmrule
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmRule"))

    @alarm_rule.setter
    def alarm_rule(self, value: builtins.str) -> None:
        jsii.set(self, "alarmRule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="actionsEnabled")
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether actions should be executed during any changes to the alarm state of the composite alarm.

        The default is TRUE.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionsenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "actionsEnabled"))

    @actions_enabled.setter
    def actions_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "actionsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmActions")
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ALARM state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmactions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmActions"))

    @alarm_actions.setter
    def alarm_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "alarmActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmDescription")
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description for the composite alarm.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmDescription"))

    @alarm_description.setter
    def alarm_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "alarmDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="insufficientDataActions")
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-insufficientdataactions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insufficientDataActions"))

    @insufficient_data_actions.setter
    def insufficient_data_actions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "insufficientDataActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="okActions")
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the OK state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-okactions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "okActions"))

    @ok_actions.setter
    def ok_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "okActions", value)


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CfnCompositeAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_name": "alarmName",
        "alarm_rule": "alarmRule",
        "actions_enabled": "actionsEnabled",
        "alarm_actions": "alarmActions",
        "alarm_description": "alarmDescription",
        "insufficient_data_actions": "insufficientDataActions",
        "ok_actions": "okActions",
    },
)
class CfnCompositeAlarmProps:
    def __init__(
        self,
        *,
        alarm_name: builtins.str,
        alarm_rule: builtins.str,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCompositeAlarm``.

        :param alarm_name: The name for the composite alarm. This name must be unique within your AWS account.
        :param alarm_rule: An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression. You can use either alarm names or ARNs to reference the other alarms that are to be evaluated. Functions can include the following: - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state. - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state. - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state. - TRUE always evaluates to TRUE. - FALSE always evaluates to FALSE. TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions. For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is TRUE.
        :param alarm_actions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description for the composite alarm.
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param ok_actions: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            cfn_composite_alarm_props = cloudwatch.CfnCompositeAlarmProps(
                alarm_name="alarmName",
                alarm_rule="alarmRule",
            
                # the properties below are optional
                actions_enabled=False,
                alarm_actions=["alarmActions"],
                alarm_description="alarmDescription",
                insufficient_data_actions=["insufficientDataActions"],
                ok_actions=["okActions"]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alarm_name": alarm_name,
            "alarm_rule": alarm_rule,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_actions is not None:
            self._values["alarm_actions"] = alarm_actions
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if insufficient_data_actions is not None:
            self._values["insufficient_data_actions"] = insufficient_data_actions
        if ok_actions is not None:
            self._values["ok_actions"] = ok_actions

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''The name for the composite alarm.

        This name must be unique within your AWS account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmname
        '''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_rule(self) -> builtins.str:
        '''An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.

        For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.

        You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.

        Functions can include the following:

        - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state.
        - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state.
        - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state.
        - TRUE always evaluates to TRUE.
        - FALSE always evaluates to FALSE.

        TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions.

        For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmrule
        '''
        result = self._values.get("alarm_rule")
        assert result is not None, "Required property 'alarm_rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether actions should be executed during any changes to the alarm state of the composite alarm.

        The default is TRUE.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionsenabled
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ALARM state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmactions
        '''
        result = self._values.get("alarm_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description for the composite alarm.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmdescription
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-insufficientdataactions
        '''
        result = self._values.get("insufficient_data_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the OK state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-okactions
        '''
        result = self._values.get("ok_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCompositeAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDashboard(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CfnDashboard",
):
    '''A CloudFormation ``AWS::CloudWatch::Dashboard``.

    The ``AWS::CloudWatch::Dashboard`` resource specifies an Amazon CloudWatch dashboard. A dashboard is a customizable home page in the CloudWatch console that you can use to monitor your AWS resources in a single view.

    All dashboards in your account are global, not region-specific.

    :cloudformationResource: AWS::CloudWatch::Dashboard
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        cfn_dashboard = cloudwatch.CfnDashboard(self, "MyCfnDashboard",
            dashboard_body="dashboardBody",
        
            # the properties below are optional
            dashboard_name="dashboardName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        dashboard_body: builtins.str,
        dashboard_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudWatch::Dashboard``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dashboard_body: The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required. For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .
        :param dashboard_name: The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.
        '''
        props = CfnDashboardProps(
            dashboard_body=dashboard_body, dashboard_name=dashboard_name
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
    @jsii.member(jsii_name="dashboardBody")
    def dashboard_body(self) -> builtins.str:
        '''The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard.

        This parameter is required.

        For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardbody
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardBody"))

    @dashboard_body.setter
    def dashboard_body(self, value: builtins.str) -> None:
        jsii.set(self, "dashboardBody", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dashboardName")
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dashboard.

        The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dashboardName"))

    @dashboard_name.setter
    def dashboard_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dashboardName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_body": "dashboardBody",
        "dashboard_name": "dashboardName",
    },
)
class CfnDashboardProps:
    def __init__(
        self,
        *,
        dashboard_body: builtins.str,
        dashboard_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDashboard``.

        :param dashboard_body: The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required. For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .
        :param dashboard_name: The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            cfn_dashboard_props = cloudwatch.CfnDashboardProps(
                dashboard_body="dashboardBody",
            
                # the properties below are optional
                dashboard_name="dashboardName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dashboard_body": dashboard_body,
        }
        if dashboard_name is not None:
            self._values["dashboard_name"] = dashboard_name

    @builtins.property
    def dashboard_body(self) -> builtins.str:
        '''The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard.

        This parameter is required.

        For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardbody
        '''
        result = self._values.get("dashboard_body")
        assert result is not None, "Required property 'dashboard_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dashboard.

        The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardname
        '''
        result = self._values.get("dashboard_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnInsightRule(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CfnInsightRule",
):
    '''A CloudFormation ``AWS::CloudWatch::InsightRule``.

    Creates or updates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see `Using Contributor Insights to Analyze High-Cardinality Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html>`_ in the *Amazon CloudWatch User Guide* .

    :cloudformationResource: AWS::CloudWatch::InsightRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        cfn_insight_rule = cloudwatch.CfnInsightRule(self, "MyCfnInsightRule",
            rule_body="ruleBody",
            rule_name="ruleName",
            rule_state="ruleState",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        rule_body: builtins.str,
        rule_name: builtins.str,
        rule_state: builtins.str,
        tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CloudWatch::InsightRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param rule_body: The definition of the rule, as a JSON object. For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .
        :param rule_name: The name of the rule.
        :param rule_state: The current state of the rule. Valid values are ``ENABLED`` and ``DISABLED`` .
        :param tags: A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule. Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ . To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.
        '''
        props = CfnInsightRuleProps(
            rule_body=rule_body, rule_name=rule_name, rule_state=rule_state, tags=tags
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the Contributor Insights rule, such as ``arn:aws:cloudwatch:us-west-2:123456789012:insight-rule/MyInsightRuleName`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRuleName")
    def attr_rule_name(self) -> builtins.str:
        '''The name of the Contributor Insights rule.

        :cloudformationAttribute: RuleName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''A list of key-value pairs to associate with the Contributor Insights rule.

        You can associate as many as 50 tags with a rule.

        Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ .

        To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleBody")
    def rule_body(self) -> builtins.str:
        '''The definition of the rule, as a JSON object.

        For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulebody
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleBody"))

    @rule_body.setter
    def rule_body(self, value: builtins.str) -> None:
        jsii.set(self, "ruleBody", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        jsii.set(self, "ruleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleState")
    def rule_state(self) -> builtins.str:
        '''The current state of the rule.

        Valid values are ``ENABLED`` and ``DISABLED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulestate
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleState"))

    @rule_state.setter
    def rule_state(self, value: builtins.str) -> None:
        jsii.set(self, "ruleState", value)


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CfnInsightRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "rule_body": "ruleBody",
        "rule_name": "ruleName",
        "rule_state": "ruleState",
        "tags": "tags",
    },
)
class CfnInsightRuleProps:
    def __init__(
        self,
        *,
        rule_body: builtins.str,
        rule_name: builtins.str,
        rule_state: builtins.str,
        tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInsightRule``.

        :param rule_body: The definition of the rule, as a JSON object. For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .
        :param rule_name: The name of the rule.
        :param rule_state: The current state of the rule. Valid values are ``ENABLED`` and ``DISABLED`` .
        :param tags: A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule. Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ . To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            cfn_insight_rule_props = cloudwatch.CfnInsightRuleProps(
                rule_body="ruleBody",
                rule_name="ruleName",
                rule_state="ruleState",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "rule_body": rule_body,
            "rule_name": rule_name,
            "rule_state": rule_state,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule_body(self) -> builtins.str:
        '''The definition of the rule, as a JSON object.

        For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulebody
        '''
        result = self._values.get("rule_body")
        assert result is not None, "Required property 'rule_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_state(self) -> builtins.str:
        '''The current state of the rule.

        Valid values are ``ENABLED`` and ``DISABLED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulestate
        '''
        result = self._values.get("rule_state")
        assert result is not None, "Required property 'rule_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]]:
        '''A list of key-value pairs to associate with the Contributor Insights rule.

        You can associate as many as 50 tags with a rule.

        Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ .

        To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInsightRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnMetricStream(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CfnMetricStream",
):
    '''A CloudFormation ``AWS::CloudWatch::MetricStream``.

    Creates or updates a metric stream. Metrics streams can automatically stream CloudWatch metrics to AWS destinations including Amazon S3 and to many third-party solutions. For more information, see `Metric streams <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html>`_ .

    To create a metric stream, you must be logged on to an account that has the ``iam:PassRole`` permission and either the *CloudWatchFullAccess* policy or the ``cloudwatch:PutMetricStream`` permission.

    When you create or update a metric stream, you choose one of the following:

    - Stream metrics from all metric namespaces in the account.
    - Stream metrics from all metric namespaces in the account, except for the namespaces that you list in ``ExcludeFilters`` .
    - Stream metrics from only the metric namespaces that you list in ``IncludeFilters`` .

    When you create a metric stream, the stream is created in the ``running`` state. If you update an existing metric stream, the state does not change.

    :cloudformationResource: AWS::CloudWatch::MetricStream
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        cfn_metric_stream = cloudwatch.CfnMetricStream(self, "MyCfnMetricStream",
            firehose_arn="firehoseArn",
            output_format="outputFormat",
            role_arn="roleArn",
        
            # the properties below are optional
            exclude_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                namespace="namespace"
            )],
            include_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                namespace="namespace"
            )],
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        firehose_arn: builtins.str,
        output_format: builtins.str,
        role_arn: builtins.str,
        exclude_filters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]] = None,
        include_filters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Create a new ``AWS::CloudWatch::MetricStream``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firehose_arn: The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream. This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.
        :param output_format: The output format for the stream. Valid values are ``json`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ . This parameter is required.
        :param role_arn: The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.
        :param exclude_filters: If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param include_filters: If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param name: If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region. If you are updating a metric stream, specify the name of that stream here.
        :param tags: An array of key-value pairs to apply to the metric stream. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        props = CfnMetricStreamProps(
            firehose_arn=firehose_arn,
            output_format=output_format,
            role_arn=role_arn,
            exclude_filters=exclude_filters,
            include_filters=include_filters,
            name=name,
            tags=tags,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the metric stream.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date that the metric stream was originally created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastUpdateDate")
    def attr_last_update_date(self) -> builtins.str:
        '''The date that the metric stream was most recently updated.

        :cloudformationAttribute: LastUpdateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateDate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the metric stream, either ``running`` or ``stopped`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''An array of key-value pairs to apply to the metric stream.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firehoseArn")
    def firehose_arn(self) -> builtins.str:
        '''The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream.

        This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-firehosearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "firehoseArn"))

    @firehose_arn.setter
    def firehose_arn(self, value: builtins.str) -> None:
        jsii.set(self, "firehoseArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        '''The output format for the stream.

        Valid values are ``json`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ .

        This parameter is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-outputformat
        '''
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        jsii.set(self, "outputFormat", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources.

        This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeFilters")
    def exclude_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]]:
        '''If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.

        You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream.

        When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-excludefilters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "excludeFilters"))

    @exclude_filters.setter
    def exclude_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "excludeFilters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="includeFilters")
    def include_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]]:
        '''If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.

        You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream.

        When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includefilters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "includeFilters"))

    @include_filters.setter
    def include_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnMetricStream.MetricStreamFilterProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "includeFilters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''If you are creating a new metric stream, this is the name for the new stream.

        The name must be different than the names of other metric streams in this account and Region.

        If you are updating a metric stream, specify the name of that stream here.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_cloudwatch.CfnMetricStream.MetricStreamFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class MetricStreamFilterProperty:
        def __init__(self, *, namespace: builtins.str) -> None:
            '''This structure contains the name of one of the metric namespaces that is listed in a filter of a metric stream.

            :param namespace: The name of the metric namespace in the filter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_cloudwatch as cloudwatch
                
                metric_stream_filter_property = cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                    namespace="namespace"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "namespace": namespace,
            }

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The name of the metric namespace in the filter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStreamFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CfnMetricStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "firehose_arn": "firehoseArn",
        "output_format": "outputFormat",
        "role_arn": "roleArn",
        "exclude_filters": "excludeFilters",
        "include_filters": "includeFilters",
        "name": "name",
        "tags": "tags",
    },
)
class CfnMetricStreamProps:
    def __init__(
        self,
        *,
        firehose_arn: builtins.str,
        output_format: builtins.str,
        role_arn: builtins.str,
        exclude_filters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnMetricStream.MetricStreamFilterProperty, _IResolvable_a771d0ef]]]] = None,
        include_filters: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[CfnMetricStream.MetricStreamFilterProperty, _IResolvable_a771d0ef]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_95fbdc29]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMetricStream``.

        :param firehose_arn: The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream. This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.
        :param output_format: The output format for the stream. Valid values are ``json`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ . This parameter is required.
        :param role_arn: The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.
        :param exclude_filters: If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param include_filters: If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param name: If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region. If you are updating a metric stream, specify the name of that stream here.
        :param tags: An array of key-value pairs to apply to the metric stream. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            cfn_metric_stream_props = cloudwatch.CfnMetricStreamProps(
                firehose_arn="firehoseArn",
                output_format="outputFormat",
                role_arn="roleArn",
            
                # the properties below are optional
                exclude_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                    namespace="namespace"
                )],
                include_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                    namespace="namespace"
                )],
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "firehose_arn": firehose_arn,
            "output_format": output_format,
            "role_arn": role_arn,
        }
        if exclude_filters is not None:
            self._values["exclude_filters"] = exclude_filters
        if include_filters is not None:
            self._values["include_filters"] = include_filters
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firehose_arn(self) -> builtins.str:
        '''The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream.

        This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-firehosearn
        '''
        result = self._values.get("firehose_arn")
        assert result is not None, "Required property 'firehose_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_format(self) -> builtins.str:
        '''The output format for the stream.

        Valid values are ``json`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ .

        This parameter is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-outputformat
        '''
        result = self._values.get("output_format")
        assert result is not None, "Required property 'output_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources.

        This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMetricStream.MetricStreamFilterProperty, _IResolvable_a771d0ef]]]]:
        '''If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.

        You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream.

        When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-excludefilters
        '''
        result = self._values.get("exclude_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMetricStream.MetricStreamFilterProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def include_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMetricStream.MetricStreamFilterProperty, _IResolvable_a771d0ef]]]]:
        '''If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.

        You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream.

        When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includefilters
        '''
        result = self._values.get("include_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnMetricStream.MetricStreamFilterProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If you are creating a new metric stream, this is the name for the new stream.

        The name must be different than the names of other metric streams in this account and Region.

        If you are updating a metric stream, specify the name of that stream here.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''An array of key-value pairs to apply to the metric stream.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMetricStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Color(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_cloudwatch.Color"):
    '''(experimental) A set of standard colours that can be used in annotations in a GraphWidget.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        # execution_count_metric is of type Metric
        # error_count_metric is of type Metric
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            title="Executions vs error rate",
        
            left=[execution_count_metric],
        
            right=[error_count_metric.with(
                statistic="average",
                label="Error rate",
                color=cloudwatch.Color.GREEN
            )]
        ))
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="BLUE")
    def BLUE(cls) -> builtins.str:
        '''(experimental) blue - hex #1f77b4.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BLUE"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="BROWN")
    def BROWN(cls) -> builtins.str:
        '''(experimental) brown - hex #8c564b.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BROWN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GREEN")
    def GREEN(cls) -> builtins.str:
        '''(experimental) green - hex #2ca02c.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GREEN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GREY")
    def GREY(cls) -> builtins.str:
        '''(experimental) grey - hex #7f7f7f.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GREY"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="ORANGE")
    def ORANGE(cls) -> builtins.str:
        '''(experimental) orange - hex #ff7f0e.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ORANGE"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="PINK")
    def PINK(cls) -> builtins.str:
        '''(experimental) pink - hex #e377c2.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PINK"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="PURPLE")
    def PURPLE(cls) -> builtins.str:
        '''(experimental) purple - hex #9467bd.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PURPLE"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="RED")
    def RED(cls) -> builtins.str:
        '''(experimental) red - hex #d62728.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RED"))


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CommonMetricOptions",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions": "dimensions",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class CommonMetricOptions:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''(experimental) Options shared by most methods accepting metric options.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_cloudwatch as cloudwatch
            
            # dimensions is of type object
            # duration is of type Duration
            
            common_metric_options = cloudwatch.CommonMetricOptions(
                account="account",
                color="color",
                dimensions={
                    "dimensions_key": dimensions
                },
                dimensions_map={
                    "dimensions_map_key": "dimensionsMap"
                },
                label="label",
                period=duration,
                region="region",
                statistic="statistic",
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account which this metric comes from.

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) Dimensions of the metric.

        :default: - No dimensions.

        :deprecated: Use 'dimensionsMap' instead.

        :stability: deprecated
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Dimensions of the metric.

        :default: - No dimensions.

        :stability: experimental
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :default: - No label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The period over which the specified statistic is applied.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region which this metric comes from.

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(experimental) What function to use for aggregating.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"

        :default: Average

        :stability: experimental
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''(experimental) Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonMetricOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.ComparisonOperator")
class ComparisonOperator(enum.Enum):
    '''(experimental) Comparison operator for evaluating alarms.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as cloudwatch
        
        # alias is of type Alias
        
        # or add alarms to an existing group
        # blue_green_alias is of type Alias
        
        alarm = cloudwatch.Alarm(self, "Errors",
            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
            threshold=1,
            evaluation_periods=1,
            metric=alias.metric_errors()
        )
        deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
            alias=alias,
            deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE,
            alarms=[alarm
            ]
        )
        deployment_group.add_alarm(cloudwatch.Alarm(self, "BlueGreenErrors",
            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
            threshold=1,
            evaluation_periods=1,
            metric=blue_green_alias.metric_errors()
        ))
    '''

    GREATER_THAN_OR_EQUAL_TO_THRESHOLD = "GREATER_THAN_OR_EQUAL_TO_THRESHOLD"
    '''(experimental) Specified statistic is greater than or equal to the threshold.

    :stability: experimental
    '''
    GREATER_THAN_THRESHOLD = "GREATER_THAN_THRESHOLD"
    '''(experimental) Specified statistic is strictly greater than the threshold.

    :stability: experimental
    '''
    LESS_THAN_THRESHOLD = "LESS_THAN_THRESHOLD"
    '''(experimental) Specified statistic is strictly less than the threshold.

    :stability: experimental
    '''
    LESS_THAN_OR_EQUAL_TO_THRESHOLD = "LESS_THAN_OR_EQUAL_TO_THRESHOLD"
    '''(experimental) Specified statistic is less than or equal to the threshold.

    :stability: experimental
    '''
    LESS_THAN_LOWER_OR_GREATER_THAN_UPPER_THRESHOLD = "LESS_THAN_LOWER_OR_GREATER_THAN_UPPER_THRESHOLD"
    '''(experimental) Specified statistic is lower than or greater than the anomaly model band.

    Used only for alarms based on anomaly detection models

    :stability: experimental
    '''
    GREATER_THAN_UPPER_THRESHOLD = "GREATER_THAN_UPPER_THRESHOLD"
    '''(experimental) Specified statistic is greater than the anomaly model band.

    Used only for alarms based on anomaly detection models

    :stability: experimental
    '''
    LESS_THAN_LOWER_THRESHOLD = "LESS_THAN_LOWER_THRESHOLD"
    '''(experimental) Specified statistic is lower than the anomaly model band.

    Used only for alarms based on anomaly detection models

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CompositeAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_rule": "alarmRule",
        "actions_enabled": "actionsEnabled",
        "alarm_description": "alarmDescription",
        "composite_alarm_name": "compositeAlarmName",
    },
)
class CompositeAlarmProps:
    def __init__(
        self,
        *,
        alarm_rule: "IAlarmRule",
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        composite_alarm_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for creating a Composite Alarm.

        :param alarm_rule: (experimental) Expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param composite_alarm_name: (experimental) Name of the alarm. Default: Automatically generated name

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # alarm1 is of type Alarm
            # alarm2 is of type Alarm
            # alarm3 is of type Alarm
            # alarm4 is of type Alarm
            
            
            alarm_rule = cloudwatch.AlarmRule.any_of(
                cloudwatch.AlarmRule.all_of(
                    cloudwatch.AlarmRule.any_of(alarm1,
                        cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                    cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
                cloudwatch.AlarmRule.from_boolean(False))
            
            cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
                alarm_rule=alarm_rule
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "alarm_rule": alarm_rule,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if composite_alarm_name is not None:
            self._values["composite_alarm_name"] = composite_alarm_name

    @builtins.property
    def alarm_rule(self) -> "IAlarmRule":
        '''(experimental) Expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.

        :stability: experimental
        '''
        result = self._values.get("alarm_rule")
        assert result is not None, "Required property 'alarm_rule' is missing"
        return typing.cast("IAlarmRule", result)

    @builtins.property
    def actions_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the actions for this alarm are enabled.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for the alarm.

        :default: No description

        :stability: experimental
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def composite_alarm_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the alarm.

        :default: Automatically generated name

        :stability: experimental
        '''
        result = self._values.get("composite_alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.CreateAlarmOptions",
    jsii_struct_bases=[],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "threshold": "threshold",
        "actions_enabled": "actionsEnabled",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "comparison_operator": "comparisonOperator",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluate_low_sample_count_percentile": "evaluateLowSampleCountPercentile",
        "period": "period",
        "statistic": "statistic",
        "treat_missing_data": "treatMissingData",
    },
)
class CreateAlarmOptions:
    def __init__(
        self,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        statistic: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional["TreatMissingData"] = None,
    ) -> None:
        '''(experimental) Properties needed to make an alarm from a metric.

        :param evaluation_periods: (experimental) The number of periods over which data is compared to the specified threshold.
        :param threshold: (experimental) The value against which the specified statistic is compared.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param alarm_name: (experimental) Name of the alarm. Default: Automatically generated name
        :param comparison_operator: (experimental) Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: (experimental) The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: (experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param period: (deprecated) The period over which the specified statistic is applied. Cannot be used with ``MathExpression`` objects. Default: - The period from the metric
        :param statistic: (deprecated) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Cannot be used with ``MathExpression`` objects. Default: - The statistic from the metric
        :param treat_missing_data: (experimental) Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # fn is of type Function
            
            
            fn.metric_errors().create_alarm(self, "Alarm",
                threshold=100,
                evaluation_periods=2
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "evaluation_periods": evaluation_periods,
            "threshold": threshold,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if comparison_operator is not None:
            self._values["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluate_low_sample_count_percentile is not None:
            self._values["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''(experimental) The number of periods over which data is compared to the specified threshold.

        :stability: experimental
        '''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''(experimental) The value against which the specified statistic is compared.

        :stability: experimental
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the actions for this alarm are enabled.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for the alarm.

        :default: No description

        :stability: experimental
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the alarm.

        :default: Automatically generated name

        :stability: experimental
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comparison_operator(self) -> typing.Optional[ComparisonOperator]:
        '''(experimental) Comparison to use to check if metric is breaching.

        :default: GreaterThanOrEqualToThreshold

        :stability: experimental
        '''
        result = self._values.get("comparison_operator")
        return typing.cast(typing.Optional[ComparisonOperator], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M
        out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon
        CloudWatch User Guide.

        :default: ``evaluationPeriods``

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation
        :stability: experimental
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''(experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant.

        Used only for alarms that are based on percentiles.

        :default: - Not configured.

        :stability: experimental
        '''
        result = self._values.get("evaluate_low_sample_count_percentile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(deprecated) The period over which the specified statistic is applied.

        Cannot be used with ``MathExpression`` objects.

        :default: - The period from the metric

        :deprecated: Use ``metric.with({ period: ... })`` to encode the period into the Metric object

        :stability: deprecated
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(deprecated) What function to use for aggregating.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"

        Cannot be used with ``MathExpression`` objects.

        :default: - The statistic from the metric

        :deprecated: Use ``metric.with({ statistic: ... })`` to encode the period into the Metric object

        :stability: deprecated
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional["TreatMissingData"]:
        '''(experimental) Sets how this alarm is to handle missing data points.

        :default: TreatMissingData.Missing

        :stability: experimental
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional["TreatMissingData"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateAlarmOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Dashboard(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.Dashboard",
):
    '''(experimental) A CloudWatch dashboard.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        # widget is of type IWidget
        
        dashboard = cloudwatch.Dashboard(self, "MyDashboard",
            dashboard_name="dashboardName",
            end="end",
            period_override=cloudwatch.PeriodOverride.AUTO,
            start="start",
            widgets=[[widget]]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dashboard_name: typing.Optional[builtins.str] = None,
        end: typing.Optional[builtins.str] = None,
        period_override: typing.Optional["PeriodOverride"] = None,
        start: typing.Optional[builtins.str] = None,
        widgets: typing.Optional[typing.Sequence[typing.Sequence["IWidget"]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dashboard_name: (experimental) Name of the dashboard. If set, must only contain alphanumerics, dash (-) and underscore (_) Default: - automatically generated name
        :param end: (experimental) The end of the time range to use for each widget on the dashboard when the dashboard loads. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param period_override: (experimental) Use this field to specify the period for the graphs when the dashboard loads. Specifying ``Auto`` causes the period of all graphs on the dashboard to automatically adapt to the time range of the dashboard. Specifying ``Inherit`` ensures that the period set for each graph is always obeyed. Default: Auto
        :param start: (experimental) The start of the time range to use for each widget on the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param widgets: (experimental) Initial set of widgets on the dashboard. One array represents a row of widgets. Default: - No widgets

        :stability: experimental
        '''
        props = DashboardProps(
            dashboard_name=dashboard_name,
            end=end,
            period_override=period_override,
            start=start,
            widgets=widgets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addWidgets")
    def add_widgets(self, *widgets: "IWidget") -> None:
        '''(experimental) Add a widget to the dashboard.

        Widgets given in multiple calls to add() will be laid out stacked on
        top of each other.

        Multiple widgets added in the same call to add() will be laid out next
        to each other.

        :param widgets: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addWidgets", [*widgets]))


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.DashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_name": "dashboardName",
        "end": "end",
        "period_override": "periodOverride",
        "start": "start",
        "widgets": "widgets",
    },
)
class DashboardProps:
    def __init__(
        self,
        *,
        dashboard_name: typing.Optional[builtins.str] = None,
        end: typing.Optional[builtins.str] = None,
        period_override: typing.Optional["PeriodOverride"] = None,
        start: typing.Optional[builtins.str] = None,
        widgets: typing.Optional[typing.Sequence[typing.Sequence["IWidget"]]] = None,
    ) -> None:
        '''(experimental) Properties for defining a CloudWatch Dashboard.

        :param dashboard_name: (experimental) Name of the dashboard. If set, must only contain alphanumerics, dash (-) and underscore (_) Default: - automatically generated name
        :param end: (experimental) The end of the time range to use for each widget on the dashboard when the dashboard loads. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param period_override: (experimental) Use this field to specify the period for the graphs when the dashboard loads. Specifying ``Auto`` causes the period of all graphs on the dashboard to automatically adapt to the time range of the dashboard. Specifying ``Inherit`` ensures that the period set for each graph is always obeyed. Default: Auto
        :param start: (experimental) The start of the time range to use for each widget on the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param widgets: (experimental) Initial set of widgets on the dashboard. One array represents a row of widgets. Default: - No widgets

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            # widget is of type IWidget
            
            dashboard_props = cloudwatch.DashboardProps(
                dashboard_name="dashboardName",
                end="end",
                period_override=cloudwatch.PeriodOverride.AUTO,
                start="start",
                widgets=[[widget]]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if dashboard_name is not None:
            self._values["dashboard_name"] = dashboard_name
        if end is not None:
            self._values["end"] = end
        if period_override is not None:
            self._values["period_override"] = period_override
        if start is not None:
            self._values["start"] = start
        if widgets is not None:
            self._values["widgets"] = widgets

    @builtins.property
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the dashboard.

        If set, must only contain alphanumerics, dash (-) and underscore (_)

        :default: - automatically generated name

        :stability: experimental
        '''
        result = self._values.get("dashboard_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end(self) -> typing.Optional[builtins.str]:
        '''(experimental) The end of the time range to use for each widget on the dashboard when the dashboard loads.

        If you specify a value for end, you must also specify a value for start.
        Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the end date will be the current time.

        :stability: experimental
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period_override(self) -> typing.Optional["PeriodOverride"]:
        '''(experimental) Use this field to specify the period for the graphs when the dashboard loads.

        Specifying ``Auto`` causes the period of all graphs on the dashboard to automatically adapt to the time range of the dashboard.
        Specifying ``Inherit`` ensures that the period set for each graph is always obeyed.

        :default: Auto

        :stability: experimental
        '''
        result = self._values.get("period_override")
        return typing.cast(typing.Optional["PeriodOverride"], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.str]:
        '''(experimental) The start of the time range to use for each widget on the dashboard.

        You can specify start without specifying end to specify a relative time range that ends with the current time.
        In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for
        minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months.
        You can also use start along with an end field, to specify an absolute time range.
        When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the start time will be the default time range.

        :stability: experimental
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def widgets(self) -> typing.Optional[typing.List[typing.List["IWidget"]]]:
        '''(experimental) Initial set of widgets on the dashboard.

        One array represents a row of widgets.

        :default: - No widgets

        :stability: experimental
        '''
        result = self._values.get("widgets")
        return typing.cast(typing.Optional[typing.List[typing.List["IWidget"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.Dimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Dimension:
    def __init__(self, *, name: builtins.str, value: typing.Any) -> None:
        '''(experimental) Metric dimension.

        :param name: (experimental) Name of the dimension.
        :param value: (experimental) Value of the dimension.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html
        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            # value is of type object
            
            dimension = cloudwatch.Dimension(
                name="name",
                value=value
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) Name of the dimension.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Any:
        '''(experimental) Value of the dimension.

        :stability: experimental
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Dimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.GraphWidgetView")
class GraphWidgetView(enum.Enum):
    '''(experimental) Types of view.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            view=cloudwatch.GraphWidgetView.BAR
        ))
    '''

    TIME_SERIES = "TIME_SERIES"
    '''(experimental) Display as a line graph.

    :stability: experimental
    '''
    BAR = "BAR"
    '''(experimental) Display as a bar graph.

    :stability: experimental
    '''
    PIE = "PIE"
    '''(experimental) Display as a pie graph.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.HorizontalAnnotation",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "color": "color",
        "fill": "fill",
        "label": "label",
        "visible": "visible",
    },
)
class HorizontalAnnotation:
    def __init__(
        self,
        *,
        value: jsii.Number,
        color: typing.Optional[builtins.str] = None,
        fill: typing.Optional["Shading"] = None,
        label: typing.Optional[builtins.str] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Horizontal annotation to be added to a graph.

        :param value: (experimental) The value of the annotation.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to be used for the annotation. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param fill: (experimental) Add shading above or below the annotation. Default: No shading
        :param label: (experimental) Label for the annotation. Default: - No label
        :param visible: (experimental) Whether the annotation is visible. Default: true

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            horizontal_annotation = cloudwatch.HorizontalAnnotation(
                value=123,
            
                # the properties below are optional
                color="color",
                fill=cloudwatch.Shading.NONE,
                label="label",
                visible=False
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if color is not None:
            self._values["color"] = color
        if fill is not None:
            self._values["fill"] = fill
        if label is not None:
            self._values["label"] = label
        if visible is not None:
            self._values["visible"] = visible

    @builtins.property
    def value(self) -> jsii.Number:
        '''(experimental) The value of the annotation.

        :stability: experimental
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to be used for the annotation. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fill(self) -> typing.Optional["Shading"]:
        '''(experimental) Add shading above or below the annotation.

        :default: No shading

        :stability: experimental
        '''
        result = self._values.get("fill")
        return typing.cast(typing.Optional["Shading"], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for the annotation.

        :default: - No label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visible(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the annotation is visible.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("visible")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalAnnotation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_cloudwatch.IAlarmAction")
class IAlarmAction(typing_extensions.Protocol):
    '''(experimental) Interface for objects that can be the targets of CloudWatch alarm actions.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_e78e779f, alarm: "IAlarm") -> AlarmActionConfig:
        '''(experimental) Return the properties required to send alarm actions to this CloudWatch alarm.

        :param scope: root Construct that allows creating new Constructs.
        :param alarm: CloudWatch alarm that the action will target.

        :stability: experimental
        '''
        ...


class _IAlarmActionProxy:
    '''(experimental) Interface for objects that can be the targets of CloudWatch alarm actions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_cloudwatch.IAlarmAction"

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_e78e779f, alarm: "IAlarm") -> AlarmActionConfig:
        '''(experimental) Return the properties required to send alarm actions to this CloudWatch alarm.

        :param scope: root Construct that allows creating new Constructs.
        :param alarm: CloudWatch alarm that the action will target.

        :stability: experimental
        '''
        return typing.cast(AlarmActionConfig, jsii.invoke(self, "bind", [scope, alarm]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmAction).__jsii_proxy_class__ = lambda : _IAlarmActionProxy


@jsii.interface(jsii_type="monocdk.aws_cloudwatch.IAlarmRule")
class IAlarmRule(typing_extensions.Protocol):
    '''(experimental) Interface for Alarm Rule.

    :stability: experimental
    '''

    @jsii.member(jsii_name="renderAlarmRule")
    def render_alarm_rule(self) -> builtins.str:
        '''(experimental) serialized representation of Alarm Rule to be used when building the Composite Alarm resource.

        :stability: experimental
        '''
        ...


class _IAlarmRuleProxy:
    '''(experimental) Interface for Alarm Rule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_cloudwatch.IAlarmRule"

    @jsii.member(jsii_name="renderAlarmRule")
    def render_alarm_rule(self) -> builtins.str:
        '''(experimental) serialized representation of Alarm Rule to be used when building the Composite Alarm resource.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderAlarmRule", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmRule).__jsii_proxy_class__ = lambda : _IAlarmRuleProxy


@jsii.interface(jsii_type="monocdk.aws_cloudwatch.IMetric")
class IMetric(typing_extensions.Protocol):
    '''(experimental) Interface for metrics.

    :stability: experimental
    '''

    @jsii.member(jsii_name="toAlarmConfig")
    def to_alarm_config(self) -> "MetricAlarmConfig":
        '''(deprecated) Turn this metric object into an alarm configuration.

        :deprecated: Use ``toMetricConfig()`` instead.

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="toGraphConfig")
    def to_graph_config(self) -> "MetricGraphConfig":
        '''(deprecated) Turn this metric object into a graph configuration.

        :deprecated: Use ``toMetricConfig()`` instead.

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''(experimental) Inspect the details of the metric object.

        :stability: experimental
        '''
        ...


class _IMetricProxy:
    '''(experimental) Interface for metrics.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_cloudwatch.IMetric"

    @jsii.member(jsii_name="toAlarmConfig")
    def to_alarm_config(self) -> "MetricAlarmConfig":
        '''(deprecated) Turn this metric object into an alarm configuration.

        :deprecated: Use ``toMetricConfig()`` instead.

        :stability: deprecated
        '''
        return typing.cast("MetricAlarmConfig", jsii.invoke(self, "toAlarmConfig", []))

    @jsii.member(jsii_name="toGraphConfig")
    def to_graph_config(self) -> "MetricGraphConfig":
        '''(deprecated) Turn this metric object into a graph configuration.

        :deprecated: Use ``toMetricConfig()`` instead.

        :stability: deprecated
        '''
        return typing.cast("MetricGraphConfig", jsii.invoke(self, "toGraphConfig", []))

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''(experimental) Inspect the details of the metric object.

        :stability: experimental
        '''
        return typing.cast("MetricConfig", jsii.invoke(self, "toMetricConfig", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMetric).__jsii_proxy_class__ = lambda : _IMetricProxy


@jsii.interface(jsii_type="monocdk.aws_cloudwatch.IWidget")
class IWidget(typing_extensions.Protocol):
    '''(experimental) A single dashboard widget.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''(experimental) The amount of vertical grid units the widget will take up.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''(experimental) The amount of horizontal grid units the widget will take up.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        ...


class _IWidgetProxy:
    '''(experimental) A single dashboard widget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_cloudwatch.IWidget"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''(experimental) The amount of vertical grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''(experimental) The amount of horizontal grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWidget).__jsii_proxy_class__ = lambda : _IWidgetProxy


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.LegendPosition")
class LegendPosition(enum.Enum):
    '''(experimental) The position of the legend on a GraphWidget.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            legend_position=cloudwatch.LegendPosition.RIGHT
        ))
    '''

    BOTTOM = "BOTTOM"
    '''(experimental) Legend appears below the graph (default).

    :stability: experimental
    '''
    RIGHT = "RIGHT"
    '''(experimental) Add shading above the annotation.

    :stability: experimental
    '''
    HIDDEN = "HIDDEN"
    '''(experimental) Add shading below the annotation.

    :stability: experimental
    '''


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.LogQueryVisualizationType")
class LogQueryVisualizationType(enum.Enum):
    '''(experimental) Types of view.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        
        
        dashboard.add_widgets(cloudwatch.LogQueryWidget(
            log_group_names=["my-log-group"],
            view=cloudwatch.LogQueryVisualizationType.TABLE,
            # The lines will be automatically combined using '\n|'.
            query_lines=["fields @message", "filter @message like /Error/"
            ]
        ))
    '''

    TABLE = "TABLE"
    '''(experimental) Table view.

    :stability: experimental
    '''
    LINE = "LINE"
    '''(experimental) Line view.

    :stability: experimental
    '''
    STACKEDAREA = "STACKEDAREA"
    '''(experimental) Stacked area view.

    :stability: experimental
    '''
    BAR = "BAR"
    '''(experimental) Bar view.

    :stability: experimental
    '''
    PIE = "PIE"
    '''(experimental) Pie view.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.LogQueryWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_names": "logGroupNames",
        "height": "height",
        "query_lines": "queryLines",
        "query_string": "queryString",
        "region": "region",
        "title": "title",
        "view": "view",
        "width": "width",
    },
)
class LogQueryWidgetProps:
    def __init__(
        self,
        *,
        log_group_names: typing.Sequence[builtins.str],
        height: typing.Optional[jsii.Number] = None,
        query_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        view: typing.Optional[LogQueryVisualizationType] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for a Query widget.

        :param log_group_names: (experimental) Names of log groups to query.
        :param height: (experimental) Height of the widget. Default: 6
        :param query_lines: (experimental) A sequence of lines to use to build the query. The query will be built by joining the lines together using ``\\n|``. Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param query_string: (experimental) Full query string for log insights. Be sure to prepend every new line with a newline and pipe character (``\\n|``). Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param region: (experimental) The region the metrics of this widget should be taken from. Default: Current region
        :param title: (experimental) Title for the widget. Default: No title
        :param view: (experimental) The type of view to use. Default: LogQueryVisualizationType.TABLE
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # dashboard is of type Dashboard
            
            
            dashboard.add_widgets(cloudwatch.LogQueryWidget(
                log_group_names=["my-log-group"],
                view=cloudwatch.LogQueryVisualizationType.TABLE,
                # The lines will be automatically combined using '\n|'.
                query_lines=["fields @message", "filter @message like /Error/"
                ]
            ))
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "log_group_names": log_group_names,
        }
        if height is not None:
            self._values["height"] = height
        if query_lines is not None:
            self._values["query_lines"] = query_lines
        if query_string is not None:
            self._values["query_string"] = query_string
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if view is not None:
            self._values["view"] = view
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def log_group_names(self) -> typing.List[builtins.str]:
        '''(experimental) Names of log groups to query.

        :stability: experimental
        '''
        result = self._values.get("log_group_names")
        assert result is not None, "Required property 'log_group_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_lines(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A sequence of lines to use to build the query.

        The query will be built by joining the lines together using ``\\n|``.

        :default: - Exactly one of ``queryString``, ``queryLines`` is required.

        :stability: experimental
        '''
        result = self._values.get("query_lines")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''(experimental) Full query string for log insights.

        Be sure to prepend every new line with a newline and pipe character
        (``\\n|``).

        :default: - Exactly one of ``queryString``, ``queryLines`` is required.

        :stability: experimental
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region the metrics of this widget should be taken from.

        :default: Current region

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''(experimental) Title for the widget.

        :default: No title

        :stability: experimental
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional[LogQueryVisualizationType]:
        '''(experimental) The type of view to use.

        :default: LogQueryVisualizationType.TABLE

        :stability: experimental
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional[LogQueryVisualizationType], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogQueryWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IMetric)
class MathExpression(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.MathExpression",
):
    '''(experimental) A math expression built with metric(s) emitted by a service.

    The math expression is a combination of an expression (x+y) and metrics to apply expression on.
    It also contains metadata which is used only in graphs, such as color and label.
    It makes sense to embed this in here, so that compound constructs can attach
    that metadata to metrics they expose.

    MathExpression can also be used for search expressions. In this case,
    it also optionally accepts a searchRegion and searchAccount property for cross-environment
    search expressions.

    This class does not represent a resource, so hence is not a construct. Instead,
    MathExpression is an abstraction that makes it easy to specify metrics for use in both
    alarms and graphs.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # fn is of type Function
        
        
        all_problems = cloudwatch.MathExpression(
            expression="errors + throttles",
            using_metrics={
                "errors": fn.metric_errors(),
                "faults": fn.metric_throttles()
            }
        )
    '''

    def __init__(
        self,
        *,
        expression: builtins.str,
        using_metrics: typing.Optional[typing.Mapping[builtins.str, IMetric]] = None,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: (experimental) The expression defining the metric. When an expression contains a SEARCH function, it cannot be used within an Alarm.
        :param using_metrics: (experimental) The metrics used in the expression, in a map. The key is the identifier that represents the given metric in the expression, and the value is the actual Metric object. Default: - Empty map.
        :param color: (experimental) Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - Expression value is used as label
        :param period: (experimental) The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: (experimental) Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: (experimental) Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.

        :stability: experimental
        '''
        props = MathExpressionProps(
            expression=expression,
            using_metrics=using_metrics,
            color=color,
            label=label,
            period=period,
            search_account=search_account,
            search_region=search_region,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="createAlarm")
    def create_alarm(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        statistic: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional["TreatMissingData"] = None,
    ) -> "Alarm":
        '''(experimental) Make a new Alarm for this metric.

        Combines both properties that may adjust the metric (aggregation) as well
        as alarm properties.

        :param scope: -
        :param id: -
        :param evaluation_periods: (experimental) The number of periods over which data is compared to the specified threshold.
        :param threshold: (experimental) The value against which the specified statistic is compared.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param alarm_name: (experimental) Name of the alarm. Default: Automatically generated name
        :param comparison_operator: (experimental) Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: (experimental) The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: (experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param period: (deprecated) The period over which the specified statistic is applied. Cannot be used with ``MathExpression`` objects. Default: - The period from the metric
        :param statistic: (deprecated) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Cannot be used with ``MathExpression`` objects. Default: - The statistic from the metric
        :param treat_missing_data: (experimental) Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing

        :stability: experimental
        '''
        props = CreateAlarmOptions(
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            period=period,
            statistic=statistic,
            treat_missing_data=treat_missing_data,
        )

        return typing.cast("Alarm", jsii.invoke(self, "createAlarm", [scope, id, props]))

    @jsii.member(jsii_name="toAlarmConfig")
    def to_alarm_config(self) -> "MetricAlarmConfig":
        '''(deprecated) Turn this metric object into an alarm configuration.

        :deprecated: use toMetricConfig()

        :stability: deprecated
        '''
        return typing.cast("MetricAlarmConfig", jsii.invoke(self, "toAlarmConfig", []))

    @jsii.member(jsii_name="toGraphConfig")
    def to_graph_config(self) -> "MetricGraphConfig":
        '''(deprecated) Turn this metric object into a graph configuration.

        :deprecated: use toMetricConfig()

        :stability: deprecated
        '''
        return typing.cast("MetricGraphConfig", jsii.invoke(self, "toGraphConfig", []))

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''(experimental) Inspect the details of the metric object.

        :stability: experimental
        '''
        return typing.cast("MetricConfig", jsii.invoke(self, "toMetricConfig", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Returns a string representation of an object.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="with")
    def with_(
        self,
        *,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> "MathExpression":
        '''(experimental) Return a copy of Metric with properties changed.

        All properties except namespace and metricName can be changed.

        :param color: (experimental) Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - Expression value is used as label
        :param period: (experimental) The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: (experimental) Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: (experimental) Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.

        :stability: experimental
        '''
        props = MathExpressionOptions(
            color=color,
            label=label,
            period=period,
            search_account=search_account,
            search_region=search_region,
        )

        return typing.cast("MathExpression", jsii.invoke(self, "with", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        '''(experimental) The expression defining the metric.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="period")
    def period(self) -> _Duration_070aa057:
        '''(experimental) Aggregation period of this metric.

        :stability: experimental
        '''
        return typing.cast(_Duration_070aa057, jsii.get(self, "period"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="usingMetrics")
    def using_metrics(self) -> typing.Mapping[builtins.str, IMetric]:
        '''(experimental) The metrics used in the expression as KeyValuePair <id, metric>.

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, IMetric], jsii.get(self, "usingMetrics"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="color")
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "color"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="label")
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "label"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="searchAccount")
    def search_account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account to evaluate search expressions within.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchAccount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="searchRegion")
    def search_region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region to evaluate search expressions within.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchRegion"))


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MathExpressionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "color": "color",
        "label": "label",
        "period": "period",
        "search_account": "searchAccount",
        "search_region": "searchRegion",
    },
)
class MathExpressionOptions:
    def __init__(
        self,
        *,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Configurable options for MathExpressions.

        :param color: (experimental) Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - Expression value is used as label
        :param period: (experimental) The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: (experimental) Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: (experimental) Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_cloudwatch as cloudwatch
            
            # duration is of type Duration
            
            math_expression_options = cloudwatch.MathExpressionOptions(
                color="color",
                label="label",
                period=duration,
                search_account="searchAccount",
                search_region="searchRegion"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if color is not None:
            self._values["color"] = color
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if search_account is not None:
            self._values["search_account"] = search_account
        if search_region is not None:
            self._values["search_region"] = search_region

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) Color for this metric when added to a Graph in a Dashboard.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :default: - Expression value is used as label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The period over which the expression's statistics are applied.

        This period overrides all periods in the metrics used in this
        math expression.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def search_account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account to evaluate search expressions within.

        Specifying a searchAccount has no effect to the account used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("search_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region to evaluate search expressions within.

        Specifying a searchRegion has no effect to the region used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("search_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MathExpressionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MathExpressionProps",
    jsii_struct_bases=[MathExpressionOptions],
    name_mapping={
        "color": "color",
        "label": "label",
        "period": "period",
        "search_account": "searchAccount",
        "search_region": "searchRegion",
        "expression": "expression",
        "using_metrics": "usingMetrics",
    },
)
class MathExpressionProps(MathExpressionOptions):
    def __init__(
        self,
        *,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
        expression: builtins.str,
        using_metrics: typing.Optional[typing.Mapping[builtins.str, IMetric]] = None,
    ) -> None:
        '''(experimental) Properties for a MathExpression.

        :param color: (experimental) Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - Expression value is used as label
        :param period: (experimental) The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: (experimental) Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: (experimental) Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.
        :param expression: (experimental) The expression defining the metric. When an expression contains a SEARCH function, it cannot be used within an Alarm.
        :param using_metrics: (experimental) The metrics used in the expression, in a map. The key is the identifier that represents the given metric in the expression, and the value is the actual Metric object. Default: - Empty map.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # fn is of type Function
            
            
            all_problems = cloudwatch.MathExpression(
                expression="errors + throttles",
                using_metrics={
                    "errors": fn.metric_errors(),
                    "faults": fn.metric_throttles()
                }
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }
        if color is not None:
            self._values["color"] = color
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if search_account is not None:
            self._values["search_account"] = search_account
        if search_region is not None:
            self._values["search_region"] = search_region
        if using_metrics is not None:
            self._values["using_metrics"] = using_metrics

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) Color for this metric when added to a Graph in a Dashboard.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :default: - Expression value is used as label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The period over which the expression's statistics are applied.

        This period overrides all periods in the metrics used in this
        math expression.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def search_account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account to evaluate search expressions within.

        Specifying a searchAccount has no effect to the account used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("search_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region to evaluate search expressions within.

        Specifying a searchRegion has no effect to the region used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("search_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expression(self) -> builtins.str:
        '''(experimental) The expression defining the metric.

        When an expression contains a SEARCH function, it cannot be used
        within an Alarm.

        :stability: experimental
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def using_metrics(self) -> typing.Optional[typing.Mapping[builtins.str, IMetric]]:
        '''(experimental) The metrics used in the expression, in a map.

        The key is the identifier that represents the given metric in the
        expression, and the value is the actual Metric object.

        :default: - Empty map.

        :stability: experimental
        '''
        result = self._values.get("using_metrics")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, IMetric]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MathExpressionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IMetric)
class Metric(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_cloudwatch.Metric"):
    '''(experimental) A metric emitted by a service.

    The metric is a combination of a metric identifier (namespace, name and dimensions)
    and an aggregation function (statistic, period and unit).

    It also contains metadata which is used only in graphs, such as color and label.
    It makes sense to embed this in here, so that compound constructs can attach
    that metadata to metrics they expose.

    This class does not represent a resource, so hence is not a construct. Instead,
    Metric is an abstraction that makes it easy to specify metrics for use in both
    alarms and graphs.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # fn is of type Function
        
        
        minute_error_rate = fn.metric_errors(
            statistic="avg",
            period=Duration.minutes(1),
            label="Lambda failure rate"
        )
    '''

    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''
        :param metric_name: (experimental) Name of the metric.
        :param namespace: (experimental) Namespace of the metric.
        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = MetricProps(
            metric_name=metric_name,
            namespace=namespace,
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="grantPutMetricData") # type: ignore[misc]
    @builtins.classmethod
    def grant_put_metric_data(cls, grantee: _IGrantable_4c5a91d1) -> _Grant_bcb5eae7:
        '''(experimental) Grant permissions to the given identity to write metrics.

        :param grantee: The IAM identity to give permissions to.

        :stability: experimental
        '''
        return typing.cast(_Grant_bcb5eae7, jsii.sinvoke(cls, "grantPutMetricData", [grantee]))

    @jsii.member(jsii_name="attachTo")
    def attach_to(self, scope: constructs.IConstruct) -> "Metric":
        '''(experimental) Attach the metric object to the given construct scope.

        Returns a Metric object that uses the account and region from the Stack
        the given construct is defined in. If the metric is subsequently used
        in a Dashboard or Alarm in a different Stack defined in a different
        account or region, the appropriate 'region' and 'account' fields
        will be added to it.

        If the scope we attach to is in an environment-agnostic stack,
        nothing is done and the same Metric object is returned.

        :param scope: -

        :stability: experimental
        '''
        return typing.cast("Metric", jsii.invoke(self, "attachTo", [scope]))

    @jsii.member(jsii_name="createAlarm")
    def create_alarm(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        statistic: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional["TreatMissingData"] = None,
    ) -> "Alarm":
        '''(experimental) Make a new Alarm for this metric.

        Combines both properties that may adjust the metric (aggregation) as well
        as alarm properties.

        :param scope: -
        :param id: -
        :param evaluation_periods: (experimental) The number of periods over which data is compared to the specified threshold.
        :param threshold: (experimental) The value against which the specified statistic is compared.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param alarm_name: (experimental) Name of the alarm. Default: Automatically generated name
        :param comparison_operator: (experimental) Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: (experimental) The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: (experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param period: (deprecated) The period over which the specified statistic is applied. Cannot be used with ``MathExpression`` objects. Default: - The period from the metric
        :param statistic: (deprecated) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Cannot be used with ``MathExpression`` objects. Default: - The statistic from the metric
        :param treat_missing_data: (experimental) Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing

        :stability: experimental
        '''
        props = CreateAlarmOptions(
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            period=period,
            statistic=statistic,
            treat_missing_data=treat_missing_data,
        )

        return typing.cast("Alarm", jsii.invoke(self, "createAlarm", [scope, id, props]))

    @jsii.member(jsii_name="toAlarmConfig")
    def to_alarm_config(self) -> "MetricAlarmConfig":
        '''(deprecated) Turn this metric object into an alarm configuration.

        :deprecated: use toMetricConfig()

        :stability: deprecated
        '''
        return typing.cast("MetricAlarmConfig", jsii.invoke(self, "toAlarmConfig", []))

    @jsii.member(jsii_name="toGraphConfig")
    def to_graph_config(self) -> "MetricGraphConfig":
        '''(deprecated) Turn this metric object into a graph configuration.

        :deprecated: use toMetricConfig()

        :stability: deprecated
        '''
        return typing.cast("MetricGraphConfig", jsii.invoke(self, "toGraphConfig", []))

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''(experimental) Inspect the details of the metric object.

        :stability: experimental
        '''
        return typing.cast("MetricConfig", jsii.invoke(self, "toMetricConfig", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Returns a string representation of an object.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="with")
    def with_(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> "Metric":
        '''(experimental) Return a copy of Metric ``with`` properties changed.

        All properties except namespace and metricName can be changed.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast("Metric", jsii.invoke(self, "with", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''(experimental) Name of this metric.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        '''(experimental) Namespace of this metric.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="period")
    def period(self) -> _Duration_070aa057:
        '''(experimental) Period of this metric.

        :stability: experimental
        '''
        return typing.cast(_Duration_070aa057, jsii.get(self, "period"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        '''(experimental) Statistic of this metric.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account which this metric comes from.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="color")
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code used when this metric is rendered on a graph.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "color"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Dimensions of this metric.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "dimensions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="label")
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "label"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region which this metric comes from.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unit")
    def unit(self) -> typing.Optional["Unit"]:
        '''(experimental) Unit of the metric.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Unit"], jsii.get(self, "unit"))


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricAlarmConfig",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "period": "period",
        "dimensions": "dimensions",
        "extended_statistic": "extendedStatistic",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class MetricAlarmConfig:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        period: jsii.Number,
        dimensions: typing.Optional[typing.Sequence[Dimension]] = None,
        extended_statistic: typing.Optional[builtins.str] = None,
        statistic: typing.Optional["Statistic"] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''(deprecated) Properties used to construct the Metric identifying part of an Alarm.

        :param metric_name: (deprecated) Name of the metric.
        :param namespace: (deprecated) Namespace of the metric.
        :param period: (deprecated) How many seconds to aggregate over.
        :param dimensions: (deprecated) The dimensions to apply to the alarm.
        :param extended_statistic: (deprecated) Percentile aggregation function to use.
        :param statistic: (deprecated) Simple aggregation function to use.
        :param unit: (deprecated) The unit of the alarm.

        :deprecated: Replaced by MetricConfig

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            # value is of type object
            
            metric_alarm_config = cloudwatch.MetricAlarmConfig(
                metric_name="metricName",
                namespace="namespace",
                period=123,
            
                # the properties below are optional
                dimensions=[cloudwatch.Dimension(
                    name="name",
                    value=value
                )],
                extended_statistic="extendedStatistic",
                statistic=cloudwatch.Statistic.SAMPLE_COUNT,
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "period": period,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if extended_statistic is not None:
            self._values["extended_statistic"] = extended_statistic
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''(deprecated) Name of the metric.

        :stability: deprecated
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''(deprecated) Namespace of the metric.

        :stability: deprecated
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> jsii.Number:
        '''(deprecated) How many seconds to aggregate over.

        :stability: deprecated
        '''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.List[Dimension]]:
        '''(deprecated) The dimensions to apply to the alarm.

        :stability: deprecated
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.List[Dimension]], result)

    @builtins.property
    def extended_statistic(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Percentile aggregation function to use.

        :stability: deprecated
        '''
        result = self._values.get("extended_statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional["Statistic"]:
        '''(deprecated) Simple aggregation function to use.

        :stability: deprecated
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional["Statistic"], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''(deprecated) The unit of the alarm.

        :stability: deprecated
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricAlarmConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricConfig",
    jsii_struct_bases=[],
    name_mapping={
        "math_expression": "mathExpression",
        "metric_stat": "metricStat",
        "rendering_properties": "renderingProperties",
    },
)
class MetricConfig:
    def __init__(
        self,
        *,
        math_expression: typing.Optional["MetricExpressionConfig"] = None,
        metric_stat: typing.Optional["MetricStatConfig"] = None,
        rendering_properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''(experimental) Properties of a rendered metric.

        :param math_expression: (experimental) In case the metric is a math expression, the details of the math expression. Default: - None
        :param metric_stat: (experimental) In case the metric represents a query, the details of the query. Default: - None
        :param rendering_properties: (experimental) Additional properties which will be rendered if the metric is used in a dashboard. Examples are 'label' and 'color', but any key in here will be added to dashboard graphs. Default: - None

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_cloudwatch as cloudwatch
            
            # duration is of type Duration
            # metric is of type Metric
            # rendering_properties is of type object
            # value is of type object
            
            metric_config = cloudwatch.MetricConfig(
                math_expression=cloudwatch.MetricExpressionConfig(
                    expression="expression",
                    period=123,
                    using_metrics={
                        "using_metrics_key": metric
                    },
            
                    # the properties below are optional
                    search_account="searchAccount",
                    search_region="searchRegion"
                ),
                metric_stat=cloudwatch.MetricStatConfig(
                    metric_name="metricName",
                    namespace="namespace",
                    period=duration,
                    statistic="statistic",
            
                    # the properties below are optional
                    account="account",
                    dimensions=[cloudwatch.Dimension(
                        name="name",
                        value=value
                    )],
                    region="region",
                    unit_filter=cloudwatch.Unit.SECONDS
                ),
                rendering_properties={
                    "rendering_properties_key": rendering_properties
                }
            )
        '''
        if isinstance(math_expression, dict):
            math_expression = MetricExpressionConfig(**math_expression)
        if isinstance(metric_stat, dict):
            metric_stat = MetricStatConfig(**metric_stat)
        self._values: typing.Dict[str, typing.Any] = {}
        if math_expression is not None:
            self._values["math_expression"] = math_expression
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if rendering_properties is not None:
            self._values["rendering_properties"] = rendering_properties

    @builtins.property
    def math_expression(self) -> typing.Optional["MetricExpressionConfig"]:
        '''(experimental) In case the metric is a math expression, the details of the math expression.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("math_expression")
        return typing.cast(typing.Optional["MetricExpressionConfig"], result)

    @builtins.property
    def metric_stat(self) -> typing.Optional["MetricStatConfig"]:
        '''(experimental) In case the metric represents a query, the details of the query.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["MetricStatConfig"], result)

    @builtins.property
    def rendering_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Additional properties which will be rendered if the metric is used in a dashboard.

        Examples are 'label' and 'color', but any key in here will be
        added to dashboard graphs.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("rendering_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricExpressionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "period": "period",
        "using_metrics": "usingMetrics",
        "search_account": "searchAccount",
        "search_region": "searchRegion",
    },
)
class MetricExpressionConfig:
    def __init__(
        self,
        *,
        expression: builtins.str,
        period: jsii.Number,
        using_metrics: typing.Mapping[builtins.str, IMetric],
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for a concrete metric.

        :param expression: (experimental) Math expression for the metric.
        :param period: (experimental) How many seconds to aggregate over.
        :param using_metrics: (experimental) Metrics used in the math expression.
        :param search_account: (experimental) Account to evaluate search expressions within. Default: - Deployment account.
        :param search_region: (experimental) Region to evaluate search expressions within. Default: - Deployment region.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            # metric is of type Metric
            
            metric_expression_config = cloudwatch.MetricExpressionConfig(
                expression="expression",
                period=123,
                using_metrics={
                    "using_metrics_key": metric
                },
            
                # the properties below are optional
                search_account="searchAccount",
                search_region="searchRegion"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "period": period,
            "using_metrics": using_metrics,
        }
        if search_account is not None:
            self._values["search_account"] = search_account
        if search_region is not None:
            self._values["search_region"] = search_region

    @builtins.property
    def expression(self) -> builtins.str:
        '''(experimental) Math expression for the metric.

        :stability: experimental
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> jsii.Number:
        '''(experimental) How many seconds to aggregate over.

        :stability: experimental
        '''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def using_metrics(self) -> typing.Mapping[builtins.str, IMetric]:
        '''(experimental) Metrics used in the math expression.

        :stability: experimental
        '''
        result = self._values.get("using_metrics")
        assert result is not None, "Required property 'using_metrics' is missing"
        return typing.cast(typing.Mapping[builtins.str, IMetric], result)

    @builtins.property
    def search_account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account to evaluate search expressions within.

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("search_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region to evaluate search expressions within.

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("search_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricExpressionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricGraphConfig",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "period": "period",
        "rendering_properties": "renderingProperties",
        "color": "color",
        "dimensions": "dimensions",
        "label": "label",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class MetricGraphConfig:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        period: jsii.Number,
        rendering_properties: "MetricRenderingProperties",
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Sequence[Dimension]] = None,
        label: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''(deprecated) Properties used to construct the Metric identifying part of a Graph.

        :param metric_name: (deprecated) Name of the metric.
        :param namespace: (deprecated) Namespace of the metric.
        :param period: (deprecated) How many seconds to aggregate over.
        :param rendering_properties: (deprecated) Rendering properties override yAxis parameter of the widget object.
        :param color: (deprecated) Color for the graph line.
        :param dimensions: (deprecated) The dimensions to apply to the alarm.
        :param label: (deprecated) Label for the metric.
        :param statistic: (deprecated) Aggregation function to use (can be either simple or a percentile).
        :param unit: (deprecated) The unit of the alarm.

        :deprecated: Replaced by MetricConfig

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            # value is of type object
            
            metric_graph_config = cloudwatch.MetricGraphConfig(
                metric_name="metricName",
                namespace="namespace",
                period=123,
                rendering_properties=cloudwatch.MetricRenderingProperties(
                    period=123,
            
                    # the properties below are optional
                    color="color",
                    label="label",
                    stat="stat"
                ),
            
                # the properties below are optional
                color="color",
                dimensions=[cloudwatch.Dimension(
                    name="name",
                    value=value
                )],
                label="label",
                statistic="statistic",
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        if isinstance(rendering_properties, dict):
            rendering_properties = MetricRenderingProperties(**rendering_properties)
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "period": period,
            "rendering_properties": rendering_properties,
        }
        if color is not None:
            self._values["color"] = color
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if label is not None:
            self._values["label"] = label
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''(deprecated) Name of the metric.

        :stability: deprecated
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''(deprecated) Namespace of the metric.

        :stability: deprecated
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> jsii.Number:
        '''(deprecated) How many seconds to aggregate over.

        :deprecated: Use ``period`` in ``renderingProperties``

        :stability: deprecated
        '''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rendering_properties(self) -> "MetricRenderingProperties":
        '''(deprecated) Rendering properties override yAxis parameter of the widget object.

        :stability: deprecated
        '''
        result = self._values.get("rendering_properties")
        assert result is not None, "Required property 'rendering_properties' is missing"
        return typing.cast("MetricRenderingProperties", result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Color for the graph line.

        :deprecated: Use ``color`` in ``renderingProperties``

        :stability: deprecated
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.List[Dimension]]:
        '''(deprecated) The dimensions to apply to the alarm.

        :stability: deprecated
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.List[Dimension]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Label for the metric.

        :deprecated: Use ``label`` in ``renderingProperties``

        :stability: deprecated
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Aggregation function to use (can be either simple or a percentile).

        :deprecated: Use ``stat`` in ``renderingProperties``

        :stability: deprecated
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''(deprecated) The unit of the alarm.

        :deprecated: not used in dashboard widgets

        :stability: deprecated
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricGraphConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricOptions",
    jsii_struct_bases=[CommonMetricOptions],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions": "dimensions",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class MetricOptions(CommonMetricOptions):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''(experimental) Properties of a metric that can be changed.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import monocdk as cloudwatch
            # delivery_stream is of type DeliveryStream
            
            
            # Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
            incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
                expression="incomingBytes / 300 / bytePerSecLimit",
                using_metrics={
                    "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
                    "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
                }
            )
            
            cloudwatch.Alarm(self, "Alarm",
                metric=incoming_bytes_percent_of_limit,
                threshold=0.9,
                evaluation_periods=3
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account which this metric comes from.

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) Dimensions of the metric.

        :default: - No dimensions.

        :deprecated: Use 'dimensionsMap' instead.

        :stability: deprecated
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Dimensions of the metric.

        :default: - No dimensions.

        :stability: experimental
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :default: - No label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The period over which the specified statistic is applied.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region which this metric comes from.

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(experimental) What function to use for aggregating.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"

        :default: Average

        :stability: experimental
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''(experimental) Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricProps",
    jsii_struct_bases=[CommonMetricOptions],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions": "dimensions",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
        "metric_name": "metricName",
        "namespace": "namespace",
    },
)
class MetricProps(CommonMetricOptions):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
        metric_name: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''(experimental) Properties for a metric.

        :param account: (experimental) Account which this metric comes from. Default: - Deployment account.
        :param color: (experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: (experimental) Dimensions of the metric. Default: - No dimensions.
        :param label: (experimental) Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: (experimental) The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: (experimental) Region which this metric comes from. Default: - Deployment region.
        :param statistic: (experimental) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param metric_name: (experimental) Name of the metric.
        :param namespace: (experimental) Namespace of the metric.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            hosted_zone = route53.HostedZone(self, "MyHostedZone", zone_name="example.org")
            metric = cloudwatch.Metric(
                namespace="AWS/Route53",
                metric_name="DNSQueries",
                dimensions_map={
                    "HostedZoneId": hosted_zone.hosted_zone_id
                }
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account which this metric comes from.

        :default: - Deployment account.

        :stability: experimental
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(experimental) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color

        :stability: experimental
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) Dimensions of the metric.

        :default: - No dimensions.

        :deprecated: Use 'dimensionsMap' instead.

        :stability: deprecated
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Dimensions of the metric.

        :default: - No dimensions.

        :stability: experimental
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Label for this metric when added to a Graph in a Dashboard.

        :default: - No label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The period over which the specified statistic is applied.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region which this metric comes from.

        :default: - Deployment region.

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(experimental) What function to use for aggregating.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"

        :default: Average

        :stability: experimental
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''(experimental) Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''(experimental) Name of the metric.

        :stability: experimental
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''(experimental) Namespace of the metric.

        :stability: experimental
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricRenderingProperties",
    jsii_struct_bases=[],
    name_mapping={
        "period": "period",
        "color": "color",
        "label": "label",
        "stat": "stat",
    },
)
class MetricRenderingProperties:
    def __init__(
        self,
        *,
        period: jsii.Number,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        stat: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Custom rendering properties that override the default rendering properties specified in the yAxis parameter of the widget object.

        :param period: (deprecated) How many seconds to aggregate over.
        :param color: (deprecated) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.
        :param label: (deprecated) Label for the metric.
        :param stat: (deprecated) Aggregation function to use (can be either simple or a percentile).

        :deprecated: Replaced by MetricConfig.

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            metric_rendering_properties = cloudwatch.MetricRenderingProperties(
                period=123,
            
                # the properties below are optional
                color="color",
                label="label",
                stat="stat"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "period": period,
        }
        if color is not None:
            self._values["color"] = color
        if label is not None:
            self._values["label"] = label
        if stat is not None:
            self._values["stat"] = stat

    @builtins.property
    def period(self) -> jsii.Number:
        '''(deprecated) How many seconds to aggregate over.

        :stability: deprecated
        '''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :stability: deprecated
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Label for the metric.

        :stability: deprecated
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stat(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Aggregation function to use (can be either simple or a percentile).

        :stability: deprecated
        '''
        result = self._values.get("stat")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricRenderingProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricStatConfig",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "period": "period",
        "statistic": "statistic",
        "account": "account",
        "dimensions": "dimensions",
        "region": "region",
        "unit_filter": "unitFilter",
    },
)
class MetricStatConfig:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        period: _Duration_070aa057,
        statistic: builtins.str,
        account: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Sequence[Dimension]] = None,
        region: typing.Optional[builtins.str] = None,
        unit_filter: typing.Optional["Unit"] = None,
    ) -> None:
        '''(experimental) Properties for a concrete metric.

        NOTE: ``unit`` is no longer on this object since it is only used for ``Alarms``, and doesn't mean what one
        would expect it to mean there anyway. It is most likely to be misused.

        :param metric_name: (experimental) Name of the metric.
        :param namespace: (experimental) Namespace of the metric.
        :param period: (experimental) How many seconds to aggregate over.
        :param statistic: (experimental) Aggregation function to use (can be either simple or a percentile).
        :param account: (experimental) Account which this metric comes from. Default: Deployment account.
        :param dimensions: (experimental) The dimensions to apply to the alarm. Default: []
        :param region: (experimental) Region which this metric comes from. Default: Deployment region.
        :param unit_filter: (experimental) Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. This field has been renamed from plain ``unit`` to clearly communicate its purpose. Default: - Refer to all metric datums

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import monocdk as monocdk
            from monocdk import aws_cloudwatch as cloudwatch
            
            # duration is of type Duration
            # value is of type object
            
            metric_stat_config = cloudwatch.MetricStatConfig(
                metric_name="metricName",
                namespace="namespace",
                period=duration,
                statistic="statistic",
            
                # the properties below are optional
                account="account",
                dimensions=[cloudwatch.Dimension(
                    name="name",
                    value=value
                )],
                region="region",
                unit_filter=cloudwatch.Unit.SECONDS
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "period": period,
            "statistic": statistic,
        }
        if account is not None:
            self._values["account"] = account
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if region is not None:
            self._values["region"] = region
        if unit_filter is not None:
            self._values["unit_filter"] = unit_filter

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''(experimental) Name of the metric.

        :stability: experimental
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''(experimental) Namespace of the metric.

        :stability: experimental
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> _Duration_070aa057:
        '''(experimental) How many seconds to aggregate over.

        :stability: experimental
        '''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(_Duration_070aa057, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''(experimental) Aggregation function to use (can be either simple or a percentile).

        :stability: experimental
        '''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''(experimental) Account which this metric comes from.

        :default: Deployment account.

        :stability: experimental
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.List[Dimension]]:
        '''(experimental) The dimensions to apply to the alarm.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.List[Dimension]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) Region which this metric comes from.

        :default: Deployment region.

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit_filter(self) -> typing.Optional["Unit"]:
        '''(experimental) Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        This field has been renamed from plain ``unit`` to clearly communicate
        its purpose.

        :default: - Refer to all metric datums

        :stability: experimental
        '''
        result = self._values.get("unit_filter")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricStatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.MetricWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
    },
)
class MetricWidgetProps:
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Basic properties for widgets that display metrics.

        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            metric_widget_props = cloudwatch.MetricWidgetProps(
                height=123,
                region="region",
                title="title",
                width=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region the metrics of this graph should be taken from.

        :default: - Current region

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''(experimental) Title for the graph.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.PeriodOverride")
class PeriodOverride(enum.Enum):
    '''(experimental) Specify the period for graphs when the CloudWatch dashboard loads.

    :stability: experimental
    '''

    AUTO = "AUTO"
    '''(experimental) Period of all graphs on the dashboard automatically adapt to the time range of the dashboard.

    :stability: experimental
    '''
    INHERIT = "INHERIT"
    '''(experimental) Period set for each graph will be used.

    :stability: experimental
    '''


@jsii.implements(IWidget)
class Row(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_cloudwatch.Row"):
    '''(experimental) A widget that contains other widgets in a horizontal row.

    Widgets will be laid out next to each other

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        # widget is of type IWidget
        
        row = cloudwatch.Row(widget)
    '''

    def __init__(self, *widgets: IWidget) -> None:
        '''
        :param widgets: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [*widgets])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''(experimental) The amount of vertical grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''(experimental) The amount of horizontal grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "width"))


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.Shading")
class Shading(enum.Enum):
    '''(experimental) Fill shading options that will be used with an annotation.

    :stability: experimental
    '''

    NONE = "NONE"
    '''(experimental) Don't add shading.

    :stability: experimental
    '''
    ABOVE = "ABOVE"
    '''(experimental) Add shading above the annotation.

    :stability: experimental
    '''
    BELOW = "BELOW"
    '''(experimental) Add shading below the annotation.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.SingleValueWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "metrics": "metrics",
        "full_precision": "fullPrecision",
        "set_period_to_time_range": "setPeriodToTimeRange",
    },
)
class SingleValueWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        metrics: typing.Sequence[IMetric],
        full_precision: typing.Optional[builtins.bool] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Properties for a SingleValueWidget.

        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6
        :param metrics: (experimental) Metrics to display.
        :param full_precision: (experimental) Whether to show as many digits as can fit, before rounding. Default: false
        :param set_period_to_time_range: (experimental) Whether to show the value from the entire time range. Default: false

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # dashboard is of type Dashboard
            # visitor_count is of type Metric
            # purchase_count is of type Metric
            
            
            dashboard.add_widgets(cloudwatch.SingleValueWidget(
                metrics=[visitor_count, purchase_count]
            ))
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metrics": metrics,
        }
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if full_precision is not None:
            self._values["full_precision"] = full_precision
        if set_period_to_time_range is not None:
            self._values["set_period_to_time_range"] = set_period_to_time_range

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region the metrics of this graph should be taken from.

        :default: - Current region

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''(experimental) Title for the graph.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metrics(self) -> typing.List[IMetric]:
        '''(experimental) Metrics to display.

        :stability: experimental
        '''
        result = self._values.get("metrics")
        assert result is not None, "Required property 'metrics' is missing"
        return typing.cast(typing.List[IMetric], result)

    @builtins.property
    def full_precision(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to show as many digits as can fit, before rounding.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("full_precision")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def set_period_to_time_range(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to show the value from the entire time range.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("set_period_to_time_range")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SingleValueWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IWidget)
class Spacer(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_cloudwatch.Spacer"):
    '''(experimental) A widget that doesn't display anything but takes up space.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        spacer = cloudwatch.Spacer(
            height=123,
            width=123
        )
    '''

    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param height: (experimental) Height of the spacer. Default: : 1
        :param width: (experimental) Width of the spacer. Default: 1

        :stability: experimental
        '''
        props = SpacerProps(height=height, width=width)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="position")
    def position(self, _x: jsii.Number, _y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param _x: -
        :param _y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [_x, _y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''(experimental) The amount of vertical grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''(experimental) The amount of horizontal grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "width"))


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.SpacerProps",
    jsii_struct_bases=[],
    name_mapping={"height": "height", "width": "width"},
)
class SpacerProps:
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Props of the spacer.

        :param height: (experimental) Height of the spacer. Default: : 1
        :param width: (experimental) Width of the spacer. Default: 1

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            spacer_props = cloudwatch.SpacerProps(
                height=123,
                width=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the spacer.

        :default: : 1

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the spacer.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpacerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.Statistic")
class Statistic(enum.Enum):
    '''(experimental) Statistic to use over the aggregation period.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as cloudwatch
        # delivery_stream is of type DeliveryStream
        
        
        # Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
        incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
            expression="incomingBytes / 300 / bytePerSecLimit",
            using_metrics={
                "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
                "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
            }
        )
        
        cloudwatch.Alarm(self, "Alarm",
            metric=incoming_bytes_percent_of_limit,
            threshold=0.9,
            evaluation_periods=3
        )
    '''

    SAMPLE_COUNT = "SAMPLE_COUNT"
    '''(experimental) The count (number) of data points used for the statistical calculation.

    :stability: experimental
    '''
    AVERAGE = "AVERAGE"
    '''(experimental) The value of Sum / SampleCount during the specified period.

    :stability: experimental
    '''
    SUM = "SUM"
    '''(experimental) All values submitted for the matching metric added together.

    This statistic can be useful for determining the total volume of a metric.

    :stability: experimental
    '''
    MINIMUM = "MINIMUM"
    '''(experimental) The lowest value observed during the specified period.

    You can use this value to determine low volumes of activity for your application.

    :stability: experimental
    '''
    MAXIMUM = "MAXIMUM"
    '''(experimental) The highest value observed during the specified period.

    You can use this value to determine high volumes of activity for your application.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.TextWidgetProps",
    jsii_struct_bases=[],
    name_mapping={"markdown": "markdown", "height": "height", "width": "width"},
)
class TextWidgetProps:
    def __init__(
        self,
        *,
        markdown: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for a Text widget.

        :param markdown: (experimental) The text to display, in MarkDown format.
        :param height: (experimental) Height of the widget. Default: 2
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # dashboard is of type Dashboard
            
            
            dashboard.add_widgets(cloudwatch.TextWidget(
                markdown="# Key Performance Indicators"
            ))
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "markdown": markdown,
        }
        if height is not None:
            self._values["height"] = height
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def markdown(self) -> builtins.str:
        '''(experimental) The text to display, in MarkDown format.

        :stability: experimental
        '''
        result = self._values.get("markdown")
        assert result is not None, "Required property 'markdown' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default: 2

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.TreatMissingData")
class TreatMissingData(enum.Enum):
    '''(experimental) Specify how missing data points are treated during alarm evaluation.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as cdk
        import monocdk as cloudwatch
        
        
        fn = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_12_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
            timeout=cdk.Duration.minutes(5)
        )
        
        if fn.timeout:
            cloudwatch.Alarm(self, "MyAlarm",
                metric=fn.metric_duration().with(
                    statistic="Maximum"
                ),
                evaluation_periods=1,
                datapoints_to_alarm=1,
                threshold=fn.timeout.to_milliseconds(),
                treat_missing_data=cloudwatch.TreatMissingData.IGNORE,
                alarm_name="My Lambda Timeout"
            )
    '''

    BREACHING = "BREACHING"
    '''(experimental) Missing data points are treated as breaching the threshold.

    :stability: experimental
    '''
    NOT_BREACHING = "NOT_BREACHING"
    '''(experimental) Missing data points are treated as being within the threshold.

    :stability: experimental
    '''
    IGNORE = "IGNORE"
    '''(experimental) The current alarm state is maintained.

    :stability: experimental
    '''
    MISSING = "MISSING"
    '''(experimental) The alarm does not consider missing data points when evaluating whether to change state.

    :stability: experimental
    '''


@jsii.enum(jsii_type="monocdk.aws_cloudwatch.Unit")
class Unit(enum.Enum):
    '''(experimental) Unit for metric.

    :stability: experimental
    '''

    SECONDS = "SECONDS"
    '''(experimental) Seconds.

    :stability: experimental
    '''
    MICROSECONDS = "MICROSECONDS"
    '''(experimental) Microseconds.

    :stability: experimental
    '''
    MILLISECONDS = "MILLISECONDS"
    '''(experimental) Milliseconds.

    :stability: experimental
    '''
    BYTES = "BYTES"
    '''(experimental) Bytes.

    :stability: experimental
    '''
    KILOBYTES = "KILOBYTES"
    '''(experimental) Kilobytes.

    :stability: experimental
    '''
    MEGABYTES = "MEGABYTES"
    '''(experimental) Megabytes.

    :stability: experimental
    '''
    GIGABYTES = "GIGABYTES"
    '''(experimental) Gigabytes.

    :stability: experimental
    '''
    TERABYTES = "TERABYTES"
    '''(experimental) Terabytes.

    :stability: experimental
    '''
    BITS = "BITS"
    '''(experimental) Bits.

    :stability: experimental
    '''
    KILOBITS = "KILOBITS"
    '''(experimental) Kilobits.

    :stability: experimental
    '''
    MEGABITS = "MEGABITS"
    '''(experimental) Megabits.

    :stability: experimental
    '''
    GIGABITS = "GIGABITS"
    '''(experimental) Gigabits.

    :stability: experimental
    '''
    TERABITS = "TERABITS"
    '''(experimental) Terabits.

    :stability: experimental
    '''
    PERCENT = "PERCENT"
    '''(experimental) Percent.

    :stability: experimental
    '''
    COUNT = "COUNT"
    '''(experimental) Count.

    :stability: experimental
    '''
    BYTES_PER_SECOND = "BYTES_PER_SECOND"
    '''(experimental) Bytes/second (B/s).

    :stability: experimental
    '''
    KILOBYTES_PER_SECOND = "KILOBYTES_PER_SECOND"
    '''(experimental) Kilobytes/second (kB/s).

    :stability: experimental
    '''
    MEGABYTES_PER_SECOND = "MEGABYTES_PER_SECOND"
    '''(experimental) Megabytes/second (MB/s).

    :stability: experimental
    '''
    GIGABYTES_PER_SECOND = "GIGABYTES_PER_SECOND"
    '''(experimental) Gigabytes/second (GB/s).

    :stability: experimental
    '''
    TERABYTES_PER_SECOND = "TERABYTES_PER_SECOND"
    '''(experimental) Terabytes/second (TB/s).

    :stability: experimental
    '''
    BITS_PER_SECOND = "BITS_PER_SECOND"
    '''(experimental) Bits/second (b/s).

    :stability: experimental
    '''
    KILOBITS_PER_SECOND = "KILOBITS_PER_SECOND"
    '''(experimental) Kilobits/second (kb/s).

    :stability: experimental
    '''
    MEGABITS_PER_SECOND = "MEGABITS_PER_SECOND"
    '''(experimental) Megabits/second (Mb/s).

    :stability: experimental
    '''
    GIGABITS_PER_SECOND = "GIGABITS_PER_SECOND"
    '''(experimental) Gigabits/second (Gb/s).

    :stability: experimental
    '''
    TERABITS_PER_SECOND = "TERABITS_PER_SECOND"
    '''(experimental) Terabits/second (Tb/s).

    :stability: experimental
    '''
    COUNT_PER_SECOND = "COUNT_PER_SECOND"
    '''(experimental) Count/second.

    :stability: experimental
    '''
    NONE = "NONE"
    '''(experimental) No unit.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.YAxisProps",
    jsii_struct_bases=[],
    name_mapping={
        "label": "label",
        "max": "max",
        "min": "min",
        "show_units": "showUnits",
    },
)
class YAxisProps:
    def __init__(
        self,
        *,
        label: typing.Optional[builtins.str] = None,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
        show_units: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Properties for a Y-Axis.

        :param label: (experimental) The label. Default: - No label
        :param max: (experimental) The max value. Default: - No maximum value
        :param min: (experimental) The min value. Default: 0
        :param show_units: (experimental) Whether to show units. Default: true

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_cloudwatch as cloudwatch
            
            y_axis_props = cloudwatch.YAxisProps(
                label="label",
                max=123,
                min=123,
                show_units=False
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if label is not None:
            self._values["label"] = label
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min
        if show_units is not None:
            self._values["show_units"] = show_units

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) The label.

        :default: - No label

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The max value.

        :default: - No maximum value

        :stability: experimental
        '''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The min value.

        :default: 0

        :stability: experimental
        '''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def show_units(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to show units.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("show_units")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "YAxisProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.AlarmProps",
    jsii_struct_bases=[CreateAlarmOptions],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "threshold": "threshold",
        "actions_enabled": "actionsEnabled",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "comparison_operator": "comparisonOperator",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluate_low_sample_count_percentile": "evaluateLowSampleCountPercentile",
        "period": "period",
        "statistic": "statistic",
        "treat_missing_data": "treatMissingData",
        "metric": "metric",
    },
)
class AlarmProps(CreateAlarmOptions):
    def __init__(
        self,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        statistic: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[TreatMissingData] = None,
        metric: IMetric,
    ) -> None:
        '''(experimental) Properties for Alarms.

        :param evaluation_periods: (experimental) The number of periods over which data is compared to the specified threshold.
        :param threshold: (experimental) The value against which the specified statistic is compared.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param alarm_name: (experimental) Name of the alarm. Default: Automatically generated name
        :param comparison_operator: (experimental) Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: (experimental) The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: (experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param period: (deprecated) The period over which the specified statistic is applied. Cannot be used with ``MathExpression`` objects. Default: - The period from the metric
        :param statistic: (deprecated) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Cannot be used with ``MathExpression`` objects. Default: - The statistic from the metric
        :param treat_missing_data: (experimental) Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing
        :param metric: (experimental) The metric to add the alarm on. Metric objects can be obtained from most resources, or you can construct custom Metric objects by instantiating one.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import monocdk as cloudwatch
            # delivery_stream is of type DeliveryStream
            
            
            # Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
            incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
                expression="incomingBytes / 300 / bytePerSecLimit",
                using_metrics={
                    "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
                    "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
                }
            )
            
            cloudwatch.Alarm(self, "Alarm",
                metric=incoming_bytes_percent_of_limit,
                threshold=0.9,
                evaluation_periods=3
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "evaluation_periods": evaluation_periods,
            "threshold": threshold,
            "metric": metric,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if comparison_operator is not None:
            self._values["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluate_low_sample_count_percentile is not None:
            self._values["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''(experimental) The number of periods over which data is compared to the specified threshold.

        :stability: experimental
        '''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''(experimental) The value against which the specified statistic is compared.

        :stability: experimental
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the actions for this alarm are enabled.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for the alarm.

        :default: No description

        :stability: experimental
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the alarm.

        :default: Automatically generated name

        :stability: experimental
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comparison_operator(self) -> typing.Optional[ComparisonOperator]:
        '''(experimental) Comparison to use to check if metric is breaching.

        :default: GreaterThanOrEqualToThreshold

        :stability: experimental
        '''
        result = self._values.get("comparison_operator")
        return typing.cast(typing.Optional[ComparisonOperator], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M
        out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon
        CloudWatch User Guide.

        :default: ``evaluationPeriods``

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation
        :stability: experimental
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''(experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant.

        Used only for alarms that are based on percentiles.

        :default: - Not configured.

        :stability: experimental
        '''
        result = self._values.get("evaluate_low_sample_count_percentile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(deprecated) The period over which the specified statistic is applied.

        Cannot be used with ``MathExpression`` objects.

        :default: - The period from the metric

        :deprecated: Use ``metric.with({ period: ... })`` to encode the period into the Metric object

        :stability: deprecated
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(deprecated) What function to use for aggregating.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"

        Cannot be used with ``MathExpression`` objects.

        :default: - The statistic from the metric

        :deprecated: Use ``metric.with({ statistic: ... })`` to encode the period into the Metric object

        :stability: deprecated
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional[TreatMissingData]:
        '''(experimental) Sets how this alarm is to handle missing data points.

        :default: TreatMissingData.Missing

        :stability: experimental
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional[TreatMissingData], result)

    @builtins.property
    def metric(self) -> IMetric:
        '''(experimental) The metric to add the alarm on.

        Metric objects can be obtained from most resources, or you can construct
        custom Metric objects by instantiating one.

        :stability: experimental
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(IMetric, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.AlarmWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "alarm": "alarm",
        "left_y_axis": "leftYAxis",
    },
)
class AlarmWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        alarm: "IAlarm",
        left_y_axis: typing.Optional[YAxisProps] = None,
    ) -> None:
        '''(experimental) Properties for an AlarmWidget.

        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6
        :param alarm: (experimental) The alarm to show.
        :param left_y_axis: (experimental) Left Y axis. Default: - No minimum or maximum values for the left Y-axis

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # dashboard is of type Dashboard
            # error_alarm is of type Alarm
            
            
            dashboard.add_widgets(cloudwatch.AlarmWidget(
                title="Errors",
                alarm=error_alarm
            ))
        '''
        if isinstance(left_y_axis, dict):
            left_y_axis = YAxisProps(**left_y_axis)
        self._values: typing.Dict[str, typing.Any] = {
            "alarm": alarm,
        }
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if left_y_axis is not None:
            self._values["left_y_axis"] = left_y_axis

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region the metrics of this graph should be taken from.

        :default: - Current region

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''(experimental) Title for the graph.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def alarm(self) -> "IAlarm":
        '''(experimental) The alarm to show.

        :stability: experimental
        '''
        result = self._values.get("alarm")
        assert result is not None, "Required property 'alarm' is missing"
        return typing.cast("IAlarm", result)

    @builtins.property
    def left_y_axis(self) -> typing.Optional[YAxisProps]:
        '''(experimental) Left Y axis.

        :default: - No minimum or maximum values for the left Y-axis

        :stability: experimental
        '''
        result = self._values.get("left_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IWidget)
class Column(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_cloudwatch.Column"):
    '''(experimental) A widget that contains other widgets in a vertical column.

    Widgets will be laid out next to each other

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_cloudwatch as cloudwatch
        
        # widget is of type IWidget
        
        column = cloudwatch.Column(widget)
    '''

    def __init__(self, *widgets: IWidget) -> None:
        '''
        :param widgets: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [*widgets])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''(experimental) The amount of vertical grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''(experimental) The amount of horizontal grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "width"))


@jsii.implements(IWidget)
class ConcreteWidget(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_cloudwatch.ConcreteWidget",
):
    '''(experimental) A real CloudWatch widget that has its own fixed size and remembers its position.

    This is in contrast to other widgets which exist for layout purposes.

    :stability: experimental
    '''

    def __init__(self, width: jsii.Number, height: jsii.Number) -> None:
        '''
        :param width: -
        :param height: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [width, height])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson") # type: ignore[misc]
    @abc.abstractmethod
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''(experimental) The amount of vertical grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''(experimental) The amount of horizontal grid units the widget will take up.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="x")
    def _x(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "x"))

    @_x.setter
    def _x(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "x", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="y")
    def _y(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "y"))

    @_y.setter
    def _y(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "y", value)


class _ConcreteWidgetProxy(ConcreteWidget):
    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ConcreteWidget).__jsii_proxy_class__ = lambda : _ConcreteWidgetProxy


class GraphWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.GraphWidget",
):
    '''(experimental) A dashboard widget that displays metrics.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            legend_position=cloudwatch.LegendPosition.RIGHT
        ))
    '''

    def __init__(
        self,
        *,
        left: typing.Optional[typing.Sequence[IMetric]] = None,
        left_annotations: typing.Optional[typing.Sequence[HorizontalAnnotation]] = None,
        left_y_axis: typing.Optional[YAxisProps] = None,
        legend_position: typing.Optional[LegendPosition] = None,
        live_data: typing.Optional[builtins.bool] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        right: typing.Optional[typing.Sequence[IMetric]] = None,
        right_annotations: typing.Optional[typing.Sequence[HorizontalAnnotation]] = None,
        right_y_axis: typing.Optional[YAxisProps] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        stacked: typing.Optional[builtins.bool] = None,
        statistic: typing.Optional[builtins.str] = None,
        view: typing.Optional[GraphWidgetView] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param left: (experimental) Metrics to display on left Y axis. Default: - No metrics
        :param left_annotations: (experimental) Annotations for the left Y axis. Default: - No annotations
        :param left_y_axis: (experimental) Left Y axis. Default: - None
        :param legend_position: (experimental) Position of the legend. Default: - bottom
        :param live_data: (experimental) Whether the graph should show live data. Default: false
        :param period: (experimental) The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param right: (experimental) Metrics to display on right Y axis. Default: - No metrics
        :param right_annotations: (experimental) Annotations for the right Y axis. Default: - No annotations
        :param right_y_axis: (experimental) Right Y axis. Default: - None
        :param set_period_to_time_range: (experimental) Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param stacked: (experimental) Whether the graph should be shown as stacked lines. Default: false
        :param statistic: (experimental) The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param view: (experimental) Display this metric. Default: TimeSeries
        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        '''
        props = GraphWidgetProps(
            left=left,
            left_annotations=left_annotations,
            left_y_axis=left_y_axis,
            legend_position=legend_position,
            live_data=live_data,
            period=period,
            right=right,
            right_annotations=right_annotations,
            right_y_axis=right_y_axis,
            set_period_to_time_range=set_period_to_time_range,
            stacked=stacked,
            statistic=statistic,
            view=view,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addLeftMetric")
    def add_left_metric(self, metric: IMetric) -> None:
        '''(experimental) Add another metric to the left Y axis of the GraphWidget.

        :param metric: the metric to add.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addLeftMetric", [metric]))

    @jsii.member(jsii_name="addRightMetric")
    def add_right_metric(self, metric: IMetric) -> None:
        '''(experimental) Add another metric to the right Y axis of the GraphWidget.

        :param metric: the metric to add.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addRightMetric", [metric]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


@jsii.data_type(
    jsii_type="monocdk.aws_cloudwatch.GraphWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "left": "left",
        "left_annotations": "leftAnnotations",
        "left_y_axis": "leftYAxis",
        "legend_position": "legendPosition",
        "live_data": "liveData",
        "period": "period",
        "right": "right",
        "right_annotations": "rightAnnotations",
        "right_y_axis": "rightYAxis",
        "set_period_to_time_range": "setPeriodToTimeRange",
        "stacked": "stacked",
        "statistic": "statistic",
        "view": "view",
    },
)
class GraphWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        left: typing.Optional[typing.Sequence[IMetric]] = None,
        left_annotations: typing.Optional[typing.Sequence[HorizontalAnnotation]] = None,
        left_y_axis: typing.Optional[YAxisProps] = None,
        legend_position: typing.Optional[LegendPosition] = None,
        live_data: typing.Optional[builtins.bool] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        right: typing.Optional[typing.Sequence[IMetric]] = None,
        right_annotations: typing.Optional[typing.Sequence[HorizontalAnnotation]] = None,
        right_y_axis: typing.Optional[YAxisProps] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        stacked: typing.Optional[builtins.bool] = None,
        statistic: typing.Optional[builtins.str] = None,
        view: typing.Optional[GraphWidgetView] = None,
    ) -> None:
        '''(experimental) Properties for a GraphWidget.

        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6
        :param left: (experimental) Metrics to display on left Y axis. Default: - No metrics
        :param left_annotations: (experimental) Annotations for the left Y axis. Default: - No annotations
        :param left_y_axis: (experimental) Left Y axis. Default: - None
        :param legend_position: (experimental) Position of the legend. Default: - bottom
        :param live_data: (experimental) Whether the graph should show live data. Default: false
        :param period: (experimental) The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param right: (experimental) Metrics to display on right Y axis. Default: - No metrics
        :param right_annotations: (experimental) Annotations for the right Y axis. Default: - No annotations
        :param right_y_axis: (experimental) Right Y axis. Default: - None
        :param set_period_to_time_range: (experimental) Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param stacked: (experimental) Whether the graph should be shown as stacked lines. Default: false
        :param statistic: (experimental) The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param view: (experimental) Display this metric. Default: TimeSeries

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # dashboard is of type Dashboard
            
            
            dashboard.add_widgets(cloudwatch.GraphWidget(
                # ...
            
                legend_position=cloudwatch.LegendPosition.RIGHT
            ))
        '''
        if isinstance(left_y_axis, dict):
            left_y_axis = YAxisProps(**left_y_axis)
        if isinstance(right_y_axis, dict):
            right_y_axis = YAxisProps(**right_y_axis)
        self._values: typing.Dict[str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if left is not None:
            self._values["left"] = left
        if left_annotations is not None:
            self._values["left_annotations"] = left_annotations
        if left_y_axis is not None:
            self._values["left_y_axis"] = left_y_axis
        if legend_position is not None:
            self._values["legend_position"] = legend_position
        if live_data is not None:
            self._values["live_data"] = live_data
        if period is not None:
            self._values["period"] = period
        if right is not None:
            self._values["right"] = right
        if right_annotations is not None:
            self._values["right_annotations"] = right_annotations
        if right_y_axis is not None:
            self._values["right_y_axis"] = right_y_axis
        if set_period_to_time_range is not None:
            self._values["set_period_to_time_range"] = set_period_to_time_range
        if stacked is not None:
            self._values["stacked"] = stacked
        if statistic is not None:
            self._values["statistic"] = statistic
        if view is not None:
            self._values["view"] = view

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.

        :stability: experimental
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) The region the metrics of this graph should be taken from.

        :default: - Current region

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''(experimental) Title for the graph.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Width of the widget, in a grid of 24 units wide.

        :default: 6

        :stability: experimental
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def left(self) -> typing.Optional[typing.List[IMetric]]:
        '''(experimental) Metrics to display on left Y axis.

        :default: - No metrics

        :stability: experimental
        '''
        result = self._values.get("left")
        return typing.cast(typing.Optional[typing.List[IMetric]], result)

    @builtins.property
    def left_annotations(self) -> typing.Optional[typing.List[HorizontalAnnotation]]:
        '''(experimental) Annotations for the left Y axis.

        :default: - No annotations

        :stability: experimental
        '''
        result = self._values.get("left_annotations")
        return typing.cast(typing.Optional[typing.List[HorizontalAnnotation]], result)

    @builtins.property
    def left_y_axis(self) -> typing.Optional[YAxisProps]:
        '''(experimental) Left Y axis.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("left_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    @builtins.property
    def legend_position(self) -> typing.Optional[LegendPosition]:
        '''(experimental) Position of the legend.

        :default: - bottom

        :stability: experimental
        '''
        result = self._values.get("legend_position")
        return typing.cast(typing.Optional[LegendPosition], result)

    @builtins.property
    def live_data(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the graph should show live data.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("live_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_070aa057]:
        '''(experimental) The default period for all metrics in this widget.

        The period is the length of time represented by one data point on the graph.
        This default can be overridden within each metric definition.

        :default: cdk.Duration.seconds(300)

        :stability: experimental
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_070aa057], result)

    @builtins.property
    def right(self) -> typing.Optional[typing.List[IMetric]]:
        '''(experimental) Metrics to display on right Y axis.

        :default: - No metrics

        :stability: experimental
        '''
        result = self._values.get("right")
        return typing.cast(typing.Optional[typing.List[IMetric]], result)

    @builtins.property
    def right_annotations(self) -> typing.Optional[typing.List[HorizontalAnnotation]]:
        '''(experimental) Annotations for the right Y axis.

        :default: - No annotations

        :stability: experimental
        '''
        result = self._values.get("right_annotations")
        return typing.cast(typing.Optional[typing.List[HorizontalAnnotation]], result)

    @builtins.property
    def right_y_axis(self) -> typing.Optional[YAxisProps]:
        '''(experimental) Right Y axis.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("right_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    @builtins.property
    def set_period_to_time_range(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to show the value from the entire time range. Only applicable for Bar and Pie charts.

        If false, values will be from the most recent period of your chosen time range;
        if true, shows the value from the entire time range.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("set_period_to_time_range")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stacked(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the graph should be shown as stacked lines.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("stacked")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''(experimental) The default statistic to be displayed for each metric.

        This default can be overridden within the definition of each individual metric

        :default: - The statistic for each metric is used

        :stability: experimental
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional[GraphWidgetView]:
        '''(experimental) Display this metric.

        :default: TimeSeries

        :stability: experimental
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional[GraphWidgetView], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_cloudwatch.IAlarm")
class IAlarm(IAlarmRule, _IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) Represents a CloudWatch Alarm.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''(experimental) Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''(experimental) Name of the alarm.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IAlarmProxy(
    jsii.proxy_for(IAlarmRule), # type: ignore[misc]
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
):
    '''(experimental) Represents a CloudWatch Alarm.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_cloudwatch.IAlarm"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''(experimental) Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''(experimental) Name of the alarm.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarm).__jsii_proxy_class__ = lambda : _IAlarmProxy


class LogQueryWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.LogQueryWidget",
):
    '''(experimental) Display query results from Logs Insights.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        
        
        dashboard.add_widgets(cloudwatch.LogQueryWidget(
            log_group_names=["my-log-group"],
            view=cloudwatch.LogQueryVisualizationType.TABLE,
            # The lines will be automatically combined using '\n|'.
            query_lines=["fields @message", "filter @message like /Error/"
            ]
        ))
    '''

    def __init__(
        self,
        *,
        log_group_names: typing.Sequence[builtins.str],
        height: typing.Optional[jsii.Number] = None,
        query_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        view: typing.Optional[LogQueryVisualizationType] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param log_group_names: (experimental) Names of log groups to query.
        :param height: (experimental) Height of the widget. Default: 6
        :param query_lines: (experimental) A sequence of lines to use to build the query. The query will be built by joining the lines together using ``\\n|``. Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param query_string: (experimental) Full query string for log insights. Be sure to prepend every new line with a newline and pipe character (``\\n|``). Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param region: (experimental) The region the metrics of this widget should be taken from. Default: Current region
        :param title: (experimental) Title for the widget. Default: No title
        :param view: (experimental) The type of view to use. Default: LogQueryVisualizationType.TABLE
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        '''
        props = LogQueryWidgetProps(
            log_group_names=log_group_names,
            height=height,
            query_lines=query_lines,
            query_string=query_string,
            region=region,
            title=title,
            view=view,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class SingleValueWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.SingleValueWidget",
):
    '''(experimental) A dashboard widget that displays the most recent value for every metric.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        # visitor_count is of type Metric
        # purchase_count is of type Metric
        
        
        dashboard.add_widgets(cloudwatch.SingleValueWidget(
            metrics=[visitor_count, purchase_count]
        ))
    '''

    def __init__(
        self,
        *,
        metrics: typing.Sequence[IMetric],
        full_precision: typing.Optional[builtins.bool] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics: (experimental) Metrics to display.
        :param full_precision: (experimental) Whether to show as many digits as can fit, before rounding. Default: false
        :param set_period_to_time_range: (experimental) Whether to show the value from the entire time range. Default: false
        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        '''
        props = SingleValueWidgetProps(
            metrics=metrics,
            full_precision=full_precision,
            set_period_to_time_range=set_period_to_time_range,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class TextWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.TextWidget",
):
    '''(experimental) A dashboard widget that displays MarkDown.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TextWidget(
            markdown="# Key Performance Indicators"
        ))
    '''

    def __init__(
        self,
        *,
        markdown: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param markdown: (experimental) The text to display, in MarkDown format.
        :param height: (experimental) Height of the widget. Default: 2
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        '''
        props = TextWidgetProps(markdown=markdown, height=height, width=width)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


@jsii.implements(IAlarm)
class AlarmBase(
    _Resource_abff4495,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_cloudwatch.AlarmBase",
):
    '''(experimental) The base class for Alarm and CompositeAlarm resources.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: (experimental) The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: (experimental) ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: (experimental) The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: (experimental) The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to

        :stability: experimental
        '''
        props = _ResourceProps_9b554c0f(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addAlarmAction")
    def add_alarm_action(self, *actions: IAlarmAction) -> None:
        '''(experimental) Trigger this action if the alarm fires.

        Typically the ARN of an SNS topic or ARN of an AutoScaling policy.

        :param actions: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addAlarmAction", [*actions]))

    @jsii.member(jsii_name="addInsufficientDataAction")
    def add_insufficient_data_action(self, *actions: IAlarmAction) -> None:
        '''(experimental) Trigger this action if there is insufficient data to evaluate the alarm.

        Typically the ARN of an SNS topic or ARN of an AutoScaling policy.

        :param actions: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addInsufficientDataAction", [*actions]))

    @jsii.member(jsii_name="addOkAction")
    def add_ok_action(self, *actions: IAlarmAction) -> None:
        '''(experimental) Trigger this action if the alarm returns from breaching state into ok state.

        Typically the ARN of an SNS topic or ARN of an AutoScaling policy.

        :param actions: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addOkAction", [*actions]))

    @jsii.member(jsii_name="renderAlarmRule")
    def render_alarm_rule(self) -> builtins.str:
        '''(experimental) AlarmRule indicating ALARM state for Alarm.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderAlarmRule", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmArn")
    @abc.abstractmethod
    def alarm_arn(self) -> builtins.str:
        '''(experimental) Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    @abc.abstractmethod
    def alarm_name(self) -> builtins.str:
        '''(experimental) Name of the alarm.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmActionArns")
    def _alarm_action_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmActionArns"))

    @_alarm_action_arns.setter
    def _alarm_action_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "alarmActionArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="insufficientDataActionArns")
    def _insufficient_data_action_arns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insufficientDataActionArns"))

    @_insufficient_data_action_arns.setter
    def _insufficient_data_action_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "insufficientDataActionArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="okActionArns")
    def _ok_action_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "okActionArns"))

    @_ok_action_arns.setter
    def _ok_action_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "okActionArns", value)


class _AlarmBaseProxy(
    AlarmBase, jsii.proxy_for(_Resource_abff4495) # type: ignore[misc]
):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''(experimental) Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''(experimental) Name of the alarm.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AlarmBase).__jsii_proxy_class__ = lambda : _AlarmBaseProxy


class AlarmStatusWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.AlarmStatusWidget",
):
    '''(experimental) A dashboard widget that displays alarms in a grid view.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        # error_alarm is of type Alarm
        
        
        dashboard.add_widgets(
            cloudwatch.AlarmStatusWidget(
                alarms=[error_alarm]
            ))
    '''

    def __init__(
        self,
        *,
        alarms: typing.Sequence[IAlarm],
        height: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarms: (experimental) CloudWatch Alarms to show in widget.
        :param height: (experimental) Height of the widget. Default: 3
        :param title: (experimental) The title of the widget. Default: 'Alarm Status'
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        '''
        props = AlarmStatusWidgetProps(
            alarms=alarms, height=height, title=title, width=width
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''(experimental) Place the widget at a given position.

        :param x: -
        :param y: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class AlarmWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.AlarmWidget",
):
    '''(experimental) Display the metric associated with an alarm, including the alarm line.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # dashboard is of type Dashboard
        # error_alarm is of type Alarm
        
        
        dashboard.add_widgets(cloudwatch.AlarmWidget(
            title="Errors",
            alarm=error_alarm
        ))
    '''

    def __init__(
        self,
        *,
        alarm: IAlarm,
        left_y_axis: typing.Optional[YAxisProps] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarm: (experimental) The alarm to show.
        :param left_y_axis: (experimental) Left Y axis. Default: - No minimum or maximum values for the left Y-axis
        :param height: (experimental) Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: (experimental) The region the metrics of this graph should be taken from. Default: - Current region
        :param title: (experimental) Title for the graph. Default: - None
        :param width: (experimental) Width of the widget, in a grid of 24 units wide. Default: 6

        :stability: experimental
        '''
        props = AlarmWidgetProps(
            alarm=alarm,
            left_y_axis=left_y_axis,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''(experimental) Return the widget JSON for use in the dashboard.

        :stability: experimental
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class CompositeAlarm(
    AlarmBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.CompositeAlarm",
):
    '''(experimental) A Composite Alarm based on Alarm Rule.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # alarm1 is of type Alarm
        # alarm2 is of type Alarm
        # alarm3 is of type Alarm
        # alarm4 is of type Alarm
        
        
        alarm_rule = cloudwatch.AlarmRule.any_of(
            cloudwatch.AlarmRule.all_of(
                cloudwatch.AlarmRule.any_of(alarm1,
                    cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
            cloudwatch.AlarmRule.from_boolean(False))
        
        cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
            alarm_rule=alarm_rule
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alarm_rule: IAlarmRule,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        composite_alarm_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alarm_rule: (experimental) Expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param composite_alarm_name: (experimental) Name of the alarm. Default: Automatically generated name

        :stability: experimental
        '''
        props = CompositeAlarmProps(
            alarm_rule=alarm_rule,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            composite_alarm_name=composite_alarm_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromCompositeAlarmArn") # type: ignore[misc]
    @builtins.classmethod
    def from_composite_alarm_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        composite_alarm_arn: builtins.str,
    ) -> IAlarm:
        '''(experimental) Import an existing CloudWatch composite alarm provided an ARN.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param composite_alarm_arn: Composite Alarm ARN (i.e. arn:aws:cloudwatch:::alarm/CompositeAlarmName).

        :stability: experimental
        '''
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromCompositeAlarmArn", [scope, id, composite_alarm_arn]))

    @jsii.member(jsii_name="fromCompositeAlarmName") # type: ignore[misc]
    @builtins.classmethod
    def from_composite_alarm_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        composite_alarm_name: builtins.str,
    ) -> IAlarm:
        '''(experimental) Import an existing CloudWatch composite alarm provided an Name.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param composite_alarm_name: Composite Alarm Name.

        :stability: experimental
        '''
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromCompositeAlarmName", [scope, id, composite_alarm_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''(experimental) ARN of this alarm.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''(experimental) Name of this alarm.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))


class Alarm(
    AlarmBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_cloudwatch.Alarm",
):
    '''(experimental) An alarm on a CloudWatch metric.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as cloudwatch
        # delivery_stream is of type DeliveryStream
        
        
        # Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
        incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
            expression="incomingBytes / 300 / bytePerSecLimit",
            using_metrics={
                "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
                "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
            }
        )
        
        cloudwatch.Alarm(self, "Alarm",
            metric=incoming_bytes_percent_of_limit,
            threshold=0.9,
            evaluation_periods=3
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metric: IMetric,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_070aa057] = None,
        statistic: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[TreatMissingData] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param metric: (experimental) The metric to add the alarm on. Metric objects can be obtained from most resources, or you can construct custom Metric objects by instantiating one.
        :param evaluation_periods: (experimental) The number of periods over which data is compared to the specified threshold.
        :param threshold: (experimental) The value against which the specified statistic is compared.
        :param actions_enabled: (experimental) Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: (experimental) Description for the alarm. Default: No description
        :param alarm_name: (experimental) Name of the alarm. Default: Automatically generated name
        :param comparison_operator: (experimental) Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: (experimental) The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: (experimental) Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param period: (deprecated) The period over which the specified statistic is applied. Cannot be used with ``MathExpression`` objects. Default: - The period from the metric
        :param statistic: (deprecated) What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Cannot be used with ``MathExpression`` objects. Default: - The statistic from the metric
        :param treat_missing_data: (experimental) Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing

        :stability: experimental
        '''
        props = AlarmProps(
            metric=metric,
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            period=period,
            statistic=statistic,
            treat_missing_data=treat_missing_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAlarmArn") # type: ignore[misc]
    @builtins.classmethod
    def from_alarm_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        alarm_arn: builtins.str,
    ) -> IAlarm:
        '''(experimental) Import an existing CloudWatch alarm provided an ARN.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param alarm_arn: Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :stability: experimental
        '''
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromAlarmArn", [scope, id, alarm_arn]))

    @jsii.member(jsii_name="addAlarmAction")
    def add_alarm_action(self, *actions: IAlarmAction) -> None:
        '''(experimental) Trigger this action if the alarm fires.

        Typically the ARN of an SNS topic or ARN of an AutoScaling policy.

        :param actions: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addAlarmAction", [*actions]))

    @jsii.member(jsii_name="toAnnotation")
    def to_annotation(self) -> HorizontalAnnotation:
        '''(experimental) Turn this alarm into a horizontal annotation.

        This is useful if you want to represent an Alarm in a non-AlarmWidget.
        An ``AlarmWidget`` can directly show an alarm, but it can only show a
        single alarm and no other metrics. Instead, you can convert the alarm to
        a HorizontalAnnotation and add it as an annotation to another graph.

        This might be useful if:

        - You want to show multiple alarms inside a single graph, for example if
          you have both a "small margin/long period" alarm as well as a
          "large margin/short period" alarm.
        - You want to show an Alarm line in a graph with multiple metrics in it.

        :stability: experimental
        '''
        return typing.cast(HorizontalAnnotation, jsii.invoke(self, "toAnnotation", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''(experimental) ARN of this alarm.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''(experimental) Name of this alarm.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metric")
    def metric(self) -> IMetric:
        '''(experimental) The metric object this alarm was based on.

        :stability: experimental
        '''
        return typing.cast(IMetric, jsii.get(self, "metric"))


__all__ = [
    "Alarm",
    "AlarmActionConfig",
    "AlarmBase",
    "AlarmProps",
    "AlarmRule",
    "AlarmState",
    "AlarmStatusWidget",
    "AlarmStatusWidgetProps",
    "AlarmWidget",
    "AlarmWidgetProps",
    "CfnAlarm",
    "CfnAlarmProps",
    "CfnAnomalyDetector",
    "CfnAnomalyDetectorProps",
    "CfnCompositeAlarm",
    "CfnCompositeAlarmProps",
    "CfnDashboard",
    "CfnDashboardProps",
    "CfnInsightRule",
    "CfnInsightRuleProps",
    "CfnMetricStream",
    "CfnMetricStreamProps",
    "Color",
    "Column",
    "CommonMetricOptions",
    "ComparisonOperator",
    "CompositeAlarm",
    "CompositeAlarmProps",
    "ConcreteWidget",
    "CreateAlarmOptions",
    "Dashboard",
    "DashboardProps",
    "Dimension",
    "GraphWidget",
    "GraphWidgetProps",
    "GraphWidgetView",
    "HorizontalAnnotation",
    "IAlarm",
    "IAlarmAction",
    "IAlarmRule",
    "IMetric",
    "IWidget",
    "LegendPosition",
    "LogQueryVisualizationType",
    "LogQueryWidget",
    "LogQueryWidgetProps",
    "MathExpression",
    "MathExpressionOptions",
    "MathExpressionProps",
    "Metric",
    "MetricAlarmConfig",
    "MetricConfig",
    "MetricExpressionConfig",
    "MetricGraphConfig",
    "MetricOptions",
    "MetricProps",
    "MetricRenderingProperties",
    "MetricStatConfig",
    "MetricWidgetProps",
    "PeriodOverride",
    "Row",
    "Shading",
    "SingleValueWidget",
    "SingleValueWidgetProps",
    "Spacer",
    "SpacerProps",
    "Statistic",
    "TextWidget",
    "TextWidgetProps",
    "TreatMissingData",
    "Unit",
    "YAxisProps",
]

publication.publish()
