'''
# CloudWatch Alarm Actions library

This library contains a set of classes which can be used as CloudWatch Alarm actions.

The currently implemented actions are: EC2 Actions, SNS Actions, Autoscaling Actions and Aplication Autoscaling Actions

## EC2 Action Example

```python
# Example automatically generated from non-compiling source. May contain errors.
import aws_cdk.aws_cloudwatch as cw

# Alarm must be configured with an EC2 per-instance metric
# alarm is of type Alarm
# Attach a reboot when alarm triggers
alarm.add_alarm_action(
    Ec2Action(Ec2InstanceActions.REBOOT))
```

See `@aws-cdk/aws-cloudwatch` for more information.
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
from ..aws_applicationautoscaling import (
    StepScalingAction as _StepScalingAction_d79ca2c9
)
from ..aws_autoscaling import StepScalingAction as _StepScalingAction_24d17483
from ..aws_cloudwatch import (
    AlarmActionConfig as _AlarmActionConfig_f831c655,
    IAlarm as _IAlarm_ff3eabc0,
    IAlarmAction as _IAlarmAction_922c5aa8,
)
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.implements(_IAlarmAction_922c5aa8)
class ApplicationScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.ApplicationScalingAction",
):
    '''Use an ApplicationAutoScaling StepScalingAction as an Alarm Action.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationautoscaling as appscaling
        from aws_cdk import aws_cloudwatch_actions as cloudwatch_actions
        
        # step_scaling_action is of type StepScalingAction
        
        application_scaling_action = cloudwatch_actions.ApplicationScalingAction(step_scaling_action)
    '''

    def __init__(self, step_scaling_action: _StepScalingAction_d79ca2c9) -> None:
        '''
        :param step_scaling_action: -
        '''
        jsii.create(self.__class__, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: constructs.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an ApplicationScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(_IAlarmAction_922c5aa8)
class AutoScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.AutoScalingAction",
):
    '''Use an AutoScaling StepScalingAction as an Alarm Action.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_autoscaling as autoscaling
        from aws_cdk import aws_cloudwatch_actions as cloudwatch_actions
        
        # step_scaling_action is of type StepScalingAction
        
        auto_scaling_action = cloudwatch_actions.AutoScalingAction(step_scaling_action)
    '''

    def __init__(self, step_scaling_action: _StepScalingAction_24d17483) -> None:
        '''
        :param step_scaling_action: -
        '''
        jsii.create(self.__class__, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: constructs.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an AutoScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(_IAlarmAction_922c5aa8)
class Ec2Action(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.Ec2Action",
):
    '''Use an EC2 action as an Alarm action.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch_actions as cloudwatch_actions
        
        ec2_action = cloudwatch_actions.Ec2Action(cloudwatch_actions.Ec2InstanceAction.STOP)
    '''

    def __init__(self, instance_action: "Ec2InstanceAction") -> None:
        '''
        :param instance_action: -
        '''
        jsii.create(self.__class__, self, [instance_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: constructs.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an EC2 action as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch_actions.Ec2InstanceAction")
class Ec2InstanceAction(enum.Enum):
    '''Types of EC2 actions available.'''

    STOP = "STOP"
    '''Stop the instance.'''
    TERMINATE = "TERMINATE"
    '''Terminatethe instance.'''
    RECOVER = "RECOVER"
    '''Recover the instance.'''
    REBOOT = "REBOOT"
    '''Reboot the instance.'''


@jsii.implements(_IAlarmAction_922c5aa8)
class SnsAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.SnsAction",
):
    '''Use an SNS topic as an alarm action.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch_actions as cw_actions
        # alarm is of type Alarm
        
        
        topic = sns.Topic(self, "Topic")
        alarm.add_alarm_action(cw_actions.SnsAction(topic))
    '''

    def __init__(self, topic: _ITopic_9eca4852) -> None:
        '''
        :param topic: -
        '''
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: constructs.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an SNS topic as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


__all__ = [
    "ApplicationScalingAction",
    "AutoScalingAction",
    "Ec2Action",
    "Ec2InstanceAction",
    "SnsAction",
]

publication.publish()
