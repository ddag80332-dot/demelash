import os
import telebot
from flask import Flask
from threading import Thread

# Bot Credentials
TOKEN = "8960828504:AAGqVVodgGcIJiF8Lk__E4JL1WFI7vDZ_1k"
ADMIN_CHAT_ID = "8293715605"

ADMIN_CHAT_ID = "8293715605"

bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ሰላም! ಡೆመላሽ ቶፕ አፕ ቦት በሥራ ላይ ይገኛል።")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
