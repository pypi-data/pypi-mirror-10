
=============
Leonardo Auth
=============

Authentification backends for Leonardo, now supports

* https://github.com/pennersr/django-allauth
* https://bitbucket.org/lgs/djangosaml2/overview which is based on https://github.com/onelogin/python-saml

Installation
============

.. code-block:: bash

    pip install leonardo-module-auth

    # or as extras

    pip install django-leonardo[auth]

Next steps depends on your case

if you want use All Auth

.. code-block:: python

    # leonardo apps
    APPS += ['leonardo_module_oauth']

.. code-block:: bash

    python manage.py migrate

for more configuration providers visit http://django-allauth.readthedocs.org/en/latest/providers.html

or SAML standard

.. code-block:: bash

    pip install leonardo_module_auth[saml]

    pip install django-leonardo[saml]

.. code-block:: python

    APPS += ['leonardo_module_saml']
 
for SAML you must manually install SAML dependencies like this

note: installation depends on ``libxmlsec1-dev`` library

Read More
=========

* https://github.com/django-leonardo/django-leonardo
* http://django-leonardo.readthedocs.org/en/develop/overview/modules.html
* https://github.com/pennersr/django-allauth
* https://github.com/onelogin/python-saml
* https://bitbucket.org/lgs/djangosaml2/overview