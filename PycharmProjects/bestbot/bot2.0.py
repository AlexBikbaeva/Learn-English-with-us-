# -*- coding: utf-8 -*-

import telebot
import random
from telebot import types
token='463907525:AAEMWcnfVzbkhYXiToKFFFBIMrhTLDqyVeo'
bot = telebot.TeleBot(token)
directory_bot = '/home/yasen/PycharmProjects/bestbot'
from telebot import types
markup = types.ReplyKeyboardMarkup()
markup.row('правила')
markup.row('тренировка с ИС')
markup.row('тренировка с ИП')
lst = ['abjectness','actor','abrasiveness','abruptness',
       'absentmindedness','absoluteness','specialist','existence',
       'abstractness','altruism']
#f = open('/home/anna/bot/rule', 'r')
f = open('/home/yasen/PycharmProjects/bestbot/ruleN', 'r')
rule = f.read()
f.close()
@bot.message_handler(content_types=["text"])
def start(message):
    sentstart = bot.send_message(message.chat.id,
                                 'Привет, я научу тебя словообразованию английского языка! С чего бы ты хотел начать?', reply_markup=markup)
    bot.register_next_step_handler(sentstart, play)
def play(message):
    if message.text == 'правила':
        bot.send_message(message.chat.id, 'вот правила!'.ReplyKeyboardHide())
        sentplay = bot.send_message(message.chat.id, rule.format(name=message.text))
        bot.register_next_step_handler(sentplay, retrn)
    else:
        sentplay2 = bot.send_message(message.chat.id, 'собери слово из этих частей:\n exist, ful, play, ence')
        bot.register_next_step_handler(sentplay2, answer)
def retrn(message):
        bot.send_message(message.chat.id, 'удачи!')
def answer(message):
        if message.text in lst:
            bot.send_sticker(message.chat.id,
                     'CAADAgADeQEAArrAlQX08DEYjwdFpwI')
        else:
            bot.send_message(message.chat.id, 'лошара')
if __name__ == '__main__':
    bot.polling(none_stop=True)
                            
