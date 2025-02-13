import sqlite3 as sq
import re
from telebot import types

from send import send_mess
from check import is_id
from admin import send_to_me


def group1(message):
    with sq.connect('users.db') as con:
        cur = con.cursor()
        class_1 = cur.execute('SELECT class FROM users_1 WHERE id = ?', [message.chat.id, ])
        class_1 = class_1.fetchone()
        if class_1[0] == '157610Г':
            cur.execute('UPDATE users_1 SET gr = ? WHERE id = ?', [int(message.text[-1]), message.chat.id])
            con.commit()
            send_mess(message.chat.id, 'Вы успешно выбрали группу', 0)


def classes(message):
    send_to_me('расп',1)
    with sq.connect('users.db') as con:
        cur = con.cursor()
        is_in = is_id(message.chat.id)
        text = message.text
        cl = re.findall(r'(\d+)(10|11|2|3|4|5|6|7|8|9)(\w{1})', text)[0]
        if is_in:
            cur.execute('''UPDATE users_1 SET class = ?, gr = ? WHERE id = ?''', (text, 0, message.chat.id))
            con.commit()
        else:
            cur.execute('INSERT INTO users_1(id,class,gr,messages, name) VALUES (?,?,0,0,?)',
                        (message.chat.id, '157610Г', message.from_user.username))
            con.commit()
        cur = con.cursor()
        gr = cur.execute('SELECT group_1,group_2 FROM groups WHERE class = ?', [text]).fetchall()[0]
    send_mess(message.chat.id,
                      f'Вы успешно выбрали клас\nВаш класс - {cl[1]}"{cl[2]}" класс школы №{cl[0]}', 0)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    group_1 = types.KeyboardButton('группа 1')
    group_2 = types.KeyboardButton('группа 2')
    markup.add(group_1, group_2)
    send_mess(message.chat.id,
              f'Теперь вы обязательно должны выбрать вашу группу\n\nГруппа №1 - учителя: '
              f'{gr[0]}\n\nГруппа №2 - учителя: '
              f'{gr[1]}', markup)
