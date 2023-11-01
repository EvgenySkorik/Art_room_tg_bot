import telebot
from telebot import types

from handler_bot import FuncInterface

bot = telebot.TeleBot('6691657677:AAGXrGHx5FbR9byyd0CcSnTUQ1G59ZOw-Os')

func = FuncInterface()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_dice(message.chat.id)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    bt1 = types.KeyboardButton(text='Услуги')
    bt2 = types.KeyboardButton(text='О нас')
    bt3 = types.KeyboardButton(text='Оставить заявку')
    bt4 = types.KeyboardButton(text='Примеры проектов')
    markup.add(bt1, bt2, bt3, bt4)
    bot.send_message(message.chat.id, f'Приветствуем {message.from_user.username}!\n'
                                      f'Вы попали в дизайнерскую студию <b>"АРТ-РУМ"</b>',
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text.lower() == 'о нас':
        func.send_website_of_company(message)
    elif message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id,
                         '<b>Будем рады сотрудничеству с Вами!</b> Оставьте свой телефон а ниже напишите что '
                         'требуется. Пример:\n88005553535\nКвартира 82м2\nРазработка дизайн-проекта\nСмета по материалу'
                         '\nРемонт под ключ', parse_mode='html')
        bot.register_next_step_handler(message, func.send_application(message))
    elif message.text.lower() == 'услуги':
        func.service(message)
    elif message.text.lower() == 'примеры проектов':
        func.random_foto(message)


if __name__ == '__main__':
    bot.infinity_polling()
