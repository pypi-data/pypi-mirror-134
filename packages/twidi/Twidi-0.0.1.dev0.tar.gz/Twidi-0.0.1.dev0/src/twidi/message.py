from enum import Enum

import mido

''' Message Argument Options
===========  ======================  ================
Name         Valid Range             Default Value
===========  ======================  ================
channel      0..15                   0
frame_type   0..7                    0
frame_value  0..15                   0
control      0..127                  0
note         0..127                  0
program      0..127                  0
song         0..127                  0
value        0..127                  0
velocity     0..127                  64
data         (0..127, 0..127, ...)   () (empty tuple)
pitch        -8192..8191             0
pos          0..16383                0
time         any integer or float    0
===========  ======================  ================
'''


class MessageType(Enum):
    '''
    The available MIDI message types
    '''
    NO_TYPE = 'undefined'
    PITCH_WHEEL = 'pitchwheel'
    NOTE_ON = 'note_on'
    NOTE_OFF = 'note_off'
    CONTROL_CHANGE = 'control_change'
    POLY_TOUCH = 'polytouch'
    AFTER_TOUCH = 'aftertouch'
    START = 'start'
    RESET = 'reset'
    STOP = 'stop'
    CONTINUE = 'continue'


class MidiMessage():
    _type: MessageType
    default_value = None
    allow_custom_value = True
    last_called = -1
    _value: int = None

    def __init__(self, value=0, channel=0, allow_custom_value=True):
        self.value = value
        self.channel = channel
        self.allow_custom_value = allow_custom_value

    @staticmethod
    def validate(**kwargs):
        raise NotImplementedError()

    def to_message(self, **kwargs) -> mido.Message:
        raise NotImplementedError()

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self.allow_custom_value:
            return
        else:
            self._value = value


class ControlMessage(MidiMessage):
    _type: MessageType = MessageType.CONTROL_CHANGE

    def __init__(self, cc_number: int, value: int = 0, channel: int = 0, **kwargs):
        super().__init__(value=value, channel=channel)
        self.channel = channel
        self.cc_number = cc_number

    def to_message(self, value: int = None, **kwargs) -> mido.Message:
        """
        Create a message to send to MIDO - MIDO message values can be overridden see docs for
        list of available options
        :param cc_number: CC number - IE - 7
        :param value: Valid int, usually 0-127
        :param kwargs: Any valid MIDO options
        :return:
        """

        val = self.value
        if self.allow_custom_value and value:
            val = value
        elif value:
            raise ValueError('Command does not allow custom values')
        channel = kwargs.get('channel', self.channel)
        return mido.Message('control_change', control=self.cc_number, value=val, channel=channel)


