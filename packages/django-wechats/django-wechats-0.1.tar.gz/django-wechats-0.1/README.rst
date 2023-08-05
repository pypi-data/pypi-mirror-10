=====
Django-wechats
=====

Django-wechats is a wrapper for wechat API.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'app',
    )

2. Include the app URLconf in your project urls.py like this::

    url(r'^app/', include('app.urls')),

3. Run `python manage.py migrate` to create the app models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a app (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/app/ to participate in the app.