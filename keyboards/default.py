from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_wikipedia_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = KeyboardButton('🔍Izlash')
    markup.add(btn)
    return markup