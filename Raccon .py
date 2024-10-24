from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot. Type /help to see available commands.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show this help message')

async def main() -> None:
    # Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token
    application = Application.builder().token("7764138812:AAHwS5_4HwY1yfu1BBKFP7rj1sRyx-uepz4").build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Start polling for updates
    await application.run_polling()

# Entry point of the script
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
