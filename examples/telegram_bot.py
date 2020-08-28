from os import environ as env

import nlcli
import telebot

bot = telebot.TeleBot(env["TELEGRAM_TOKEN"])


@nlcli.cmd(["hi", "Hi my name is {name}"])
def hello(name=""):
    return f"hi {name}"


@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.send_message(message.chat.id, nlcli.interact(message.text))


if __name__ == "__main__":
    bot.polling()
