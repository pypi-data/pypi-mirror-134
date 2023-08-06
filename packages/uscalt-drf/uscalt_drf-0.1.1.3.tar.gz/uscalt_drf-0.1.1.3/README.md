# **Uscalt-DRF**

Uscalt-DRF is a library for Django-Rest-Framework backend servers to allow you to control the data retrieval process rather than Uscalt.

To install using `pip`:
```
pip install uscalt-django
```

----------
# Quick start


1. Add "uscalt-drf" to your INSTALLED_APPS setting:
```python
    INSTALLED_APPS = [
        ...
        'uscalt-drf.apps.UscaltDRFConfig',
    ]
```
2. Include the uscalt-drf URLconf in your project urls.py:
```python
    path('', include('uscalt-drf.urls')),
```
3. Run `python manage.py migrate`.

4. We need to send the key to the user to decrypt the file and to do this we use email. You'll need to set these variables in settings:
```python
EMAIL_HOST = 'smtp.XXXX.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'EMAIL@HOST.com'
EMAIL_HOST_PASSWORD = 'XXXXXX'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False 
```
Don't worry, this is a standard library. We have not created our own email sending code or handle your details.

----
# Allowing users to upload data

Allowing users to upload data is straightforward. In fact, so long as you set your email, Uscalt takes care of the rest!

----
# Creating a dataset from data stored on a database

This is for links that were created using the 'Use data from cloud database (not local devices)' option. This will require you to define how to retrieve the data from a given list of user identifiers. 

You'll need to create a file called `uscalt.py` in **every app that contains data needed by a Room Link**. Instantiate a class and define each data retrieval function with the uscalt_task decorator. (The name of the class is not important)

```python
from uscalt_drf.utils import uscalt_task
from .models import running_model

class Uscalt:

    @uscalt_task
    def Running(identifiers):
        data = running_model.objects.filter(pk__in=identifiers)

        return data
```