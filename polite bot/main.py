# -*- coding: utf-8 -*-
import random as rnd
import telebot
import json
import re

token = "584405943:AAG2acubPunQmp2W2qHfndm0OVSZ7JbPy48"
bot = telebot.TeleBot(token)


def censor(msg):
    flag = False
    with open('initial_data.json', 'r') as file:
        a = json.load(file)

    for elem in a:
        if (elem.get('fields')).get('word') in msg:
            flag = True

    return flag

@bot.message_handler(commands=['PoliteBot'])
def compliment(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Вежливый бот v 1.1!\n'
                 'Я создан, чтобы делать комплименты и банить грубиянов.\n'
                 'Меня создал @OdlinAlex как пример для ваших идей.\n'
                 'Чтобы получить от меня комплимент просто напишите мне об этом!\n\n'
                 'Новвоведения: \n- Бан за плохие слова')

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def compliment_or_ban(message):
        nice_things = [', ты сегодня чудестно выглядишь!', ', у тебя все получится!',
                       ', ты крут, бро!', ', продолжай в том же духе!', ', удачного дня!',
                       ', твои глаза как бирюза!', ', тебя ждет успех!', ', ты супер!']

        if censor(message.text):
                bot.send_message(message.chat.id, message.from_user.first_name+' ЗАБАНИН!1!')
                bot.kick_chat_member(message.chat.id, message.from_user.id)

        if "комплимент" in message.text.lower():
            bot.send_message(message.chat.id, message.from_user.first_name + rnd.choice(nice_things))

if __name__ == "__main__":
    bot.polling(none_stop=True)
