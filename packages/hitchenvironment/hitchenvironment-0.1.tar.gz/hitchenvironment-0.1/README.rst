HitchEnvironment
================

HitchEnvironment is a plugin for the Hitch testing framework that lets you
describe your environment and verify that it correct.

It is supposed to provide some measure of safety for tests that might pass on,
for example, a 64 bit machine but fail on a 32 bit machine, by making
the environment a test runs on declared explicitly.

It is required by HitchServe_ to run, requiring you to specify your
environment.

Currently, it lets you describe the following:

* Platform (linux2, win32, cygwin, darwin, os2, os2emx, riscos, atheos)
* System bits (32 or 64)
* Access to internet (True or False)



Use with Hitch
==============

Install like so::

    $ hitch install hitchenvironment


.. code-block:: python

        >>> import hitchenvironment
        >>> hitchenvironment.class_definition()
        hitchenvironment.Environment(platform="linux2", systembits=64, requires_internet_access=True)

        >>> hitchenvironment.Environment(platform="linux2", systembits=64, requires_internet_access=True).match()



See this plugin in action at the DjangoRemindMe_ project.


.. _HitchServe: https://github.com/hitchtest/hitchserve
.. _DjangoRemindmMe: https://github.com/hitchtest/django-remindme
