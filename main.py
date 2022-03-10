import telebot



from telebot import types
# pip install pytelegrambotapi
token = '5280003455:AAGOqtbvUpLI_DL_HIbz8h4N8ocmJGFoYbc'
bot = telebot.TeleBot(token)
chat_id = '-1001667629231' # Например chat_id = '223344'
# Telegram bot: Get My Id

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, text="Привет,что бы записаться на тренировку пожалуйста оставь заявку в формате:")
    bot.send_message(message.chat.id, text="Имя Фамилия,жанр,дата-время")

    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Расписание', url='https://aerialrope.fun/go')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Время и дату тренировок можно узнать тут 👇", reply_markup = markup)

    bot.send_message(message.chat.id, text="Напрмиер: Павел Иванов,акробатика 15.02 16:30")
    bot.send_message(message.chat.id, text="После,вы будете автоматически записаны на тренировку")



@bot.message_handler(content_types=['text'])
def all_messages(message):
    bot.forward_message(chat_id, message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop=True)