# investing

Команды для работы с проектом:
1. `pip install -r requirements.txt` - установка зависимостей
2. `python manage.py migrate` - накатывание миграций в БД
3. `python manage.py add_shares` - добавление акций через managment_command
4. `celery -A config beat`  - запуск Celery Beat (for cron)
5. `celery -A config worker -l INFO`  - запуск Celery
6. `python manage.py runserver` - запуск приложения
7. `python manage.py сreatesuperuser` - создание суперпользователя
8. `python manage.py test` - запуск тестов

Базу данных можно использовать файловую SQLITE3 или PostgreSQL. Для использования PostrgreSQL запустить БД в Docker

Необходимо указать TINKOFF_TOKEN для работы приложения

Основные маршруты приложения:
1. `http://127.0.0.1:8000` - Главная страницы
2. `http://127.0.0.1:8000/api/v1/shares/` - OpenApi 
3. `http://127.0.0.1:8000/admin` - Стандартная админка Django, можно авторизоваться под суперпользователем.