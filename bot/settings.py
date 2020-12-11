import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
assert BOT_TOKEN

START_TEXT = 'Hi I am alive'
HELP_TEXT = 'Help'



if __name__ == "__main__":
    print(BOT_TOKEN)
