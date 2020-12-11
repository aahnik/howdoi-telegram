from .get_answers import get_answers
import logging
from telegram.ext.filters import Filters

from telegram.ext.messagehandler import MessageHandler
from .settings import BOT_TOKEN, START_TEXT, HELP_TEXT
from telegram import Update
from telegram.ext import (Updater,
                          PicklePersistence,
                          CommandHandler,
                          CallbackQueryHandler,
                          CallbackContext,
                          ConversationHandler)

from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup, ParseMode


def start(update: Update, context: CallbackContext):
    ''' Replies to start command '''
    update.message.reply_text(START_TEXT)


def question_handler(update: Update, context: CallbackContext):
    ''' Entry point of conversation  this gives  buttons to user'''

    question = update.message.text
    answer = get_answers(question)
    text = answer.get('answer', 'Not found')
    link = answer.get('link', 'Not found')
    button = [[IKB('Go to Source', url=link)],
              [IKB('Previous ', callback_data='prev'), IKB(' Next', callback_data='next')]]
    markup = InlineKeyboardMarkup(button)

    update.message.reply_text(
        f'`{text[:3000]}`', reply_markup=markup, parse_mode=ParseMode.MARKDOWN, quote=True)


# def button_click_handler(update: Update, context: CallbackContext):
#     ''' This gets executed on button click '''
#     query = update.callback_query
#     # shows a small notification inside chat
#     query.answer(f'button click {query.data} recieved')

#     if query.data == 'name':
#         context.bot.send_message(chat_id=update.effective_chat.id,
#                                  text='Send your name', reply_markup=ForceReply())


def main():

    updater = Updater(token=BOT_TOKEN)

    dispatcher = updater.dispatcher

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    _handlers = {}

    _handlers['start_handler'] = CommandHandler('start', start)
    _handlers['question_handler'] = MessageHandler(
        Filters.text, question_handler)

    for name, _handler in _handlers.items():
        print(f'Adding handler {name}')
        dispatcher.add_handler(_handler)

    updater.start_polling()

    updater.idle()
