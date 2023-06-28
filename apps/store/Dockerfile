FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8001
COPY . .
CMD python manage.py migrate --settings=floship_test.settings.settings_store
CMD python manage.py runserver --settings=floship_test.settings.settings_store 0.0.0.0:8001