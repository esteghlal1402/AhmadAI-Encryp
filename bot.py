from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

TOKEN = os.getenv('BOT_TOKEN')

async def start(update, context):
    await update.message.reply_text('🔐 AhmadAI Encryptor فعال شد!')

async def encrypt_message(update, context):
    text = ' '.join(context.args)
    if text:
        encrypted = f"🔒 encrypted: {text[::-1]}"  # مثال ساده
        await update.message.reply_text(encrypted)
    else:
        await update.message.reply_text('متن رو بفرست: /encrypt متن شما')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("encrypt", encrypt_message))
    print("🔐 AhmadAI Encryptor فعال شد!")
    app.run_polling()

if __name__ == '__main__':
    main()
