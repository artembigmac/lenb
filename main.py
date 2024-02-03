import os
from background import keep_alive
import pip
import telebot
import requests
from bs4 import BeautifulSoup
import time

# Your Telegram bot token
bot_token = '6903658767:AAEtq4YMoi4PglTtytmqWZ0NZ8dHgUcPH9U'
bot = telebot.TeleBot(bot_token)

# List of user IDs to whom messages will be sent
ids = [1149500487, '6352005815']

# Notify users that the bot is running
for user_id in ids:
    bot.send_message(user_id, 'Бот запущен')

keep_alive()
print('Успех')

# Initialize old_data as an empty set
old_data = set()

def check_price():
    global old_data
    url ='https://csgopositive.me/profile/665902/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    trs1 = soup.find('tbody').find_all('tr', {'class': ''})
    # Use a set to store the new data
    new_data = set()

    for i in trs1:
        artved = i.find_all('td')[1:]
        row_data = ' '.join([j.get_text() for j in artved])
        new_data.add(row_data)
    # Check for changes in data
    if (new_data != old_data or len(new_data) != len(old_data)) and new_data - old_data:
        for user_id in ids:
            for st in new_data - old_data:
                bot.send_message(user_id, f'{st}')

        # Update old_data
    old_data = new_data

while True:
    check_price()
    time.sleep(1)  # Sleep for 3 seconds to avoid continuous polling and reduce server load