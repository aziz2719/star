import telebot
import os
from telebot import types
from faker import Faker
import requests


faker = Faker()

bot = telebot.TeleBot('5072580156:AAEVPu9rvDMWqvYkdjKdXQfHrN1UVCOVos8')

numbers_of_users = 0
user_datas = []

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,
        f'Здравствуйте приятно Вас здесь видеть!')
        bot.send_message(message.from_user.id, 'Максимальное число юзеров, которых можно создать 10. Введите сколько юзеров нужно создать')
        bot.register_next_step_handler(message, get_info)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start чтобы начать')

def get_info(message):
    global numbers_of_users
    numbers_of_users = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_info = types.InlineKeyboardButton(text='Информация', callback_data='info')
    key_create_of_users = types.InlineKeyboardButton(text='Создать юзеров', callback_data='create_of_users')
    key_number_of_users = types.InlineKeyboardButton(text='Количество юзеров', callback_data='number_of_users')
    keyboard.add(key_info)
    keyboard.add(key_create_of_users)
    keyboard.add(key_number_of_users)
    bot.send_message(message.from_user.id, 'Выбери команду', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def create_user(call):
    if call.data == 'create_of_users':
        nb = int(numbers_of_users)
        max_users = 10
        if nb > max_users:
            raise ValueError(bot.send_message(call.message.chat.id, "Cоздайте меньше 10 юзеров или введите число в цифровом формате!"))
        for i in range(nb):
            email = faker.email()
            password = faker.password()
            data = {
            "email": email,
            "password": password,
            "password_repeat": password
            }
            user_datas.append(data)
        user_create_url = "http://127.0.0.1:8000/api/users/users/"
        for item in user_datas:
            requests.post(url=user_create_url, data=item)
        bot.send_message(call.message.chat.id, "Юзеры созданы!")
        print(user_datas)
    elif call.data == 'number_of_users':
        user_list_url = "http://127.0.0.1:8000/api/users/users/"
        for item in user_datas:
            requests.get(url=user_list_url, data=item)
        print(len(user_datas))


bot.polling(none_stop=True, interval=0)