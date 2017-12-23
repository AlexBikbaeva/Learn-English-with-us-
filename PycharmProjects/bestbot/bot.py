# -*- coding: utf-8 -*-
# Импортируем все нужные в дальнейшем модули
import telebot
import random
import sqlite3 # библиотека соответствующая типу нашей базы данных
from telebot import types # модуль для создания кастомных клавиатур
from datetime import datetime
#import re
import polyglot

"""from polyglot.text import Text, Word"""
token='463907525:AAEMWcnfVzbkhYXiToKFFFBIMrhTLDqyVeo' # Индивидуальный код бота
bot = telebot.TeleBot(token) # Подключение работы модуля к конкретному боту

directory_bot = '/home/yasen/PycharmProjects/bestbot/bot.py' # Путь к боту


# Создание меню с кастомной клавиатурой
"""for menu"""
markup = types.ReplyKeyboardMarkup() # Создание объекта для будущей клавиатуры
hide_markup = types.ReplyKeyboardRemove() #
markup.row('1', '2','3','4') # Добавляем кнопки с названиями
markup.row('5','6','7','8')
"""for nouns"""
keyboardS = types.InlineKeyboardMarkup() # Создание Inline - клавиатуры кнопок; То же и для других частей речи
button1S = types.InlineKeyboardButton(text='funn', callback_data='false')
button2S = types.InlineKeyboardButton(text='y', callback_data='false')
button3S = types.InlineKeyboardButton(text='exist', callback_data='trueSO')
button4S = types.InlineKeyboardButton(text='ly', callback_data='false')
button5S = types.InlineKeyboardButton(text='ful', callback_data='false')
button6S = types.InlineKeyboardButton(text='ence', callback_data='trueSS')
button7S = types.InlineKeyboardButton(text='joy', callback_data='false')
button8S = types.InlineKeyboardButton(text='ride', callback_data='false')
button9S = types.InlineKeyboardButton(text='mean', callback_data='false')
keyboardS.add(button1S,button2S,button3S,button4S,button5S,button6S,button7S,button8S,button9S) # Добавление кнопок в клавиатуру

"""for adverbs"""
keyboardN = types.InlineKeyboardMarkup()
button1N = types.InlineKeyboardButton(text='en', callback_data='false')
button2N = types.InlineKeyboardButton(text='fy', callback_data='false')
button3N = types.InlineKeyboardButton(text='exist', callback_data='false')
button4N = types.InlineKeyboardButton(text='ly', callback_data='false')
button5N = types.InlineKeyboardButton(text='live', callback_data='trueNO')
button6N = types.InlineKeyboardButton(text='ence', callback_data='false')
button7N = types.InlineKeyboardButton(text='joy', callback_data='false')
button8N = types.InlineKeyboardButton(text='free', callback_data='false')
button9N = types.InlineKeyboardButton(text='long', callback_data='trueNS')
keyboardN.add(button1N, button2N, button3N, button4N, button5N, button6N, button7N, button8N, button9N)
"""for adjectives"""
keyboardP = types.InlineKeyboardMarkup()
button1P = types.InlineKeyboardButton(text='redd', callback_data='false')
button2P = types.InlineKeyboardButton(text='y', callback_data='false')
button3P = types.InlineKeyboardButton(text='ence', callback_data='false')
button4P = types.InlineKeyboardButton(text='ly', callback_data='false')
button5P = types.InlineKeyboardButton(text='ent', callback_data='truePS')
button6P = types.InlineKeyboardButton(text='exist', callback_data='truePO')
button7P = types.InlineKeyboardButton(text='joy', callback_data='false')
button8P = types.InlineKeyboardButton(text='ride', callback_data='false')
button9P = types.InlineKeyboardButton(text='mean', callback_data='false')
keyboardP.add(button1P, button2P, button3P, button4P, button5P, button6P, button7P, button8P, button9P)

# Создание кнопки с переходом на сайт с правилами словообразования существительных в английском языке
"""for link in nouns"""
keyboard1 = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Перейти к суффиксам существительных (на сайт)", url="http://engblog.ru/affixation") # Прикрепляем
keyboard1.add(url_button)
goodstickers = ['CAADAgADmwEAArrAlQWXCQdzCyhmVgI','CAADAgADeQEAArrAlQX08DEYjwdFpwI','CAADAgADhAEAArrAlQUeIFJHWmDBwQI','CAADAgADkwEAArrAlQW-HLw00EheNgI','CAADAgADlgEAArrAlQVqIbCgrj_j_wI'] # Массив стикеров
badstickers = ['CAADAgADegEAArrAlQXS8GCYKGkNnAI', 'CAADAgADfAEAArrAlQXtc1bdwghK3QI', 'CAADAgADjwEAArrAlQUxqRA4kmsN3QI', 'CAADAgADkQEAArrAlQXjMXuldKNlswI', 'CAADAgADlwEAArrAlQWdD9RfcxJWLAI']
f1 = open('/home/yasen/PycharmProjects/bestbot/ruleP', 'r') # Открытие файла
ruleP = f1.read() # Чтение файла
f1.close() # Закрытие файла
f2 = open('/home/yasen/PycharmProjects/bestbot/ruleN', 'r')
ruleN = f2.read()
f2.close()
f3 = open('/home/yasen/PycharmProjects/bestbot/ruleG', 'r')
ruleG = f3.read()
f3.close()

#"""word = Word("abstractness")"""
active_train = 0
@bot.message_handler(content_types=["text"])
def learnenglish(message):
    global idch
    global active_train
    idch = message.chat.id
    if message.text == '/start':
        bot.send_sticker(message.chat.id, 'CAADAgADmwEAArrAlQWXCQdzCyhmVgI') #
        bot.send_message(message.chat.id,
                     'Привет, я научу тебя словообразованию английского языка! С чего бы ты хотел начать?\n1)правила словообразования;\n2)тренировка глагол;\n3) тренировка ИП;\n4)тренировка наречия;\n5)тренировка ИС;\n6) тренировка mix;\n7)документация\n8)Статистика\n чтобы вернуться к меню из любого пункта введи на клавиатуре \"меню\"',
                     reply_markup=markup) # Функция для отправки сообщений ботом
    if message.text == '1':
        markup1 = types.ReplyKeyboardMarkup()
        hide_markup1 = types.ReplyKeyboardRemove()
        markup1.row('а', 'б')
        markup1.row('в', 'г')
        bot.send_message(message.chat.id,
                         "Выбери, словообразование какой части речи хочешь изучать: \nа) Имя Существительное;\nб) Имя Прилагательное;\nв) Наречие;\nг) Глагол".format(name=message.text), reply_markup=markup1)
    # Вывод правил
    if message.text == 'а':
        bot.send_message(message.chat.id,"Нажми на кнопку", reply_markup=keyboard1)
    if message.text == 'б':
        bot.send_message(message.chat.id, ruleP.format(name=message.text))
    if message.text == 'в':
        bot.send_message(message.chat.id, ruleN.format(name=message.text))
    if message.text == 'г':
        bot.send_message(message.chat.id, ruleG.format(name=message.text))
    if message.text == '2':
        """for verbs"""
        conn = sqlite3.connect('/home/yasen/PycharmProjects/bestbot/db/bazaslov.dms') # Создание соединения с базой данных SQLite со словами
        c = conn.cursor() # Создание курсора - специального объекта, который делает запросы и получает их результаты
        # Рандомно выбираем сколько нужно выбрать правильных значений
        rEl = random.randint(1, 2)
        rows = c.execute('SELECT * FROM words WHERE `partofspeech` = "verb" ORDER BY RANDOM() LIMIT :limit_n',
                         {"limit_n": rEl}) # Делаем SELECT запрос к базе данных, используя SQL - синтаксис
        rows = rows.fetchall() # Получаем результат сделанного запроса
        # Отнимаем от количества кнопок правильные и получаем  количество неправильных, которые нам нужно выбрать
        no_rEl = 9 - rEl
        no_rows = c.execute('SELECT * FROM words WHERE `partofspeech` != "verb" ORDER BY RANDOM() LIMIT :no_limit_n',
                            {"no_limit_n": no_rEl})
        no_rows = no_rows.fetchall()
        conn.commit() # Занесение изменений в базу данных
        #соединяем массивы
        rows_all = rows + no_rows
        # Создание клавиатуры с кнопками основ слов и суффиксов
        keyboardG = types.InlineKeyboardMarkup()
        buttonG = []
        i = 0
        for row in rows_all:
            if (row[1] == "verb"):
                if i > 8:
                    break
                button = types.InlineKeyboardButton(text=row[2],
                                                    callback_data='' + row[0] + '_verb_' + row[2] + '_' + row[3] + '')
                buttonG.append(button)
                i += 1
                if i > 8:
                    buttonG[0] = types.InlineKeyboardButton(text=row[3], callback_data='' + row[3] + '')
                    break
                else:
                    button = types.InlineKeyboardButton(text=row[3], callback_data='' + row[3] + '')
                    buttonG.append(button)
                    i += 1
            else:
                if i > 8:
                    break
                button = types.InlineKeyboardButton(text=row[2], callback_data='false')
                buttonG.append(button)
                i += 1
                if i > 8:
                    break
                button = types.InlineKeyboardButton(text=row[3], callback_data='false')
                buttonG.append(button)
                i += 1

        # Мешаем все основы и суффиксы
        random.shuffle(buttonG)

        keyboardG.add(*buttonG)
        active_train = 2
        bot.send_message(message.chat.id,
                        'cоставь глагол, нажав сначала на основу, а затем на суффикс слова', reply_markup=keyboardG) # Вывод сообщения пользователю
    if message.text == '3':
        bot.send_message(message.chat.id,
                        'cоставь прилагательное, нажав сначала на основу, а затем на суффикс слова', reply_markup=keyboardP)
    if message.text == '4':
        bot.send_message(message.chat.id,
                        'cоставь наречие, нажав сначала на основу, а затем на суффикс слова', reply_markup=keyboardN)
    if message.text == '5':
        bot.send_message(message.chat.id,
                        'cоставь существительное, нажав сначала на основу, а затем на суффикс слова', reply_markup=keyboardS)
    if message.text == 'меню':
        bot.send_message(message.chat.id, 'С чего бы ты хотел начать?\n1)правила словообразования;\n2)тренировка глагол;\n3) тренировка ИП;\n4)тренировка наречия;\n5)тренировка ИС;\n6) тренировка mix;\n7)документация\n8)Статистика\n чтобы вернуться к меню из любого пункта введи на клавиатуре \"меню\"',
                         reply_markup=markup)
    if message.text == '6':
        bot.send_message(message.chat.id, 'mix в процессе')
        bot.send_message(message.chat.id, 'С чего бы ты хотел начать?\n1)правила словообразования;\n2)тренировка глагол;\n3) тренировка ИП;\n4)тренировка наречия;\n5)тренировка ИС;\n6) тренировка mix;\n7)документация\n8)Статистика\n чтобы вернуться к меню из любого пункта введи на клавиатуре \"меню\"',
                         reply_markup=markup)
    if message.text == '7':
        bot.send_message(message.chat.id, 'документация в процессе')
        bot.send_message(message.chat.id, 'С чего бы ты хотел начать?\n1)правила словообразования;\n2)тренировка глагол;\n3) тренировка ИП;\n4)тренировка наречия;\n5)тренировка ИС;\n6) тренировка mix;\n7)документация\n8)Статистика\n чтобы вернуться к меню из любого пункта введи на клавиатуре \"меню\"',
                         reply_markup=markup)
    if message.text == '8':
        conn2 = sqlite3.connect ('/home/yasen/PycharmProjects/bestbot/db/bazaotvetov.dms') # Соединение с базой данных
        cur = conn2.cursor()
        #
        rows = cur.execute('SELECT * FROM otvety WHERE `user_id` = :user', {"user": message.from_user.id}) #
        rows = rows.fetchall()
        stat_text = "Статистика:\n"
        # Проверяем, если слово было верным, то его значение = 1 и имеется ли суффикс в строке, если да, то записываем, что слово правильное, в статистику. Если его нет, то записываем, что верна была основа слова. Если же слово было неверным, то значение будет соответствовать нулю и пишем, что была неверно выбрана основа.
        i = 0
        for row in rows:
            i += 1
            if row[4] == 1:
                if row[2] != "":
                    stat_text = stat_text + "" + str(i) + ") Правильное слово "+row[2]+"\n"
                else:
                    stat_text = stat_text + "" + str(i) + ") Правильная основа " + row[0] + "\n"
            else:
                stat_text = stat_text + ""+str(i)+") Неправильная основа\n"

        bot.send_message(message.chat.id, stat_text, reply_markup=markup) # ВЫвод сообщения со статистикой

    if message.text != '/start' and message.text != '1' and message.text != '2' and message.text != '3' and message.text != '4' and message.text != '5' and message.text != '6' and message.text != '7' and message.text != '8' and message.text != 'а' and message.text != 'б' and message.text != 'в' and message.text != 'г' and message.text != 'меню':
        bot.send_message(message.chat.id, 'ой, ты что-то не то пишешь, попробуй еще раз')
        bot.send_message(message.chat.id, 'С чего бы ты хотел начать?\n1)правила словообразования;\n2)тренировка глагол;\n3) тренировка ИП;\n4)тренировка наречия;\n5)тренировка ИС;\n6) тренировка mix;\n7)документация\n8)Статистика\n чтобы вернуться к меню из любого пункта введи на клавиатуре \"меню\"',
                         reply_markup=markup)


active_el = False

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
#

    global active_el
    conn2 = sqlite3.connect('/home/yasen/PycharmProjects/bestbot/db/bazaotvetov.dms') # Устанавливаем соединение с базой ответов
    cur = conn2.cursor()
    if call.message:
        temp_data_now = call.data
        temp_data_now = temp_data_now.split('_')
        if (call.data == 'false') or (temp_data_now[0] == 'false') or (active_el == False and temp_data_now[0] == call.data):
            bot.send_message(idch, 'неправильно мыслишь, попробуй еще (выбери на панели ответов другой)')
            bot.send_sticker(idch, badstickers[random.randint(0,4)])
            active_el = False
            cur.execute("insert into otvety values (?,?,?,?,?)", ("", "", "", call.message.chat.id, 0))
            conn2.commit() # Вносим изменения в базу данных
            return
        if (active_train == 2 and active_el != False):
            temp_data_mem = active_el
            temp_data_mem = temp_data_mem.split('_')
            if temp_data_mem[3] == call.data:
                bot.send_message(idch, 'ты гений')
                bot.send_sticker(idch, goodstickers[random.randint(0,4)])
                cur.execute("insert into otvety values (?,?,?,?,?)", (temp_data_mem[2], call.data, temp_data_mem[0], call.message.chat.id, 1))
                conn2.commit()
                active_el = False
            else:
                active_el = False
                bot.send_message(idch, 'неправильно мыслишь, попробуй еще (выбери на панели ответов другой)')
                bot.send_sticker(idch, badstickers[random.randint(0, 4)])
                cur.execute("insert into otvety values (?,?,?,?,?)",(temp_data_mem[2], call.data, temp_data_mem[0], call.message.chat.id, 0))
                conn2.commit()
                return
        if (active_train == 2 and len(temp_data_now)>1 and temp_data_now[1] == "verb" and active_el == False):
            active_el = call.data
            bot.send_message(idch, 'правильно, а теперь найди суффикс')
            cur.execute("insert into otvety values (?,?,?,?,?)",(temp_data_now[2], "", "", call.message.chat.id, 1))
            conn2.commit()

#
        if call.data == 'trueSO' or call.data == 'truePO' or call.data == 'trueNO' or call.data == 'trueGO':
            bot.send_message(idch,'правильно, а теперь найди суффикс')
        if call.data == 'trueSS' or call.data == 'truePS' or call.data == 'trueNS' or call.data == 'trueGS':
            bot.send_message(idch, 'ты гений')
            bot.send_sticker(idch, goodstickers[random.randint(0,4)])


if __name__ == '__main__':
     bot.polling(none_stop=True) # Функция, которая позволяет боту работать непрерывно
