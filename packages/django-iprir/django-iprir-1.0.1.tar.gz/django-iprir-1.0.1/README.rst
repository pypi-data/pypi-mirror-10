=====
iprir
=====

iprir is a simple Django app to store and query information about Regional
Internet Registries like Top Level Domains and IP adresses.

Useful if you'd like to know where your visitors come from.


Quick start
-----------

1. Add "iprir" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'iprir',
    )

2. Include the iprir URLconf in your project urls.py like this::

    url(r'^iprir/', include('iprir.urls')),

3. Run `python manage.py migrate` to create the iprir models.

3. Run `python manage.py loadregistry` to import data.
