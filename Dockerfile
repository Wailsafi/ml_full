FROM python:3.11.5

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:${PORT:-8000} app:app
