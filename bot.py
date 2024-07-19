import os
from dataclasses import dataclass

import requests
import telebot


API_ENDPOINT = os.getenv('API_ENDPOINT')
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@dataclass(frozen=True)
class State:

    name: str
    capital: str
    area: str
    population: str

    def repr(self):
        return (
            f'Name: {self.name}\n'
            f'Capital: {self.capital}\n'
            f'Area: {self.area} sq. km\n'
            f'Population: {self.population:,}'
        )


@bot.message_handler(commands=['random'])
def random_state_handler(message):
    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()
    except requests.RequestException:
        returned_data = 'Error was occurred. Pls try again later.'
    else:
        random_state = response.json()
        returned_data = State(**random_state).repr()

    bot.reply_to(message, returned_data)


bot.infinity_polling()
