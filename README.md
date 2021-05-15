# Hotel Booking System

Description to this project [here](https://github.com/tolegenovbt/HotelBookingSystem/)
   
## Setups
```
pip install virtualenvwrapper
mkvirtualenv yourOptinallyEnvironmentName
workon yourOptinallyEnvironmentName
pip install -r requirements.txt
```

## PostgreSQL

1. Install [PostgreSQL](https://www.postgresql.org/download/)
2. Start SQL Shell
3. Enter 5 times <kbd>Enter</kbd>
4. Create database:
```
    create database your_optionally_database_name;
    create user user_name with password 'default';
    grant all privileges on database your_optionally_database_name to user_name;
```
5. Change database settings in settings.py:
 ```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_optionally_database_name',
        'USER': 'user_name',
        'PASSWORD': 'default',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
 ```
 6. Run your project


## Postman Import

Link to postman collection is [here](https://www.getpostman.com/collections/e6e8a607e899ae5d61b7)

1. Run ***Postman***
2. <kbd>Ctrl</kbd> + <kbd>O</kbd> or ***File -> Import***
3. Enter tab Link
4. <kbd>Ctrl</kbd> + <kbd>V</kbd> 
5. Enter ***Continue***

## Run

```
python manage.py makemigrations
python manage.my migrate
python manage.py runserver
```
Run Postman or visit [localhost](http://localhost:8000) to view the app.


## Clone the repository

[git repository](https://github.com/tolegenovbt/HotelBookingSystem/):
 * `git clone git://github.com/tolegenovbt/HotelBookingSystem.git`

