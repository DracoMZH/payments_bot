import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")         # задаётся в Railway
MINI_APP_URL = os.getenv("MINI_APP_URL")   # URL твоего GitHub Pages

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            "💳 Открыть трекер платежей",
            web_app=WebAppInfo(url=MINI_APP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Это твой личный трекер ежемесячных платежей.\n"
        "Нажми кнопку ниже чтобы открыть приложение 👇",
        reply_markup=reply_markup
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Как пользоваться:\n\n"
        "• /start — открыть приложение\n"
        "• В приложении добавляй платежи (название, сумма, день месяца)\n"
        "• Отмечай платежи как оплаченные\n"
        "• В начале месяца нажми «Сбросить статусы»\n\n"
        "Все данные хранятся в облаке — доступно с любого устройства 💾"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
