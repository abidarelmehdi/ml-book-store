# pull official base image
FROM python:3.8-slim-buster

RUN mkdir book_store_ml
WORKDIR /book_store_ml
# install dependencies
COPY pyproject.toml .
RUN pip install pip -U
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
RUN python manage.py collectstatic --noinput