Django SecureAdmin
==================

``django-secureadmin`` is a package for secure your django administration.
How It Works ? it save real admin ip , after new logins it check new and last ip. if the last ip and new ip not equeals, it send email to user email and that email has verification code and date and ip of logged in user.
in the admin page , user see Login code text field and user shoud enter the login code in that field. then the secureadmin verify that and if it equals login code, then user enters the administration page.

Requirements
============

``django-secureadmin`` is tested on django-1.7 and works well. it require django-1.7 but may works in 1.6 (i not tested it)

Installation
============

You can install the latest stable package running this command::

    $ pip install django-secureadmin

Configuration
=============

First of all, you must add this project to your list of ``INSTALLED_APPS`` in
``settings.py``::
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'django-secureadmin',
        ...
    )

Next, install the ``ipcheck`` middleware::
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'secureadmin.middleware.ipcheck'
    )

Run ``python manage.py syncdb``.  This creates the appropriate tables in your database
that are necessary for operation.

Customizing SecureAdmin
-----------------------
You can customize SecureAdmin Email options and templates ,

* SECUREADMIN_MAILSUBJECT : the subject of emails sent from secureadmin , Default : Unusual sign in attempt prevented 
* SECUREADMIN_MAILFROM : define mail from option. Default : security@localhost
* SECUREADMIN_TEMPLATE : template for view when unusual login detected. its require for secureadmin work ! - in you template you should created a form , in the form you should have a input named code for login code input. you can check login code true or false. example : {% if errorcore %}<p style="color:red">login code false</p>{% endif %}  -- it login code true , it redirect to admin page.

