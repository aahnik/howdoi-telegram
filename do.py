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


def poll():
    from bot.bot import start_polling
    start_polling()


def set_webhook():
    from bot.settings import WEBHOOK_URL
    from bot.bot import updater
    updater.bot.set_webhook(WEBHOOK_URL)


def hook():
    from bot.bot import start_webhook
    start_webhook()


def webhook_info():
    from bot.bot import updater
    print(updater.bot.get_webhook_info())


def set_hook():
    from bot.bot import updater
    from bot.settings import WEBHOOK_URL, HEROKU_APP_NAME
    if not HEROKU_APP_NAME:
        print('Heroku app name ( subdomain ) not set')
        quit()
    updater.bot.set_webhook(WEBHOOK_URL)
    print('Success! ')


if __name__ == '__main__':
    set_webhook()
    set_commands()
    hook()
