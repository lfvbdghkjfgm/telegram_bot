import telebot
import time
import threading
from os import getenv
from dotenv import load_dotenv,find_dotenv

from admin import send_to_me
from check import is_id
from time_now import time_now
from regisrt import group1, classes
from basa import change_db1, timetable1, messages1, lesson_send1, help1, start1
from notice import not1
from upd import first, next_les
from gets import dbs_1

load_dotenv(find_dotenv())

bot = telebot.TeleBot(getenv('TOKEN'))

dbs,dbs1 = dbs_1()
first_time = first(dbs)
next_time = next_les(dbs)
already_sent = 0

def group(message):
    group1(message)
    start(message)


def send_all_messages():
    global next_time, first_time, already_sent, dbs
    while True:
        com_time = time_now()[-1]
        already_sent = not1(already_sent, com_time, next_time, first_time)
        for i in next_time:
            if com_time >= i[0]:
                next_time = next_les(dbs)
        time.sleep(15)


@bot.message_handler(commands=['start'])
def start(message):
    start1(message)


@bot.message_handler(commands=['help'])
def help(message):
    help1(message)


@bot.message_handler(commands=['lesson_data'])
def lesson_send(message):
    lesson_send1(message)


@bot.message_handler(commands=['messages'])
def messages(message):
    messages1(message)


@bot.message_handler(commands=['timetable'])
def timetable(message):
    timetable1(message)


@bot.message_handler(commands=['change_db'])
def change_db(message):
    change_db1(message,dbs1)


@bot.message_handler(content_types=['text'])
def new_user(message):
    if message.text == 'поменять группу/класс':
        change_db(message)

    if message.text in dbs1:
        classes(message)
    elif is_id(message.chat.id):
        if message.text in ['группа 1', 'группа 2']:
            group(message)
        elif message.text == 'помощь':
            help(message)
        elif message.text == 'следующий урок':
            lesson_send(message)
        elif message.text == 'вкл/выкл уведомления':
            messages(message)
        elif message.text == 'расписание':
            timetable(message)


threading.Thread(target=send_all_messages, daemon=True).start()

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            send_to_me('расписание', e)
            time.sleep(5)
