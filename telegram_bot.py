import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, ApplicationBuilder

TOKEN = '5905018015:AAGar6s-VtRlGh0GJKXfHg4Eo7zeUeyF8JI'
BOT_USERNAME = '@audio_recognizerr_bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a telegram voice message and I will send you a text version of it")


async def handle_voice(update, context):
    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)
    await file.download_to_drive('audio-to-recognize.ogg')
    await update.message.reply_text('Downloading your audio')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    # Errors
    app.add_error_handler(error)

    # Polling huyoling
    print('Polling...')
    app.run_polling(poll_interval=3)