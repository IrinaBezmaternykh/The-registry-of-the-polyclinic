# The-registry-of-the-polyclinic
Простое веб-приложение на Flask
Это проект простого веб-приложения, написанного на фреймворке Flask языка Python.

Установка
Установите Python, если он не установлен. Его можно скачать с официального сайта.

Клонируйте репозиторий на локальную машину:

git clone https://github.com/DroidVedroid/TiSKPO_webapp_project
Перейдите в каталог с проектом:
cd TiSKPO_webapp_project
Установите виртуальное окружение
python -m venv venv
Активируйте виртуальное окружение Windows: venv\Scripts\activate Unix: source venv/bin/activate

Установите зависимости:

pip install -r requirements.txt
Запуск
Запустите приложение:
python app.py
Откройте браузер и перейдите по адресу http://localhost:5000 для просмотра приложения.
Для остановки веб-сервера используйте CTRL+C в командной строке.
Структура проекта
templates/: каталог, содержащий HTML-шаблоны;
static/: каталог, содержащий статические файлы, такие как CSS, JavaScript и изображения;
app.py: основной файл приложения, содержащий код Flask;
database.py: файл, содержащий настройки базы данных и создания экземпляра SQLAlchemy;
models.py: файл с определением структуры базы данных;
app.db: SQLite база данных проекта;
requirements.txt: файл, содержащий список зависимостей Python.
