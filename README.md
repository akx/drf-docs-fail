DRF docs bug test case
======================

Usage
-----

* Create and enter a virtualenv
* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py runserver`
* Navigate to http://127.0.0.1:8000/docs/; acquire *AttributeError*: 'Link' object has no attribute 'links'