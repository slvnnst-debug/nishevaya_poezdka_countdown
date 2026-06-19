from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8829750059:AAFGyELlmVcCHlvaa-_d3ZUOdmE5ygDOK9A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app = WebAppInfo(url="https://github.com/slvnnst-debug/nishevaya_poezdka_countdown/settings/pages")

    keyboard = [
        [KeyboardButton(text="⏳ Открыть таймер", web_app=web_app)]
    ]

    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Нажми кнопку 👇",
        reply_markup=markup
    )


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
