import telebot
from telebot import types
from node import Node
with open('bottoken.txt', 'r') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message)

def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton("Начать")
    markup.add(btn1)  
    bot.send_message(message.from_user.id, "Добро пожаловать", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def talking(message):
    global Dialog
    if message.text == "назад":
       Dialog= Node(["Вы живете в Нижнем Новгороде или в Нижегородской области?","Нижний Новгород"],Node(["Вы знаете в какое ведомство нужно обратиться с Вашей проблемой?","да","нет"],Node(["Выберите ведомство","1","2"],Node(["выбрали1","назад"]),Node(["выбрали2","назад"])),    Node(["Опишите Вашу проблему.","назад"],Node(["назад"]))))
    Data_len=len(Dialog.data)
    for i in range(Data_len-1):
     if message.text == Dialog.data[i+1]:
        if i==0: 
            Dialog=Dialog.one 
            break
        if i==1: 
            Dialog=Dialog.two 
            break
        if i==2: 
            Dialog=Dialog.three 
            break
        if i==3: 
            Dialog=Dialog.four 
            break
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    option=create_button(Dialog.data[1:])
    for i in range(len(option)):
       markup.add(option[i])        
    bot.reply_to(message, Dialog.data[0], reply_markup=markup)
    print(Dialog.data[0])     

Dialog= Node(["Вы живете в Нижнем Новгороде или в Нижегородской области?","Нижний Новгород"],Node(["Вы знаете в какое ведомство нужно обратиться с Вашей проблемой?","да","нет"],Node(["Выберите ведомство","1","2"],Node(["выбрали1","назад"]),Node(["выбрали2","назад"])),    Node(["Опишите Вашу проблему.","назад"],Node(["назад"]))))

def create_button(buttons):
    Options=[]
    for i in range(len(buttons)):
        Option=telebot.types.KeyboardButton(buttons[i])
        Options.append(Option)
    return Options




bot.polling()

