Testrunner that shows the tests that took longest to execute.

Adapted from https://bitbucket.org/metametrics/django-hotrunner by:

* Use Django 1.7 test runner as base runner class
* remove XML output feature
* print the longest-running tests at the end

Might require Django 1.7 and Python > 2.6 (2.7 or 3.*). I've only
tried it with Django 1.7 and Python 2.7 so far.

To use, 

* Install this package
* Modify your Django settings with

        TEST_RUNNER = 'warmrunner.WarmRunner'

* Run your tests as usual with 'python manage.py test [options] [args]'


LICENSE:

The code this was adapted from was copyright Metametrics and under the
BSD license:

Copyright (c) 2012, MetaMetrics Inc
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Changes are Copyright (c) 2014, Caktus Group Inc. and also under the same BSD license.
