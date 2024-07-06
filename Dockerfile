# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы приложения в контейнер
COPY . /app
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt 

# Определяем переменные окружения
ENV FLASK_APP=main.py

ENV FLASK_RUN_HOST=0.0.0.0

# Указываем порт, который будет использовать Flask
EXPOSE 5000

# Команда для запуска Flask-приложения
CMD ["flask", "run"]