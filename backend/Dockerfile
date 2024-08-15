FROM python:3.11

WORKDIR /app

ENV PYTHONUNBUFFERED=1\
PYTHONDONTWRITEBYTECODE=1\
POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update &&\
    apt-get install -y --no-install-recommends\
    curl &&\
    apt-get clean

run pip install --upgrade pip && pip install poetry

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry install --no-root

COPY . .

WORKDIR /app/app

EXPOSE 8000