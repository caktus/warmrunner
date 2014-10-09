Testrunner that shows the tests that took longest to execute.

Adapted from https://bitbucket.org/metametrics/django-hotrunner by:

* Use Django 1.7 test runner as base runner class
* remove XML output feature
* print the longest-running tests at the end

Might require Django 1.7 and Python > 2.6 (2.7 or 3.*).

To use, 

* Install this package
* modify your Django settings with

        TEST_RUNNER = 'warmrunner.WarmRunner'

* run your tests as usual with 'python manage.py test [options] [args]'
