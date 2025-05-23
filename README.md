# 🧠 CRM System

Добро пожаловать в кастомную CRM-систему, разработанную для управления клиентами, заявками и сотрудниками. Этот проект построен с использованием **Django** на бэкенде и включает в себя структуру для простой интеграции с фронтендом (ссылка ниже).

## 🚀 Особенности

- Управление клиентами (CRUD)
- Управление заявками
- Авторизация и аутентификация пользователей
- Админ-панель на Django
- Простая настройка и запуск

## 🧰 Технологии

- Python 3.x
- Django
- SQLite (по умолчанию)
- HTML/CSS/JavaScript
- Bootstrap (если применимо)
- (Фронтенд: [MMA-Front](https://github.com/beknazar93/MMA-Front) — React)

## 📦 Установка и запуск

1. Клонируй репозиторий:

   ```bash
   git clone https://github.com/beknazar93/CRM.git
   cd CRM
Создай и активируй виртуальное окружение:

bash
Копировать
Редактировать
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
Установи зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Применяй миграции:

bash
Копировать
Редактировать
python manage.py migrate
Запусти сервер:

bash
Копировать
Редактировать
python manage.py runserver
Перейди в браузер: http://127.0.0.1:8000/

🔐 Доступ в админку
Создай суперпользователя:

bash
Копировать
Редактировать
python manage.py createsuperuser
📂 Структура проекта
bash
Копировать
Редактировать
crm_project/
├── crm/                # Основное Django-приложение
├── staticfiles/        # Статика
├── db.sqlite3          # База данных
├── manage.py
├── requirements.txt
📌 Заметки
Проект находится на стадии активной разработки.

Фронтенд находится в отдельном репозитории: MMA-Front

🧙 Автор
Разработано с утомлением и бессонницей: beknazar93
