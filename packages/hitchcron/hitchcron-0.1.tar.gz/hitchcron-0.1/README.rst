HitchCron
=========

HitchCron is a plugin for the Hitch test framework that lets you mimic
the effect of having a cron run during your tests by running a command
repeatedly.


Use with Hitch
==============

Install like so::

    $ hitch install hitchcron

.. code-block:: python

        # Service definition in engine's setUp:
        self.services['Cron'] = hitchcron.CronService(
            run=self.services['Django'].manage("trigger").command,      # Python list containing command + args
            every=1,                                                    # Run every 1 seconds
        )

See this service in action at the DjangoRemindMe_ project.


.. _HitchServe: https://github.com/hitchtest/hitchserve
.. _DjangoRemindMe: https://github.com/hitchtest/django-remindme
