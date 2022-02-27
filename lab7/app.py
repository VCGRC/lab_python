from random import random
from typing import List
import telebot
from telebot import types
from dotenv import dotenv_values
import requests
from random import randint

config = dotenv_values('.env')

bot = telebot.TeleBot(config.get('TOKEN'))

def get_args(message:str) -> List[str]:
    return message.split()[1:]

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Автор","Пельмени",'Чей крым?', "/help","/weather москва", "/roulette")
    bot.send_message(message.chat.id, 'Привет! Я бот!', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\nАвтор - покажет кто автор этого бота\nПельмени - отправит фото пельменей\nЧей крым? - скажет чей крым\n/help - покажет помощь\n/weather <city> - покажет температуру в городе\n/roulette - покажет случайное  число от 0 до 100')

@bot.message_handler(commands=['weather'])
def start_message(message):
    args = get_args(message.text)
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={args[0]}&units=metric&lang=ru&appid={config.get('WEATHER_API')}").json()
    bot.send_message(message.chat.id, f"Температура в городе {args[0]}: {weather['main']['temp']}")

@bot.message_handler(commands=['roulette'])
def start_message(message):
    bot.send_message(message.chat.id, f"{randint(1,100)}")


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "автор":
        bot.send_message(message.chat.id, 'БСС1901 Блинов Виктор')
    elif message.text.lower() == 'пельмени':
        bot.send_chat_action(message.chat.id,'upload_photo')
        image = open('pelmeni.png', 'rb')
        bot.send_photo(message.chat.id, image)
        image.close()
    elif message.text.lower() == 'чей крым?':
        bot.send_message(message.chat.id, 'Крым наш!!!\nРоссия ВПЕРЕД!!!')

bot.infinity_polling()
