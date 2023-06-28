# floship_test

## This is a technical requirement for this project:
* Create two applications. (Store and Warehouse)
* (Store) One application should provide Orders (should be able to create order from admin page)
* (Warehouse) Another application should be able to receive these orders via the API and push back the information to the (Store).
* So when you create and order in Store, this should be synced to the Warehouse. If in warehouse you change some information this will update the information in Store (i.e. status)
* Make sure these applications can only communicate via Rest API and don't share a same database (two separate databases).


### The project was realized with Django fraemwork and Django Rest Fraemwork.

# Instruction:

Before the first run, you need to copy .env.dist to .env
If necessary, change the configuration of ports, logins, passwords, etc.
Download, install and run Docker
Run "make dev" command in console
If you have a Windows, then run the command instead of the previous command: docker compose up -d --build

### Create super user for both services in each service console with commands:

for store: python manage.py createsuperuser --settings=floship_test.settings.settings_store
for warehouse: python manage.py createsuperuser --settings=floship_test.settings.settings_warehouse


### With the existing .env

store admin site by the link http://localhost:8001/store/admin/
warehouse admin site by the link http://localhost:8002/warehouse/admin/

