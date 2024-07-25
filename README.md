# Лэндинг Страница - Start Bootstrap Theme

Этот проект представляет собой лэндинг страницу, созданную с использованием Django и Bootstrap.

## Функции

- Навигация с использованием Bootstrap
- Карусель изображений
- Карточки продуктов
- Секций для демонстрации оптических приборов и измерительного оборудования
- Вызов к действию и футер

## Установка

Следуйте этим шагам для установки и запуска проекта на вашем локальном компьютере:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/username/repository-name.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd repository-name
    ```

3. Создайте виртуальную среду и активируйте её:
    ```bash
    python -m venv env
    source env/bin/activate  # Для Windows: env\Scripts\activate
    ```

4. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

5. Выполните миграции базы данных:
    ```bash
    python manage.py migrate
    ```

6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

7. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000` для просмотра сайта.

## Использование

В проекте используются следующие ключевые технологии и библиотеки:

- **Django**: Веб-фреймворк на языке Python
- **Bootstrap**: Фреймворк для создания адаптивных веб-сайтов
- **JavaScript**: Для функционала карусели и формы

### Основные файлы

- `index.html`: Главная страница проекта
- `styles.css`: Стили для страницы
- `scripts.js`: Скрипты для страницы

### Структура папок

project/
│
├── media/
│ ├── img/
│ │ ├── ZEISS Axio.jpg
│ │ ├── факометр-lensmeter.jpg
│ │ ├── schott-obsh_2.jpg
│ │ ├── Trimble 3d scanning total station_1.jpg
│ │ ├── Nd-YAG_Crystal_1.jpg
│ │ ├── ZEISS Spectrometer.jpg
│ │ ├── High Homogeneity Glass.jpg
│ │ ├── Leica 3d disto.jpg
│ │ ├── 123-shot.png
│ │ ├── Nd-YAG1.png
│ │ └── ...
│
├── static/
│ ├── css/
│ │ ├── styles.css
│ │ └── favicon.ico
│ └── js/
│ └── scripts.js
│
├── templates/
│ └── index.html
│
├── requirements.txt
├── manage.py
└── ...


## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по электронной почте: ufukkirmizigedik1984@gmail.com
