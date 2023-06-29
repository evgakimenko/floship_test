FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8002
COPY . .
CMD python manage.py runserver --settings=floship_test.settings.settings_warehouse 0.0.0.0:8002