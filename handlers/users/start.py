from data import bot
from telebot.types import Message
from keyboards.default import get_wikipedia_button


@bot.message_handler(commands=['start'], chat_types='private')
def start(message: Message):
    chat_id = message.from_user.id
    print(chat_id)
    bot.send_message(chat_id, f"Assalomu alaukum, {message.from_user.first_name}, <b>wikipedia</b> botga xush kelibsiz!\n"
                              f"Ma'lumot izlash uchun <b>🔍Izlash</b> tugmasini bosib so'ng izlanayotgan so'zni kiriting.",
                     reply_markup=get_wikipedia_button())

