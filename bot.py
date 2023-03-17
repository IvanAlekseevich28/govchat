import telebot

with open('./bottoken.private', 'r') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Добро пожаловать в госчатбот!")
    main_menu(message)

def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    option_a = telebot.types.KeyboardButton('Нижний Новгород')
    option_b = telebot.types.KeyboardButton('Нижегородская область')
    markup.add(option_a, option_b)
    bot.reply_to(message, "Вы живете в Нижнем Новгороде или в Нижегородской области?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Нижний Новгород')
def option_nn(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    option_nn1 = telebot.types.KeyboardButton('да')
    option_nn2 = telebot.types.KeyboardButton('нет')
    markup.add(option_nn1, option_nn2)
    bot.reply_to(message, "Вы знаете в какую организацию нужно обратиться с проблемой/запросом?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'нет')
def option_nn2(message):
    bot.reply_to(message, "Опишите Вашу проблему.")

@bot.message_handler(func=lambda message: message.text == 'У нас нет врачей в поликлинике 167, не могу записаться к терапевту.  Сама поликлиника как год закрыта на ремонт.')
def option_nnNo(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    option_nnno1 = telebot.types.KeyboardButton('Нет')
    option_nnno2 = telebot.types.KeyboardButton('Да, жду ответа')
    option_nnno3 = telebot.types.KeyboardButton('Да, мне не помогли')
    option_nnno4 = telebot.types.KeyboardButton('Да, меня не приняли')
    markup.add(option_nnno1, option_nnno2, option_nnno3, option_nnno4)
    bot.reply_to(message, "Вы обращались в администрацию поликлиники 167 с данной проблемой?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Да, мне не помогли')
def option_nnno3(message):
    bot.reply_to(message, "Ваше заявление нужно отправить в министерство здравоохранения Нижегородской области – https://zdrav-nnov.ru/. Перефразируйте ваше заявление под шаблон (скачать) и отправите с кодом 4567 в чат. Ответ придет Вам в течении 3 дней. Посмотреть его можно будет в разделе «уведомления», личный аккаунт, сайт «Госуслуги». ")

@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.reply_to(message, "Простите, не смог обработать ваш текущий запрос.")

bot.polling()

