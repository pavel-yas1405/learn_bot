from datetime import datetime
import ephem
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename ="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, пользователь! Ты вызвал команду /start")

def user_planet(update, context):
    enter_planet = update.message.text.split(' ')[1]
    if enter_planet == "Mercury":
        planet_now = ephem.Mercury(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Venus":
        planet_now = ephem.Venus(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Earth":
        planet_now = ephem.Earth(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Mars":
        planet_now = ephem.Mars(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Jupiter":
        planet_now = ephem.Jupiter(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Saturn":
        planet_now = ephem.Saturn(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Uranus":
        planet_now = ephem.Uranus(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    elif enter_planet == "Neptune":
        planet_now = ephem.Neptune(datetime.today())
        update.message.reply_text(ephem.constellation(planet_now))
    else:
        update.message.reply_text("Такой планеты не существует")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", user_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()