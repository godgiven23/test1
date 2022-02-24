import telebot
from settings import token
bot =telebot.TeleBot(token)

@bot.message_handlers(content_types=['text'])
def get_text_message(message):
    username = message.from_user.username
    msg=f'кто здесь.'
    bot.send_message(message.from_user.id,msg)