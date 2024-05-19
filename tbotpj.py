
import telebot
from telebot import types
from telegram.ext import Updater,CommandHandler,MessageHandler
import datetime
import json
import openpyxl
import pandas as pd


TOKEN=""
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
                if message.text=="Arıza" or message.text=="Masraf":
                     bot.send_message(message.chat.id,"Hatalı seçim")
                else:
                     bot.register_next_step_handler(message,report)
            #report(message)
            elif message.text == 'Arıza':
                bot.send_message(message.chat.id,"Lütfen Arızayı yazın")
                bot.register_next_step_handler(message,mulfunction)
            elif message.text == 'Masraf':
                bot.send_message(message.chat.id,"Lütfen Aralarında çizgi '-' koyarak TARİH-FİRMA BİLGİSİ-TUTAR şeklinde fiş bilgisini yazın")
                bot.register_next_step_handler(message,expenses)

def report(message):
    if message.text=="Arıza" or message.text=="Masraf":
        bot.send_message(message.chat.id,"Hatalı giriş. Lütfen doğru butonu seçin!")
        return
    else:
        data1= message.text
        print(data1)
        now1=datetime.datetime.now()
        tsp1=now1.strftime("%Y-%m-%d %H:%M:%S")

        with open('report.txt','+a') as file:
             file.write("{} , {} \n".format(tsp1,data1))
             file.close()
        bot.send_message(message.chat.id,"Kayıt Alındı")

def mulfunction(message):
    if message.text=="Rapor" or message.text=="Masraf":
        bot.send_message(message.chat.id,"Hatalı giriş. Lütfen doğru butonu seçin!")
        return
    else:
        data3= message.text
        now = datetime.datetime.now()
        tsp=now.strftime("%Y-%m-%d %H:%M:%S")
        with open('Arıza.txt','+a') as file:
             file.write("{} , {} \n".format(tsp,data3))
             file.close()
        bot.send_message(message.chat.id,"Arıza Kaydı oluşturuldu")

def expenses(message):
    if message.text=="Rapor" or message.text=="Masraf":
        bot.send_message(message.chat.id,"Hatalı giriş. Lütfen doğru butonu seçin!")
        return
    else:
        try:
            data2= message.text.split("-")
            print(data2)
            now2=datetime.datetime.now()
            tsp2=now2.strftime("%Y-%m-%d %H:%M:%S")
            with open('Masraf.txt','+a') as file:
                 file.write("{}-{}-{} \n".format(data2[0],data2[1],data2[2]))
                 file.close()
            bot.send_message(message.chat.id,"Masraf Girildi")
        except IndexError:
            if  message.text == "Exit":
               bot.send_message(message.chat.id,"Yapmak istediğiniz işlem butonunu seçin")
               return
            
            else:
                bot.send_message(message.chat.id,"Hatalı giriş,Lütfen doğru formatta girin!")
                bot.send_message(message.chat.id,"Lütfen Aralarında çizgi '-' koyarak TARİH-FİRMA BİLGİSİ-TUTAR şeklinde fiş bilgisini yazın")
                bot.register_next_step_handler(message,expenses)


bot.polling(non_stop=True)
