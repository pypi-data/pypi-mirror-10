HitchDjango
===========

HitchDjango is a plugin for the Hitch test framework that lets you run and
interact with Django as part of a test.

When the plugin starts Django, *before* running runserver, it will:

* Check the version and fail if it is different to what is specified.
* Run migrations (using manage.py migrate).
* Get the URL using localhost + the specified port and put it in sites.site.
* Install all specified Django fixtures.

Currently HitchDjango runs only on Django 1.8 and above. Please raise a ticket
if you need an earlier version.

Use with Hitch
==============

Install like so::

    $ hitch install hitchdjango


.. code-block:: python

        # Service definition in engine's setUp:
        self.services['Django'] = hitchdjango.DjangoService(
            version="1.8",                                              # Mandatory
            python="{}/venv/bin/python".format(PROJECT_DIRECTORY),      # Mandatory
            managepy=None,                                              # Optional full path to manage.py (default: None, assumes in project directory)
            django_fixtures=['fixture1.json',],                         # Optional (default: None)
            port=18080,                                                 # Optional (default: 18080)
            settings="remindme.settings",                               # Optional (default: settings)
            needs=[self.services['Postgres'], ]                         # Optional (default: no prerequisites)
        )


        # Interact during the test:
        >>> self.services['Django'].manage("help").run()
        [ Prints help ]

        >>> self.services['Django'].url()
        http://127.0.0.1:18080/

        >>> self.services['Django'].savefixture("fixtures/database_current_state.json").run()
        [ Saves fixture ]


See this service in action at the DjangoRemindMe_ project.


.. _HitchServe: https://github.com/hitchtest/hitchserve
.. _DjangoRemindMe: https://github.com/hitchtest/django-remindme
