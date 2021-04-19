import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

START_TEXT = '''
Hi! I am alive. *Ask me a question.*

My [source code](https://github.com/aahnik/howdoi-telegram) is on GitHub.

I am made using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and [howdoi](https://github.com/gleitz/howdoi).
'''

HELP_TEXT = '''
Any message you send to me is treated as a question.

I will reply the relevant code snippets. You can send /next to get the next answer of the current question.
'''

BOT_COMMANDS = [
    ('start', 'check whether i am alive'),
    ('help', 'know more about me'),
    ('next', 'get next answer'),
]


# webhook settings

PORT = os.environ.get('PORT')
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
WEBHOOK_URL = f'https://{HEROKU_APP_NAME}.herokuapp.com/{BOT_TOKEN}'

print(f'PORT {PORT}')
print(f'HEROKU_APP_NAME {HEROKU_APP_NAME}')
print(f'WEBHOOK_URL {WEBHOOK_URL}')
