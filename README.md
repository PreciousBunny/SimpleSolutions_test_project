# SimpleSolutions_test_project
Тестовое задание.

## Задача

· 	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
· 	Django Модель Item с полями (name, description, price)
· 	API с двумя методами:
· 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
· 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

## Выполненные бонусные задачи
· 	Использование environment variables
· 	Просмотр Django Моделей в Django Admin панели

## Развертывание проекта
Для корректной работы проекта, вам необходимо выполнить следующие шаги:

1) Установить локально на свой компьютер Python версией не ниже 3.10.x!
2) Клонировать файлы проекта с GitHub репозитория.
3) Установите виртуальное окружение.
```bash
python3 -m venv venv
```
4) Активировать виртуальное окружение (если есть необходимость).
```bash
venv/Scripts/activate (Windows)
```
```bash
source venv/bin/activate (Linux, MacOS)
```
5) Установить необходимые зависимости проекта, указанные в файле `requirements.txt`
```bash
pip install -r requirements.txt
```
6) Установить Redis, глобально себе на компьютер (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install redis-server
```
7) Запустить Redis-сервер (Redis-сервер запустится на стандартном порту 6379).
```bash
sudo service redis-server start
```
8) Убедиться, что Redis-сервер работает правильно, выполните команду:
```bash
redis-cli ping
```
9) Установить БД PostreSQL (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install postgresql
```
10) Если БД PostreSQL уже была ранее установлена, то перезапустите сервер PostreSQL.
```bash
sudo service postgresql restart
```
11) Выполнить вход.
```bash
sudo -u postgres psql
```
12) Создать базу данных с помощью следующей команды:
```bash
create database item;
```
Если такая база данных уже используется, то возможно изменить ее название на свою.

13) Выйти.
```bash
\q
```
14) Создать файл .env
15) Добавить в файл настройки, как в .env.sample и заполнить их.
16) Применить миграции (локально, у себя в виртуальном окружении проекта).
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
17) Загрузить данные в созданную таблицу БД с помощью команды:
```bash
python manage.py create_data
```
18) Запустить сервер (появившуюся ссылку открыть в браузере  http://127.0.0.1:8000/ )
```bash
python manage.py runserver
```