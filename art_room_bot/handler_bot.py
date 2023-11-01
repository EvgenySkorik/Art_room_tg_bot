import telebot
from telebot import types
import random
from datetime import datetime
import os

bot = telebot.TeleBot(os.getenv('TG_API_KEY'))
COUNTER = 0


def _send_service(message):
    bot.send_message(message.chat.id, '1. Разработка дизайн-проекта со сметной документацией (на руки и в PDF)')
    bot.send_message(message.chat.id, '2. Рекомендации по планированию и проектированию')
    bot.send_message(message.chat.id, '3. Авторский контроль Вашей бригады по ходу строительства')
    bot.send_message(message.chat.id, '4. Ремонт под ключ по согласованному проекту')


def _random_foto(message):
    with open('foto_art/diz (1).jpg', 'rb') as f1, open('foto_art/diz (1).jpeg', 'rb') as f2, open(
            'foto_art/diz (2).jpg', 'rb') as f3, \
            open('foto_art/a 02.jpg', 'rb') as f4, open('foto_art/11.jpg', 'rb') as f5, open('foto_art/23.jpg',
                                                                                             'rb') as f6:
        bot.send_photo(message.chat.id, random.choice([f1, f2, f3, f4, f5, f6]))


def _send_website_of_company(val):
    markup = types.InlineKeyboardMarkup()
    url_bt = types.InlineKeyboardButton(text='Ссылка на сайт', url='https://art-rum.ru/')
    markup.add(url_bt)
    bot.send_message(val.chat.id, 'Информация о компании\nРаботаем 100500 лет, делаем красиво\nВаш дизайн и ремонт '
                                  'в надёжных руках', reply_markup=markup)


def _send_application(message):
    global COUNTER
    COUNTER += 1
    dt = datetime.now()
    with open('log.txt', 'a', encoding='utf-8') as lof_file:
        lof_file.write(f'Заявка№: {COUNTER}, Name: {message.from_user.username} INPUT: {message.text}, DATE: {dt}\n')
    bot.send_message(message.chat.id, 'Спасибо за заявку. С вами свяжутся\nДля возобновления введите /start')


class FuncInterface():
    @staticmethod
    def service(message):
        return _send_service(message)

    @staticmethod
    def random_foto(message):
        return _random_foto(message)

    @staticmethod
    def send_website_of_company(message):
        return _send_website_of_company(message)

    @staticmethod
    def send_application(message):
        return _send_application(message)


if __name__ == '__main__':
    FuncInterface()
    _send_service()
    _random_foto()
    _send_website_of_company()
    _send_application()
