import os
import telebot
import main
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('TELEGRAM_API_KEY')
bot = telebot.TeleBot(
    API_KEY, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def greet(message):
    bot.reply_to(message, "Hey My G")


@bot.message_handler(commands=['btc', 'BTC', 'bitcoin', 'BITCOIN'])
def prices(message):
    bot.reply_to(message, main.get_cmc_data('BTC'))


@bot.message_handler(commands=['eth', 'ETH', 'ethereum', 'ETHEREUM'])
def prices(message):
    bot.reply_to(message, main.get_cmc_data('ETH'))


@bot.message_handler(commands=['wagmi', 'WAGMI'])
def prices(message):
    bot.reply_to(message, main.get_cmc_data('WAGMI'))


bot.polling()
print("bot running...")
