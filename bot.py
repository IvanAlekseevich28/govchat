import telebot

with open('bottoken.private', 'r') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

# read the file with pre-defined answers
with open('act.txt', 'r') as f:
    lines = f.readlines()
    answers = {}
    for i in range(0, len(lines), 3):
        key = lines[i].rstrip('\n').lower()
        value = lines[i+1].rstrip('\n')
        answers[key] = value


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! How can I assist you?')


@bot.message_handler(func=lambda message: True)
def reply(message):
    user_phrase = message.text.lower()
    bot_answer = answers.get(user_phrase, 'I do not understand you.')
    bot.reply_to(message, bot_answer)


bot.polling()