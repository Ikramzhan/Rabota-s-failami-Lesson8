import time
import telebot 
from time import sleep

import logging

import random



TOKEN = '5875708806:AAED_HXh60M9XFWh6Jy-30JsAfQe-Uo6DK0'

bot = telebot.TeleBot(TOKEN)


# команда /random_num
@bot.message_handler(commands=['random_num'])
def random_num(message):
    num = random.randint(0, 1000)
    bot.send_message(message.chat.id, str(num))


# команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Салам, мен бот жардамчымын')

# текст
@bot.message_handler(content_types=['text'])
def text(message):
       if message.text.lower() == "салам":
          bot.send_message(message.chat.id,'Салам, салам ')
       
       elif message.text.lower() == "атыңыз ким?":
        bot.send_message(message.chat.id,'Бектурхан')

       elif message.text.lower() == "атаңдын аты ким?":
        bot.send_message(message.chat.id,'Икрам') 

       elif message.text.lower() == "энеңдин аты ким?":
        bot.send_message(message.chat.id,'Зарифа') 
         
       elif message.text.lower() == "эжеңдин аты ким?":
        bot.send_message(message.chat.id,'Мавлида')       

bot.polling()
