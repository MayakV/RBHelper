import telebot
import openai
import time
import os

import openai_api
import db_api

TG_TOKEN = os.getenv("GeorgiaHelpBot_Token")
bot = telebot.TeleBot(TG_TOKEN)

stop_symbols = "###"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = db_api.User(message.from_user)
    if user.is_in_db():
        user.clear_context()
        bot.reply_to(message, f"Started! (History cleared).")
    else:
        bot.reply_to(message, f"Hi and welcome to bot!")
        get_help(message)


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.reply_to(message, f"This is all the help you get")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    request = message.text
    user = db_api.User(message.from_user.id)
    user.lookup_in_db()

    # if last prompt time > 10 minutes ago - drop context
    if time.time() - user.last_prompt_time > 600:
        user.last_prompt_time = 0
        user.last_text = ''

    ans = ''
    try:
        ans = openai_api.get_answer(user.id,
                                    request,
                                    user.last_text,
                                    user.last_prompt_time)
    except ValueError as err:
        bot.send_message(message.chat.id, err)


    user.last_text = request
    user.last_prompt_time = time.time()

    bot.send_message(message.chat.id, ans)


bot.infinity_polling(interval=3)
