from data import bot
from telebot.types import Message, ReplyKeyboardRemove
import wikipedia

from keyboards.default import get_wikipedia_button


@bot.message_handler(regexp='🔍Izlash')
def wiki(message: Message):
    chat_id = message.from_user.id
    msg = bot.send_message(chat_id, "Nimani izlashni xoxlaysiz?", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_info)

def get_info(message: Message):
    chat_id = message.chat.id
    text = message.text
    try:
        wikipedia.set_lang('uz')
        info = wikipedia.summary(text)
        link_info = f"\n\n<b>Botdan foydalanganligingiz uchun rahmat</b>😊\nBotni qolganlar bilan ham ulashning\n👉 <b>\"<a href=\"https://t.me/uzprowebtest_bot\">bot linki</a>\"</b>"
        bot.send_message(chat_id, info + link_info, reply_markup=get_wikipedia_button())

    except:
        bot.send_message(chat_id, "Bunday ma'lumot toiplamdi", reply_markup=get_wikipedia_button())
