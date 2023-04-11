import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

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

# read the file with menu options
with open('menu.txt', 'r') as f:
    menu_lines = f.readlines()
    menu_options = [option.rstrip('\n') for option in menu_lines]

# Define the start menu with buttons
start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
for option in menu_options:
    start_menu.add(KeyboardButton(option))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! How can I assist you?', reply_markup=start_menu)

@bot.message_handler(func=lambda message: True)
def reply(message):
    user_phrase = message.text.lower()
    bot_answer = answers.get(user_phrase, 'I do not understand you.')
    if user_phrase == menu_options[-1].lower():
        bot_answer = 'Welcome back to the menu!'
        bot.send_message(message.chat.id, bot_answer, reply_markup=start_menu)
    else:
        bot.reply_to(message, bot_answer, reply_markup=start_menu)


bot.polling()
