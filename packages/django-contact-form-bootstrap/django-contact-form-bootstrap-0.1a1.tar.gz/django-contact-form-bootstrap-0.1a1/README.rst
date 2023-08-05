######
README
######

Twitter Bootstrap templates for `django-contact-form
<https://bitbucket.org/ubernostrum/django-contact-form/>`_.


Requirements
============

* Python 2.7 or >=3.3.
* Django >=1.6


Installation
============

Installation via::

   pip install django-contact-form-bootstrap==0.1a1

The templates extend ``base.html``, so the ``templates`` folder of the
project should provide one, together with the Twitter Bootstrap and a JQuery
library.

Then add ``'bootstrapform'`` and ``'contact_form_bootstrap'`` to
``INSTALLED_APPS``, *before* ``'contact_form'``.  The order is important
because following apps are overwritten::

   INSTALLED_APPS = (
       # ...
       'django.contrib.sites',  # For ``contact_form``.

       'bootstrapform',
       'contact_form_bootstrap',
       'contact_form',
       # ...
   )

For ``contact_form`` itself, remember to add the following settings::

   SITE_ID = 1


Example Project
===============

The example project can be run to have a quick look and to check out a
running setup. Download the source files and run::

   virtualenv -p /usr/bin/python3 ~/myenv
   source ~/myenv/bin/activate
   pip install -r requirements.txt
   ./manage.py migrate
   ./manage.py runserver


Customization
=============

To use custom templates, there are two ways to accomplish that:

1. Overwrite a template at ``templates/contact_form`` to replace them completely.
2. Inherit a template from ``templates/contact_form`` to overwrite only one or
   more of its blocks. Defining a custom URL pointing at the custom template is
   necessary then.
