# pylint: disable=unused-argument, broad-except, invalid-name
from timeit import default_timer as timer
from telegram.ext import Updater, CommandHandler
from variables import TELEGRAM_BOT_TOKEN, EMOJI_SCREAM, EMOJI_SLEEP
from google_sheets.execute import execute


def _help(update, context):
    """Return help message with allowed commands.
    """
    message = '''This bot will fetch data from some public APIs, insert fetched data into \
Google spreadsheets and send url of the spreadsheet to the user. \n
/fetch - fetch data and return url of spreadsheet.
/help - return help message'''
    update.message.reply_text(message)


def fetch(update, context):
    """Run script and return url of created spreadsheet.
    """
    message = f'fetching data, this should take few seconds... {EMOJI_SLEEP*3}'
    update.message.reply_text(message)
    try:
        start = timer()
        url = execute()
        message = f'data fetched in {round(timer() - start, 1)}s. here is url to spreadsheet: {url}'
        update.message.reply_text(message)
    except Exception as e:
        message = f'there was some error {EMOJI_SCREAM*3}\nerror message: {e}'
        update.message.reply_text(message)


def run_bot():
    """Start Telegram bot.
    """
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('help', _help))
    updater.dispatcher.add_handler(CommandHandler('start', _help))
    updater.dispatcher.add_handler(CommandHandler('fetch', fetch))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run_bot()
