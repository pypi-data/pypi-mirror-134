from twidi.command import CommandOptions, CommandArgument
from twidi.message import ControlMessage


def test_command_constructor():
    options = CommandOptions(
        arguments=[CommandArgument(name="value")],
        device_id='MRCC',
        channel=12,
        name='Knob 1 Position',
        description='Change Knob 1 Position',
        cooldown_time_in_seconds=20,
        text_triggers=['eyesy1'],
        help_text='',
        midi_command=ControlMessage(cc_number=21, value=0)

    )

    assert options is not None


def test_command_to_dict():
    options = CommandOptions(
        arguments=[CommandArgument(name="value")],
        device_id='MRCC',
        channel=12,
        name='Knob 1 Position',
        description='Change Knob 1 Position',
        cooldown_time_in_seconds=20,
        text_triggers=['eyesy1'],
        help_text='',
        midi_command=ControlMessage(cc_number=21, value=0)
    )

    d = options.to_dict()
    assert d is not None
    argument = d.get('arguments')[0]
    assert argument.get('name') == 'value'
    assert argument.get('min') == 0
    assert argument.get('max') == 127


def test_command_from_dict():
    options = CommandOptions(
        arguments=[CommandArgument(name="value")],
        device_id='MRCC',
        channel=12,
        name='Knob 1 Position',
        description='Change Knob 1 Position',
        cooldown_time_in_seconds=20,
        text_trigger='eyesy1',
        help_text='',
        midi_command=ControlMessage(cc_number=21, value=0)
    )

    from_dict_options = CommandOptions.from_dict(options.to_dict())
    assert from_dict_options.arguments[0].get('name') == 'value'


def test_command_to_yaml():
    options = CommandOptions(
        arguments=[CommandArgument(name="value")],
        device_id='MRCC',
        channel=12,
        name='Knob 1 Position',
        description='Change Knob 1 Position',
        cooldown_time_in_seconds=20,
        text_trigger='eyesy2',
        help_text='',
        midi_command=ControlMessage(cc_number=21, value=0)
    )

    from_dict_options = CommandOptions.from_dict(options.to_dict())
    assert from_dict_options.arguments[0].get('name') == 'value'
