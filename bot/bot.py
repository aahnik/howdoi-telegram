from .get_answers import get_answers
from .typing import send_typing_action
import logging
from telegram.ext.filters import Filters

from telegram.ext.messagehandler import MessageHandler
from .settings import BOT_TOKEN, START_TEXT, HELP_TEXT, PORT, HEROKU_APP_NAME
from telegram import Update
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackContext)

from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup, ParseMode


updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def start_handler(update: Update, context: CallbackContext):
    ''' Replies to start command '''

    update.message.reply_text(START_TEXT, parse_mode=ParseMode.MARKDOWN)


def help_handler(update: Update, context: CallbackContext):
    ''' Replies to help command '''
    update.message.reply_text(HELP_TEXT, parse_mode=ParseMode.MARKDOWN)


def reply_answer(update: Update, question: str, pos: int):
    answer = get_answers(question, pos)
    warning = answer.get('warning')

    if warning:
        update.message.reply_text(warning, quote=True)
        return

    text = answer.get('answer', 'Not found')
    link = answer.get('link', 'Not found')
    button = [[IKB('Go to Source', url=link)], ]
    markup = InlineKeyboardMarkup(button)

    update.message.reply_text(
        f'`{text[:3000]}` \n/next',
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN,
        quote=True)


@send_typing_action
def question_handler(update: Update, context: CallbackContext):
    ''' Entry point of conversation  this gives  buttons to user'''

    question = update.message.text
    context.user_data['last_question'] = question
    context.user_data['last_position'] = 1

    reply_answer(update, question, 1)


@send_typing_action
def next_handler(update: Update, context: CallbackContext):
    ''' Sends the next answer to the last question asked by user '''
    question = context.user_data.get('last_question')
    if not question:
        update.message.reply_text('Please ask a question first !', quote=True)
        return
    pos = context.user_data.get('last_position') + 1
    reply_answer(update, question, pos)
    context.user_data['last_position'] = pos


@send_typing_action
def last_handler(update: Update, context: CallbackContext):
    last_question = context.user_data.get('last_question')
    pos = context.user_data.get('last_position')
    update.message.reply_text(
        f'Last question:\n*{last_question}* \n\nLast Postion:*{pos}*', quote=True, parse_mode=ParseMode.MARKDOWN)


@send_typing_action
def unknown(update: Update, context: CallbackContext):
    ''' Handle unknown commands '''
    update.message.reply_text(
        'Command not recognized. Send /help to learn more.', quote=True)


def howdoi_handler(update: Update, context: CallbackContext):
    ''' handle /howdoi command in groups '''
    question = ' '.join(context.args).replace('@how_doiBOt', '')
    reply_answer(update, question, 1)


def add_handlers():
    _handlers = {}

    _handlers['start_handler'] = CommandHandler('start', start_handler)
    _handlers['help_handler'] = CommandHandler('help', help_handler)
    _handlers['next_handler'] = CommandHandler('next', next_handler)
    _handlers['whatLast'] = CommandHandler('last', last_handler)
    _handlers['howdoi'] = CommandHandler('howdoi', howdoi_handler)
    _handlers['unknown'] = MessageHandler(Filters.command, unknown)

    _handlers['question_handler'] = MessageHandler(
        Filters.text, question_handler)

    for name, _handler in _handlers.items():
        print(f'Adding handler {name}')
        dispatcher.add_handler(_handler)


def start_polling():
    add_handlers()
    updater.bot.delete_webhook()
    updater.start_polling()
    updater.idle()
    print('Started polling! ')


def start_webhook():
    add_handlers()
    updater.start_webhook(listen='0.0.0.0',
                          port=int(PORT),
                          url_path=BOT_TOKEN)
    print('Started webhook!')
