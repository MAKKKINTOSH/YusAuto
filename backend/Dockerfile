FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update &&\
    apt-get install -y --no-install-recomends\
    curl &&\
    apt-get clean

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry install --no-root

WORKDIR /app/src

COPY --exclude="./venv" ./src ./

EXPOSE 8000