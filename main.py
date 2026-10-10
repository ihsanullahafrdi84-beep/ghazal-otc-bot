import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Ghazal Market Analysis Bot!\n\n"
        "Commands:\n"
        "/scan - Educational analysis demo\n"
        "/status - Check bot status\n\n"
        "Note: This bot does not provide verified "
        "live Quotex OTC signals."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot is running.\n"
        "Live Quotex OTC market data is not connected."
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Market analysis demo\n\n"
        "RSI: Not available\n"
        "EMA: Not available\n"
        "MACD: Not available\n\n"
        "A verified live price-data source is required "
        "before real analysis is possible."
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("scan", scan))

    app.run_polling()


if __name__ == "__main__":
    main()
