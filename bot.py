import telebot
from telebot import types
import parser


url = 'https://www.pravda.com.ua/rus/news/'
Api_Bot = '5958326152:AAHF6GYtAK1bBuXfxT-qaIHyULYKuESLs5g'
bot = telebot.TeleBot(Api_Bot)

new_ua = parser.new(url)

new_ua = parser.new(url)

description = parser.new_description(url)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Hello 👋')
    btn2 = types.KeyboardButton('How are you')
    btn3 = types.KeyboardButton('Help')
    btn4 = types.KeyboardButton('News')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, f'Hello', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Hello 👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Hello 👋')
        btn2 = types.KeyboardButton('How are you')
        btn3 = types.KeyboardButton('Help')
        btn4 = types.KeyboardButton('News')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name},thanks for using this bot', reply_markup=markup)
    elif message.text == '/Start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Hello 👋')
        btn2 = types.KeyboardButton('How are you')
        btn3 = types.KeyboardButton('Help')
        btn4 = types.KeyboardButton('News')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, f'Hello', reply_markup=markup)

    elif message.text == 'How are you':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Good and you?')
        btn2 = types.KeyboardButton('No good')
        btn3 = types.KeyboardButton('Back')
        btn4 = types.KeyboardButton('News')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "I'm fine and you?", reply_markup=markup)
    elif message.text == 'Help':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Back')
        markup.add(btn1)
        command = '/start' + '\n' + '\n' + '/help'
        bot.send_message(message.chat.id, command, reply_markup=markup)
    elif message.text == '/Help':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Back')
        markup.add(btn1)
        command = '/start' + '\n' + '\n' + '/help'
        bot.send_message(message.chat.id, command, reply_markup=markup)
    elif message.text == '/help':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Back')
        markup.add(btn1)
        command = '/start' + '\n' + '\n' + '/help'
        bot.send_message(message.chat.id, command, reply_markup=markup)
    elif message.text == 'Good':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Что ты можешь?')
        btn2 = types.KeyboardButton('Хочешь скину тебе какой нибудь смайл?')
        btn3 = types.KeyboardButton('Back')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "I'm fine and you?", reply_markup=markup)
    elif message.text == 'Что ты можешь?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton('Back')
        markup.add(btn3)
        bot.send_message(message.chat.id, "Пока что ничего", reply_markup=markup)
    elif message.text == 'No good':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton('Back')
        markup.add(btn3)
        bot.send_message(message.chat.id, "Drink tea!", reply_markup=markup)
    elif message.text == 'Хочешь скину тебе какой нибудь смайл?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton('Back')
        markup.add(btn3)
        bot.send_message(message.chat.id, "Закончились!", reply_markup=markup)
    elif message.text == 'Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Hello 👋')
        btn2 = types.KeyboardButton('How are you')
        btn3 = types.KeyboardButton('Help')
        btn4 = types.KeyboardButton('News')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Start menu', reply_markup=markup)
    elif message.text == 'News':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Узнать больше")
        btn2 = types.KeyboardButton('Next news')
        btn3 = types.KeyboardButton('Back')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, new_ua[0], reply_markup=markup)
        del description[0]
        del new_ua[0]
    elif message.text == 'Next news':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Узнать больше")
        btn2 = types.KeyboardButton('Next news')
        btn3 = types.KeyboardButton('Back')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, new_ua[0], reply_markup=markup)
        del description[0]
        del new_ua[0]
    elif message.text == "Узнать больше":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton('Back')
        btn1 = types.KeyboardButton("Узнать больше")
        btn2 = types.KeyboardButton('Next news')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, description[0], reply_markup=markup)


bot.polling(none_stop=True)
# тематика навостей
