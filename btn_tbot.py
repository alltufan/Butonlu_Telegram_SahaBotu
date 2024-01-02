
import telebot
from telebot import types
from telegram.ext import Updater,CommandHandler,MessageHandler
import datetime
import json


TOKEN="your bot token here"
bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1=types.KeyboardButton("Rapor")
    b2=types.KeyboardButton("Arıza")
    b3=types.KeyboardButton("Masraf")

    markup.add(b1,b2,b3)
    bot.send_message(message.chat.id,"Hoşgeldiniz!", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.chat.type == message.chat.type:
        if message.text=="Rapor":
            bot.send_message(message.chat.id,"Lütfen rapor metnini girin")
            bot.register_next_step_handler(message,report)
            #report(message)
        elif message.text == 'Arıza':
            bot.send_message(message.chat.id,"Lütfen Arızayı yazın")
            bot.register_next_step_handler(message,mulfunction)
        elif message.text == 'Masraf':
            bot.send_message(message.chat.id,"Lütfen Aralarında virgül koyarak TARİH, FİRMA BİLGİSİ, TUTAR şeklinde fiş bilgisini yazın")
            bot.register_next_step_handler(message,expenses)

def report(message):
    data1= message.text
    now1=datetime.datetime.now()
    tsp1=str(now1)
    data1_json={"Aciklama: ": data1,
                "tarih: ": tsp1,}
    with open("report.js","a+",encoding='UTF-8') as file:
         json.dump(data1_json,file)
    bot.send_message(message.chat.id,"Kayıt Alındı")

def mulfunction(message):

    data3= message.text
    now = datetime.datetime.now()
    tsp=str(now)
    data_json={"arıza": data3,
                "tarih": tsp,}
    with open("mulfunction.js","a+",encoding='UTF-8') as file:
              json.dump(data_json,file)
    bot.send_message(message.chat.id,"Arıza Kaydı oluşturuldu")


def expenses(message):

    data2= message.text.split(",")
    now2=datetime.datetime.now()
    tsp2=str(now2)
    data2_json={"Tarih: ": data2[0],
                "Aciklama: ": data2[1],
                "Tutar: ": data2[2],}
    with open("expenses.js","a+",encoding='UTF-8') as file:
            json.dump(data2_json,file)
    bot.send_message(message.chat.id,"Masraf Girildi")






bot.polling(non_stop=True)
