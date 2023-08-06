import datetime
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Literal

import mido
from mido import Backend

from twidi.message import MessageType, MidiMessage


class ChangeType(Enum):
    NO_CHANGE = 0
    CURVE = 1
    INSTANT = 2


@dataclass
class CommandArgument:
    name: str = 'value'
    position: int = 0
    min: int = 0
    max: int = 127


@dataclass
class CommandOptions:
    name: str
    description: str
    help_text: str
    device_id: str
    channel: int
    mod_only: bool
    midi_command: MidiMessage
    cooldown_time_in_seconds: int
    arguments: List[CommandArgument]
    text_trigger: str
    backend = 'mido.backends.pygame'
    permitted_users: List[str] = None
    reply_text_format: str = None
    case_sensitive = False
    point_cost: int = -1
    enabled = False
    min_value = 0
    max_value = 127
    change_type: Literal['instant', 'curve'] = 'instant'
    bit_cost = -1

    def to_dict(self):
        return asdict(self)

    def to_yaml(self):
        pass

    @staticmethod
    def from_dict(option_dict):
        return CommandOptions(**option_dict)

    def from_yaml(self):
        pass


class Command:
    permitted_users = []
    text_trigger: str
    case_sensitive = False
    device_id = ''
    name = ''
    change_type = ChangeType.INSTANT
    channel: int
    arguments = []
    mod_only = False
    cool_down_time_in_seconds = None
    last_called = None
    point_cost = -1
    bit_cost = -1
    description: str
    help_text: str

    type: MessageType

    def __init__(self, options: CommandOptions):
        '''TODO Make initialization more elegant'''
        self.device_id = options.device_id
        self.backend = options.backend
        self.permitted_users = options.permitted_users
        self.case_sensitive = options.case_sensitive
        self.name = options.name
        self.arguments = options.arguments
        self.description = options.description
        self.help_text = options.help_text
        self.cool_down_time_in_seconds = options.cooldown_time_in_seconds
        self.channel = options.channel
        self.text_trigger = options.text_trigger
        # TODO Investigate command constructor options
        # self.command: MidiCommand = CommandFactory.create(type=MessageType(options.midi_command_type), **options.to_dict())
        self.command = options.midi_command

    def process_command(self, user: str, arguments=None, **kwargs):
        cooldown_ready = not self.cool_down_time_in_seconds or self.is_off_cooldown()
        has_permission = self.user_has_permission(user)

        if arguments and arguments[0] == 'help':
            return self.help_text

        if arguments and arguments[0] == 'description':
            return self.description

        if not cooldown_ready:
            time_since_call = datetime.datetime.now() - self.last_called
            return f'Command {self.text_trigger} is on cooldown for another {str(self.cool_down_time_in_seconds - time_since_call.seconds)} seconds.'

        if not self.user_has_permission(user=user):
            return f'User {user} does not have permission to call {self.text_trigger}.'

        self.last_called = datetime.datetime.now()
        parsed_arguments = self.parse_arguments(arguments)
        if kwargs.get('debug', False):
            return self.command.to_message(**parsed_arguments)
        self.send_midi(self.command, **parsed_arguments)

    def send_midi(self, command: MidiMessage, **options):
        mido.set_backend(self.backend, load=True)
        # noinspection PyTypeChecker
        backend: Backend = mido
        with backend.open_output(self.device_id) as opened_output:
            opened_output.send(command.to_message(channel=self.channel))

    def is_off_cooldown(self):
        if not self.last_called:
            return True
        time_since_call = datetime.datetime.now() - self.last_called
        return time_since_call.seconds > self.cool_down_time_in_seconds

    def user_has_permission(self, user: str):
        '''Stub - Check mod permissions, etc'''
        if self.mod_only:
            return self.user_is_mod(user=user)
        return True

    def parse_arguments(self, arguments):
        argument_dict = dict()
        for index, arg in enumerate(arguments):
            expected_argument = self.arguments[index]
            argument_dict.update({expected_argument.name: int(arg)})
        return argument_dict

    def user_is_mod(self, user: str):
        return True
