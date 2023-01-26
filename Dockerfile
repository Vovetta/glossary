# Использование базового Docker-образа
FROM python:3.10-alpine

# Создание директории веб-приложения
RUN mkdir /app

# Объявление рабочей директории
WORKDIR /app

# Копирование файлов веб-приложения в контейнер
COPY . .

# Установка необходимых библиотек
RUN pip install wheel setuptools && pip install -r requirements.txt

# Запуск веб-приложения
CMD ["python", "main.py"]
