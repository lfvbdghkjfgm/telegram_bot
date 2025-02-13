import telebot
from os import getenv
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
bot = telebot.TeleBot(getenv('TOKEN1'))

ID = 5150707530

def send_to_me(bots, text):
    global ID
    bot.send_message(ID, f'{bots}\n{text}')
