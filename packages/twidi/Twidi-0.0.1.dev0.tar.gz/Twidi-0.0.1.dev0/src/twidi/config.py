from twidi.command import Command as TwidiCommand, CommandArgument, CommandOptions
from twidi.message import ControlMessage

default_device = 'MRCC'
default_channel = 12

commands = [
    TwidiCommand(CommandOptions(
            name="Knob 1 Position",
            text_trigger='eyesy1',
            description="Adjust Knob 1 Position",
            mod_only=False,
            device_id=default_device,
            cooldown_time_in_seconds=30,
            help_text='Useful help text to help the user deal with knob1',
            channel=default_channel,
            arguments=[CommandArgument(name='value', min=0, max=127, position=0)],
            midi_command=ControlMessage(cc_number=21, device_id=default_device, channel=default_channel),
        ),
    ),
    TwidiCommand(CommandOptions(
            name="Knob 2 Position",
            text_trigger='eyesy2',
            description="Adjust Knob 2 Position",
            mod_only=False,
            device_id=default_device,
            cooldown_time_in_seconds=30,
            channel=default_channel,
            help_text='Useful help text to help the user deal with knob2',
            arguments=[CommandArgument(name='value', min=0, max=127, position=0)],
            midi_command=ControlMessage(cc_number=22, device_id=default_device, channel=default_channel),
        )
    ),
]
