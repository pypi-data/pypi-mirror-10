HitchCelery
===========

HitchCelery is a plugin for the Hitch test framework that lets you run and
interact with Celery as part of a test.


Use with Hitch
==============

Install like so::

    $ hitch install hitchcelery


.. code-block:: python

        # Service definition in engine's setUp:
        self.services['Celery'] = hitchcelery.CeleryService(
            version="3.1.17",                                       # Mandatory
            python="{}/venv/bin/python".format(PROJECT_DIRECTORY),  # Mandatory
            app="remindme",                                         # Mandatory
            beat=False,                                             # Optional (default: False)
            concurrency=2,                                          # Optional (default: 2)
            loglevel="INFO",                                        # Optional (default: INFO)
            broker=None,                                            # Optional (default: None)
            needs=[ self.services['Redis'], ]                       # Optional (default: no prerequisites)
        )


        # Interact during the test:
        self.services['Celery'].help().run()
        [ Prints output ]

        self.services['Celery'].status().run()
        [ Prints status output ]

        self.services['Celery'].control(*args).run()
        [ Prints output ]

        self.services['Celery'].inspect(*args).run()
        [ Prints output ]


See this service in action at the DjangoRemindMe_ project.


.. _HitchServe: https://github.com/hitchtest/hitchserve
.. _DjangoRemindMe: https://github.com/hitchtest/django-remindme

