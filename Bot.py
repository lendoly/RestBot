import telebot

from settings import KeyBot

from user.models import User

bot = telebot.TeleBot(KeyBot)

help_message = '''
    RestBot is a Bot for help you and your to find a place for dinner/lunch or simply take a break
    The possibles commands are:
        /start
'''


def start(message):
    bot_user = message.from_user
    user = User(bot_user.first_name, bot_user.last_name, bot_user.username, bot_user.id)
    user.save()

    bot.send_message(message.chat.id,
                     "Hi {}, I'm RestIntBot your personal Bot for schedule dinners!".format(user.username))


def test_start(message):
    return message.text.lower() == 'start'


@bot.message_handler(func=test_start)
def send_welcome(message):
    start(message)


@bot.message_handler(commands=['start'])
def send_help(message):
    start(message)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, help_message)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, "I don't understund {}".format(message.text))


bot.polling()
