FROM python:3

COPY . /app
WORKDIR /app

RUN pip install uwsgi flask
CMD ["uwsgi", "--ini", "uwsgi.ini"]