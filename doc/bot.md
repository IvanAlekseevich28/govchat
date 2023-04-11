# Описание кода чат-бота на Telegram

bot.py основной код телеграм бота @GovChat23_bot, который будет отвечать на вопросы пользователей.
## Импорт библиотеки

```python
import telebot
```
Мы импортируем библиотеку telebot, которая позволяет создавать чат-ботов для Telegram.
## Получение токена

```python
with open('bottoken.private', 'r') as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)
```
Мы открываем файл bottoken.private, в котором хранится токен нашего бота, и сохраняем его в переменную token. Затем мы создаем объект TeleBot с помощью этого токена.
## Загрузка ответов из файла

```python

with open('act.txt', 'r') as f:
    lines = f.readlines()
    answers = {}
    for i in range(0, len(lines), 3):
        key = lines[i].rstrip('\n').lower()
        value = lines[i+1].rstrip('\n')
        answers[key] = value
```
Мы открываем файл act.txt, в котором хранятся пользовательские сценарии, и загружаем их в словарь answers. Ключом в словаре является вопрос, а значением - ответ.
## Главное меню

```python

with open('menu.txt', 'r') as f:
    menu_lines = f.readlines()
    menu_options = [option.rstrip('\n') for option in menu_lines]

menu_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu_markup.add(*[telebot.types.KeyboardButton(btn_name) for btn_name in menu_text.split("\n")])
```
Мы открываем файл menu.txt, в котором хранятся текст и названия кнопок для главного меню, и загружаем его в переменную menu_text. Затем мы создаем объект ReplyKeyboardMarkup, который позволяет создать главное меню с несколькими кнопками. Каждая кнопка создается с помощью класса KeyboardButton и добавляется в объект menu_markup.
## Обработка команды /start

```python

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Добрый день, я чат-бот по Нижнему Новгороду. Чем я могу вам помочь?', reply_markup=start_menu)

```
Мы создаем функцию start, которая вызывается, когда пользователь отправляет команду /start. Она отправляет сообщение "Здравствуйте! Чем я могу вам помочь?".
## Обработка сообщений

```python

@bot.message_handler(func=lambda message: True)
def reply(message):
    user_phrase = message.text.lower()
    bot_answer = answers.get(user_phrase, 'Простите, не смог обработать ваш текущий запрос.')
    if user_phrase == menu_options[-1].lower():
        bot_answer = 'Чем я могу вам помочь? Выберите опцию.'
        bot.send_message(message.chat.id, bot_answer, reply_markup=start_menu)
    else:
        bot.reply_to(message, bot_answer, reply_markup=start_menu)
```
Эта функция отвечает за обработку всех сообщений, которые отправляет пользователь боту. Функция начинается с получения текста сообщения пользователя в нижнем регистре и поиска соответствующего ответа в словаре answers. Если ответ не найден, бот отправляет стандартное сообщение "Простите, не смог обработать ваш текущий запрос.".

Затем функция проверяет, соответствует ли сообщение, которое отправил пользователь, последней опции в главном меню. Если да, то бот отправляет сообщение "Чем я могу вам помочь? Выберите опцию." и показывает главное меню. Если сообщение пользователя не соответствует последней опции в главном меню, бот отправляет соответствующий ответ и показывает главное меню.

Функция также использует параметр reply_markup, который указывает, какую клавиатуру использовать при отправке сообщения. В этом случае мы используем start_menu, который определен выше в коде.

## Запуск бота

```python

bot.polling()
```

Мы запускаем бота с помощью функции polling(). Бот будет ожидать новых сообщений и обрабатывать их, пока мы не остановим выполнение программы.