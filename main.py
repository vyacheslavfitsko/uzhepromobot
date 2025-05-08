import telebot
import os

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я работаю!")

bot.polling()
