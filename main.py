import random
from telebot import types

import telebot

token = '5915273370:AAGi54xzVZsIjAlLPZh8_GE3PAReQ8YdGYA'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    rq = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_button = 'Go to menu'
    rq.add(menu_button)
    bot.send_message(message.chat.id, "Привет ✌️ ", reply_markup=rq)


@bot.message_handler(content_types=['text'])
def text(message):
    # print(f'Получено сообщение:\n {message.text}\t от\t{message.from_user.username}\n')
    if message.text == 'Go to menu':
        rq = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_1 = 'For both'
        button_2 = 'For her'
        button_3 = 'For him'
        rq.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id,
                         'Hello, I’m here to help, do u wanna have some fun today? Let’s get started!',
                         reply_markup=rq)

    if message.text == 'For both':
        with open('Data/ForBoth.txt') as f:
            ForBothList = list(f.readlines())
        try:
            choice = random.choice(ForBothList)
            bot.send_message(message.chat.id, out_text := f'Today your task is:\n\t{choice}')
            # print(f'Отправлено пользователю {message.from_user.username}\n{out_text}')
            ForBothList.remove(choice)
        except IndexError:
            bot.send_message(message.chat.id, 'Задания закончились...')
        with open('Data/ForBoth.txt', 'w') as f:
            f.writelines(ForBothList)
        # print(len(ForBothList))
    if message.text == 'For her':
        with open('Data/ForHer.txt') as f:
            ForBothList = list(f.readlines())
        try:
            choice = random.choice(ForBothList)
            bot.send_message(message.chat.id, out_text := f'Today your task is:\n\t{choice}')
            # print(out_text)
            ForBothList.remove(choice)
        except IndexError:
            bot.send_message(message.chat.id, 'Задания закончились...')
        with open('Data/ForHer.txt', 'w') as f:
            f.writelines(ForBothList)
    if message.text == 'For him':
        with open('Data/ForHim.txt') as f:
            ForBothList = list(f.readlines())
        try:
            choice = random.choice(ForBothList)
            bot.send_message(message.chat.id, out_text := f'Today your task is:\n\t{choice}')
            # print(out_text)
            ForBothList.remove(choice)
        except IndexError:
            bot.send_message(message.chat.id, 'Задания закончились...')
        with open('Data/ForHim.txt.txt', 'w') as f:
            f.writelines(ForBothList)

    if message.text == '/AdminSayYes':
        with open('Data/ForBoth.txt', 'w') as x:
            with open('Data/ForBoth_copy.txt') as y:
                s = y.read()
            x.write(s)

        with open('Data/ForHim.txt', 'w') as x:
            with open('Data/ForHim_copy.txt') as y:
                s = y.read()
            x.write(s)

        with open('Data/ForHer.txt', 'w') as x:
            with open('Data/ForHer_copy.txt') as y:
                s = y.read()
            x.write(s)

        bot.send_message(message.chat.id, 'Задания восстановлены')


bot.infinity_polling()
