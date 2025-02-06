import telebot
import os 

from googletrans import Translator




# from googletrans import Translator
# translates=Translator()


translator = Translator()




# API_TOKEN=os.environ.get['API_TOKEN']

API_TOKEN='8132888082:AAFn-RWIaHNlUgoVPcXs2Zz6a19ifSHm3GU'



bot=telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=[ 'start'])
def handle_start_help(message):
    bot.reply_to(message,'جمله خود را به فارسی وارد کنید')
    print(message)


# @bot.message_handler(func=lambda m:True)
# def translator_2(message):
#     translate_text=translates.translate(message.text ,src="en",dest="fa")
#     print(translate_text)
#     bot.send_message(message.chat.id,translate_text.text)                                             

@bot.message_handler(func=lambda m:True)
def t(message):
    message_translated = translator.translate(message.text, dest='fr', src='en')
    
    # mim=translates.translate(message.text , src="en" , dest="fa")                   
    # bot.reply_to(message , mim.text)
    print(message_translated.text)
    bot.send_message(message.chat.id,message_translated.text) 







bot.infinity_polling()
