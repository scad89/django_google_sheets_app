# django_google_sheets_app

Данное приложение помогает получать данные из таблиц Google Sheets, добавляя их в базу данных и выводя на страницу приложения в виде таблицы.

Для реализации использовался следующий стэк

```
cachetools
celery
Django
flake8
flower
google-api-python-client
google-auth
google-auth-httplib2
gunicorn
httplib2
Jinja2
lxml
oauth2client
pip-compile-multi
psycopg2
psycopg2-binary
pyflakes
python-dateutil
python-dotenv
pyasn1
pyasn1-modules
pycodestyle
redis
requests
rsa
six
sqlparse
uritemplate
xmltodict
```

## Установка и запуск(локально):

1. Скачать проект

   - git clone https://github.com/scad89/django_google_sheets_app.git

2. Добавить файл с переменными окружения(.env) в корень проекта(для получения файла отпишите мне на один из контактов ниже).

3. Активировать виртуальное окружение:

   - . venv_name/Scripts/activate - Windows
   - source venv_name/bin/activate - Linux

4. Установить зависимости(в виртуальном окружении):

   - pip install -r requirements.txt
   - pip-compile -U

5. Сделать миграции:

   - python manage.py makemigrations
   - python manage.py migrate

6. Запустить сервер:

   - python manage.py runserver

7. Запустить Celery в отдельном терминале:

   - celery -A django_sheets worker --beat --loglevel=info

8. Запустить flower в отдельном терминале:

- celery -A django_sheets flower --port=5555

```

http://127.0.0.1:8000 - страница приложения
http://127.0.0.1:5555 - flower для мониторинга процесса выполнения задач добавления данных из таблицы в базу данных

```

## Установка и запуск(docker-compose):

1. Добавить файл с переменными окружения(.env_docker) в корень проекта
2. Запустить командой:

```

- sudo docker-compose up -d

```

Если необходимо пересобрать контейнеры(внесли какие-то изменения) использовать:

```

- sudo docker-compose up --build

```

Если Вы запускаете проект на Windows, а docker из-под виртуальной машины(по типу VirtualBox), проект
по адресу 0.0.0.0:8000 может не открыться. Тогда необходимо использовать адрес 192.168.99.100:8000

Для остановки контейнеров используйте команду:

```

- docker-compose down

```

```

- http://0.0.0.0:8000 - страница приложения
- http://0.0.0.0:5555 - flower

```

### Описание реализации:

Приложение один раз в минуту получает данны из таблицы Goodle Sheet, где имеются колонки в виде №заказа, цена в $ срок поставки.
После приложение получает курс рубля на текующую дату и добавляет ещё и цену в рос. рубля. Затем все эти данные записываются в базу данных.
Если пользователю необходимо ознакомиться с актуальными данными из таблицы Google Sheet, он открывает страницу приложения, где они выводятся в следующем виде:
![](https://github.com/scad89/django_google_sheets_app/blob/main/image/browser.jpg)

Обновления актуальных данных из таблицы Google Sheet происходит один раз в минуту:
![](https://github.com/scad89/django_google_sheets_app/blob/main/image/flower_count.jpg)
![](https://github.com/scad89/django_google_sheets_app/blob/main/image/flower.jpg)

Ссылка на мой Google Sheets:
[Googe Sheets](https://docs.google.com/spreadsheets/d/1LrFj3Q8E_rcNCI3hGAA7qXm31mNQO8tJli7ThE8SuNg/edit#gid=0)

## Contacts

- Instagram: [@igor*komkov*](https://www.instagram.com/igor_komkov_/)
- Vk.com: [Igor Komkov](https://vk.com/zzzscadzzz)
- Linkedin: [Igor Komkov](https://www.linkedin.com/in/igor-komkov/)
- email: **scad200@gmail.com**
- Telegram: **@zzzSCADzzz**
