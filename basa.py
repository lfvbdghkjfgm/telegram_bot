import sqlite3 as sq
from telebot import types

from send import send_mess
from check import is_id, is_holiday
from gets import get_db, lesson, what_group
from time_now import time_now


def change_db1(message,dbs1):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in dbs1:
        class_1 = types.KeyboardButton(i)
        markup.add(class_1)
    send_mess(message.chat.id, 'Выберите ваш класс', markup)


def timetable1(message):
    g = is_id(message.chat.id)
    if g:
        DB = get_db(message.chat.id)
        if is_holiday(DB):
            day = time_now()[2]
            lessons = lesson(DB)
            lessons = next((i for i in lessons if i),0)
            with sq.connect(f'{DB}.db') as con:
                cur = con.cursor()
                g = cur.execute(f'SELECT * FROM {day}')
                g = g.fetchall()
            for i in g:
                i = what_group(i, message.chat.id)
                if lessons == 0:
                    mess = f'<strike><b>{i[0]} урок</b>\nУрок - {i[1]}\nВ кабинете номер {i[3]}\nУчителя зовут - {i[2]}</strike>'
                elif lessons == 1 or lessons[0] > int(i[0]):
                    mess = f'<strike><b>{i[0]} урок</b>\nУрок - {i[1]}\nВ кабинете номер {i[3]}\nУчителя зовут - {i[2]}</strike>'
                elif lessons[0] == int(i[0]):
                    mess = f'<b>{i[0]} урок\nУрок - {i[1]}\nВ кабинете номер {i[3]}\nУчителя зовут - {i[2]}</b>'
                else:
                    mess = f'<i><b>{i[0]} урок</b>\nУрок - {i[1]}\nВ кабинете номер {i[3]}\nУчителя зовут - {i[2]}</i>'
                send_mess(message.chat.id, mess, 0)
        else:
            send_mess(message.chat.id, 'Сегодня нет уроков', 0)
    else:
        send_mess(message.chat.id,
                  'Вы не ввели идентификатор вашего класса\nВам недоступны все функции этого бота', 0)


def messages1(message):
    g = is_id(message.chat.id)
    if g:
        with sq.connect('users.db') as con:
            cur = con.cursor()
            h = cur.execute('''SELECT messages FROM users_1 WHERE id = ?''', (message.chat.id,))
            h = h.fetchone()
            h = h[0]
            if not h:
                mess = 'Вы включили уведомления об уроках'
                h = 1
            else:
                mess = 'Вы выключили уведомления об уроках'
                h = 0
            cur.execute('''UPDATE users_1 SET messages = ? WHERE id = ?''', (h, message.chat.id))
            con.commit()
            send_mess(message.chat.id, mess, 0)
    else:
        send_mess(message.chat.id,
                  'Вы не ввели идентификатор вашего класса\nВам недоступны все функции этого бота', 0)


def lesson_send1(message):
    g = is_id(message.chat.id)
    if g:
        db = get_db(message.chat.id)
        if is_holiday(db):
            lessons = lesson(db)
            if lessons[0] and lessons[1]:
                h1,h2 = what_group(lessons[0],message.chat.id), what_group(lessons[1],message.chat.id)
                mess = f'Сейчас - {h1[1]}\nВ кабинете номер {h1[3]}\nУчителя зовут {h1[2]}'
                send_mess(message.chat.id, mess, 0)
                mess_3 = f'Следующий урок - {h2[1]}\nВ кабинете номер {h2[3]}\nУчителя зовут {h2[2]}'
                send_mess(message.chat.id, mess_3, 0)
            elif lessons[0]:
                h1 = what_group(lessons[0],message.chat.id)
                mess_3 = f'Сейчас - {h1[1]}\nВ кабинете номер {h1[3]}\nУчителя зовут {h1[2]}'
                send_mess(message.chat.id, mess_3, 0)
                send_mess(message.chat.id, 'Это последний урок', 0)
            elif lessons[1]:
                h2 = what_group(lessons[1],message.chat.id)
                mess_3 = f'Следующий урок - {h2[1]}\nВ кабинете номер {h2[3]}\nУчителя зовут {h2[2]}'
                send_mess(message.chat.id, mess_3, 0)

            else:
                send_mess(message.chat.id, 'Уроки закончились', 0)
        else:
            send_mess(message.chat.id, 'Сегодня нет уроков', 0)
    else:
        send_mess(message.chat.id,
                  'Вы не ввели идентификатор вашего класса\nВам недоступны все функции этого бота', 0)


def help1(message):
    g = is_id(message.chat.id)
    if g:
        mess_1 = '''
Приветствую вас в моем боте\n
Этот бот позволяет быстро узнать следующий урок, а также кабинет и ФИО учителя\n
        '''

        mess_2 = '''
<b>Руководство по командам бота</b>\n
<b>/lesson_data</b> - команда, чтобы узнать следующий урок\n
<b>/timetable</b> - команда, чтобы узнать все расписание на сегодня \n
<b>/messages</b> - команда, чтобы включить или выключить уведомления\n
<i>Уведомления приходят за 30 минут до начала первого урока и за 5 минут до начала каждого урока</i>\n\n
<b>/change_db</b> - команда, чтобы поменять класс'''

        mess_3 = '''
        Тех поддержка бота <b>@topych_lfvb</b>'''
        send_mess(message.chat.id, mess_1, 0)
        send_mess(message.chat.id, mess_2, 0)
        send_mess(message.chat.id, mess_3, 0)
    else:
        send_mess(message.chat.id,
                  'Вы не ввели идентификатор вашего класса\nВам недоступны все функции этого бота', 0)


def start1(message):
    g = is_id(message.chat.id)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if g:
        fun_2 = types.KeyboardButton('помощь')
        fun_3 = types.KeyboardButton('расписание')
        fun_4 = types.KeyboardButton('следующий урок')
        fun_5 = types.KeyboardButton('вкл/выкл уведомления')
        change = types.KeyboardButton('поменять группу/класс')
        mess_1 = f'Привет, {message.from_user.first_name}'
        markup.add(fun_2, fun_3, fun_4, fun_5, change)
        send_mess(message.chat.id, mess_1, markup)
        send_mess(message.chat.id, 'Выбери нужную команду или нажми \n/help для открытия инструкции', 0)
    else:
        change = types.KeyboardButton('поменять группу/класс')
        markup.add(change)
        send_mess(message.chat.id,
                  'Вы еще не пользовались этим ботом\nНажмите команду /change_db чтобы выбрать класс', markup)
