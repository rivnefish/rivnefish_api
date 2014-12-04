1)  At first install Django

```
pip install  django
```

2)  Next

```
pip install djangorestframework
```

3)  Run project server

```
python manage.py runserver 0.0.0.0:8000
```

# Using virtualenv (ubuntu)

```
sudo apt-get install python-pip
sudo pip install virtualenv

# create virtualenv
virtualenv rivnefish-env

# activate rivnefish-env
source rivnefish-env/bin/activate

# now you can install required packages
pip install -r requirements.txt

# apply migrations
python manage.py migrate

```

## Recommend to add

**Django Extensions** https://github.com/django-extensions/django-extensions

**Shell plus** https://github.com/django-extensions/django-extensions/blob/master/docs/shell_plus.rst
