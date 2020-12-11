import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

START_TEXT = '''
Hi! I am alive. *Ask me a question.*

My [source code](https://github.com/aahnik/how_doiBOt) is on GitHub.

I am made using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and [howdoi](https://github.com/gleitz/howdoi)
'''

HELP_TEXT = ''' Any message you send to me is treated as a question. 

I will reply the relevant code snippets. You can send /next to get the next answer of the current question. '''

BOT_COMMANDS = [
    ('start', 'check whether i am alive'),
    ('help', 'know more about me'),
    ('next', 'get next answer'),
]

if __name__ == "__main__":
    print(BOT_TOKEN)
