import telebot
import os 

import sqlite3

API_TOKEN='8132888082:AAFn-RWIaHNlUgoVPcXs2Zz6a19ifSHm3GU'

bot=telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def message_start(message):
    bot.reply_to(message,'Hello my friend')
    







bot.infinity_polling()
