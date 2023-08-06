import logging

import fire

from twidi.bot import Bot
from twidi.config import commands

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handle_twitch_chat_input(input_text, debug_mode=True):
    bot = Bot()
    bot.add_commands(commands)
    try:
        result = bot.handle_input(input_text, debug_mode)
        if debug_mode:
            result = 'DEBUG TRUE - ' + str(result)
        logger.warning(result)
    except KeyError as e:
        logger.error(e)


if __name__ == '__main__':
    fire.Fire(handle_twitch_chat_input)
