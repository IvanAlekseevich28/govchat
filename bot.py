import telebot

with open('./bottoken.private', 'r') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в госчатбот")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == '1':
        bot.send_message(message.chat.id, 'A')
    elif message.text == '2':
        bot.send_message(message.chat.id, 'B')
    elif message.text == '3':
        bot.send_message(message.chat.id, 'C')
    else:
        bot.send_message(message.chat.id, 'Простите, не смог обработать ваш текущий запрос.')

bot.polling()
