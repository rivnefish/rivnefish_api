1)  At first install Django

```
pip install  django
```

2)  Next

```
pip install djangorestframework
```

3)  Next

```
pip install django-filter
```

4)  Install MySQldb

```
sudo apt-get install python-dev
pip install mysql-python
```

5)  Run project server

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


# Runbooks 

## If API is not avaliable  
by URL http://api.rivnefish.com/admin/site_manager/markers/97/

1) Next strings should be added into httpd.conf :

```
cat /usr/local/directadmin/data/users/rivnefish/httpd.conf

WSGIPythonPath /usr/home/rivnefish/domains/api.rivnefish.com/rivnefish-env/lib/python2.7/site-packages

<VirtualHost api.rivnefish.com:80>
    ServerAdmin webmaster@localhost
    ServerName api.rivnefish.com
    WSGIScriptAlias / /usr/home/rivnefish/domains/api.rivnefish.com/rivnefish/RivneFish/wsgi.py
    CustomLog /var/log/httpd/domains/api.rivnefish.com.log homedir
    ErrorLog /var/log/httpd/domains/api.rivnefish.com.error.log
    WSGIPassAuthorization On
</VirtualHost>

<VirtualHost 77.120.80.6:80 >
        ServerName www.www2.rivnefish.com
        ServerAlias www.www2.rivnefish.com www2.rivnefish.com
```

2) Restart httpd process
