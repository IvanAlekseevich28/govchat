# Dockerfile

Этот Dockerfile используется для создания Docker-контейнера, в котором будет запущен телеграм-бот на Python.
Инструкции

1. Необходимо установить Docker на ваш компьютер. Для этого, перейдите по ссылке: https://docs.docker.com/get-docker/

2. Создайте новую папку и переместите туда Dockerfile, bot.py, bottoken.private и act.txt.

3. Соберите Docker-образ из Dockerfile командой:
```shell
docker build -t govchat_bot .
```

Здесь govchat_bot - это имя образа, которое вы выбираете.

4. Запустите Docker-контейнер командой:

```shell
docker run -d --name govchat_bot_container govchat_bot
```
Где govchat_bot_container - это имя контейнера, а govchat_bot - имя созданного образа.

Флаг -d означает, что контейнер будет запущен в фоновом режиме.

## Инструкции для Windows

1. Скачайте и установите Docker Desktop для Windows с официального сайта https://www.docker.com/products/docker-desktop

2. Откройте командную строку (cmd) и перейдите в папку с Dockerfile, bot.py, bottoken.private и act.txt.

3. Выполните команды из предыдущего раздела.

## Инструкции для Linux

1. Установите Docker с помощью менеджера пакетов вашего дистрибутива. Например, для Ubuntu:

```shell
sudo apt-get update
sudo apt-get install docker.io
```

2. Откройте терминал и перейдите в папку с Dockerfile, bot.py, bottoken.private и act.txt.

3. Выполните команды из предыдущего раздела.