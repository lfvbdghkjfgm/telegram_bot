from telebot import apihelper
import sqlite3 as sq
import telebot

from admin import send_to_me
from config import TOKEN

load_dotenv(find_dotenv())

bot = telebot.TeleBot(getenv('TOKEN'))


def send_mess(ID, text, but):
    try:
        if but:
            bot.send_message(ID, text, reply_markup=but, parse_mode='html')
        else:
            bot.send_message(ID, text, parse_mode='html')
    except apihelper.ApiException as e:
        send_to_me('расписание', e)
        if e.error_code == 403:
            with sq.connect('users.db') as con:
                cur = con.cursor()
                cur.execute('DELETE FROM users_1 WHERE id  = ?', [ID])
                con.commit()
    except Exception as e:
        send_to_me('расписание', e)
