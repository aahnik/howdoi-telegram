''' Do a lot of stuff. Run any function by ado <func_name>
'''


def set_commands():
    from bot.settings import BOT_TOKEN, BOT_COMMANDS
    from telegram import BotCommand, Bot

    def get_bot_commands():
        bot_commands = []
        for command, description in BOT_COMMANDS:
            bot_commands.append(BotCommand(command, description))
        return bot_commands

    bot = Bot(BOT_TOKEN)
    bot.set_my_commands(get_bot_commands())


def start_polling():
    from bot import bot
    bot.main()
