import sys, rawi
from telegram.ext import Updater, CommandHandler
from telegram import Bot
from config import config

def dump(update, context, count):
    context.bot.send_document(
        chat_id='@rawidump', 
        document=open('rawi.csv', 'rb'),
        caption=f'{count} articles'
    )

def infinite_fetch(update, context):
    rows_count = rawi.count_rows()

    text = f'Number of articles: {rows_count}'

    context.bot.edit_message_text(text, '@rawistats', 21)

    count = 0
    while True:
        if((count+rows_count) % 1000 == 0):
            dump(update, context, count+rows_count)
        text = f'Number of articles: {rows_count + count}'
        text += f'\nCurrent article: {rawi.fetch()}'
        context.bot.edit_message_text(text, '@rawistats', 21)
        count += 1

def start(update, context):
    try:
        infinite_fetch(update, context)
    except Exception:
        start(update, context)

def main():
    mode = sys.argv[1] if(len(sys.argv) >= 2) else 'debug'

    if(mode == 'production'):
        token = config('bot.ini', 'tokens')['main']
    else:
        token = config('bot.ini', 'tokens')['dev']
    
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
