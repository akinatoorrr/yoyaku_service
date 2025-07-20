# Dockerfile
FROM python:3.12-slim

# 1) Poetry
ENV POETRY_VERSION=2.1.3
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
 && apt-get install --no-install-recommends -y curl \
 && pip install --upgrade pip \
 && pip install "poetry==$POETRY_VERSION"

WORKDIR /app/yoyaku

# 2) Копируем только конфиги зависимостей
COPY pyproject.toml poetry.lock /app/

# 3) Устанавливаем зависимости, НЕ ставя сам проект
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

# 4) Копируем весь код приложения
COPY . /app

EXPOSE 8000

# 5) Запуск Django
CMD ["sh", "-c", "gunicorn yoyaku.wsgi:application --bind 0.0.0.0:8000 --workers=${GUNICORN_WORKERS:-4} --access-logfile - --error-logfile -"]
