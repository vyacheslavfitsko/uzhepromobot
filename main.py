import telebot
from datetime import datetime
import random
import os

TOKEN = os.getenv("8072658630:AAFafvZi8EF0Qkjjzacv0lfkB5W9A1zHwUg")
bot = telebot.TeleBot(8072658630:AAFafvZi8EF0Qkjjzacv0lfkB5W9A1zHwUg)

users = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    today = datetime.now().strftime("%Y-%m-%d")

    if users.get(user_id) == today:
        bot.send_message(user_id, "😬 Вы уже получали промокод сегодня. Попробуйте снова завтра!")
    else:
        promo = random.choice(["LUCKY5", "LUCKY10", "LUCKY15", "LUCKY20"])
        users[user_id] = today
        bot.send_message(user_id, f"🎉 Поздравляем! Ваш промокод: <b>{promo}</b>", parse_mode="HTML")

print("✅ Бот запущен...")
bot.polling()
