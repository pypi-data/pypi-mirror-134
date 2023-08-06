from typing import List

from twidi.command import Command


class Bot:

    commands = dict()

    def __init__(self):
        return

    def add_commands(self, commands: List[Command]):
        for command in commands:
            self.add_command(command)

    def add_command(self, command: Command):
        self.commands.update({command.text_trigger.lower(): command})

    def handle_input(self, input, debug=True):
        parts = input.split(' ')
        if not parts[0].lower() in self.commands.keys():
            raise KeyError(f'Command {parts[0]} not found in command configuration')
        else:
            command: Command = self.commands[parts[0]]
            result = command.process_command(user='1', arguments=parts[1:], debug=debug)
        return result
