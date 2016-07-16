import telebot
import sqlite3

from settings import KeyBot

from Utils.functions import initialize_database
from User.models import User

initialize_database()
bot = telebot.TeleBot(KeyBot)

user_bot = bot.get_me()


def start(message):
    bot_user = message.from_user
    user = User(bot_user.first_name, bot_user.last_name, bot_user.username, bot_user.id)
    try:
        user.save()
    except sqlite3.IntegrityError:
        user.update()
    bot.send_message(message.chat.id, "Hi, I'm RestIntBot your personal Bot for schedule dinners!")


def test_start(message):
    return message.text == 'start'


@bot.message_handler(func=test_start)
def send_welcome(message):
    start(message)


@bot.message_handler(commands=['start'])
def send_help(message):
    start(message)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Help is comming')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, "I don't understund {}".format(message.text))


bot.polling()
