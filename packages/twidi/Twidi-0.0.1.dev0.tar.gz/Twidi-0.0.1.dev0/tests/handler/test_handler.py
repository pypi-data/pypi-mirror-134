from twidi.message import ControlMessage


def test_command_default_values():
    cc = ControlMessage(cc_number=7, value=100, device_id='input', channel=1)
    msg = cc.to_message()
    properties = msg.dict()
    assert msg is not None
    assert msg.is_cc(control=7)
    assert properties.get('channel') == 1
    assert properties.get('value') == 100
