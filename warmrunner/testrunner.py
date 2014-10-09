"""
Testrunner that shows the tests that took longest to execute.

See README in the same package.
"""

from operator import itemgetter
import re
import time
from unittest import TextTestResult, TextTestRunner

from django.test.runner import DiscoverRunner


class WarmTestRunner(DiscoverRunner):
    """
    * If tests are run with --verbosity=2 or higher, the time taken to
      run each test will be displayed in microseconds.
    * In any case, at the end the time taken by the slowest tests will be
      printed.
    """

    def run_suite(self, suite, **kwargs):
        return _TimeLoggingTestRunner(
            verbosity=self.verbosity,
            failfast=self.failfast
        ).run(suite)


class TimeLoggingTestResult(TextTestResult):

    def __init__(self, *args, **kwargs):
        super(TimeLoggingTestResult, self).__init__(*args, **kwargs)
        self.test_times = []

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            test = re.findall('[\w_]+', str(test))
            template = '{testname} ({app}.{suite}.{testname})'
            return template.format(app=test[1], suite=test[-1], testname=test[0])

    def startTest(self, test):
        self.case_start_time = time.time()
        super(TimeLoggingTestResult, self).startTest(test)

    def addSuccess(self, test):
        self.case_time_taken = time.time() - self.case_start_time
        if self.showAll:
            self.stream.write("(%0.6fs) " % self.case_time_taken)
        self.test_times.append((self.case_time_taken, test))
        super(TimeLoggingTestResult, self).addSuccess(test)

    def addFailure(self, test, err):
        self.case_time_taken = time.time() - self.case_start_time
        if self.showAll:
            self.stream.write("(%0.6fs) " % self.case_time_taken)
        self.test_times.append((self.case_time_taken, test))
        super(TimeLoggingTestResult, self).addFailure(test, err)

    def addError(self, test, err):
        self.case_time_taken = time.time() - self.case_start_time
        if self.showAll:
            self.stream.write("(%0.6fs) " % self.case_time_taken)
        self.test_times.append((self.case_time_taken, test))
        super(TimeLoggingTestResult, self).addError(test, err)

    def addUnexpectedSuccess(self, test):
        self.case_time_taken = time.time() - self.case_start_time
        if self.showAll:
            self.stream.write("(%0.6fs) " % self.case_time_taken)
        self.test_times.append((self.case_time_taken, test))
        super(TimeLoggingTestResult, self).addUnexpectedSuccess(test)

    def addSkip(self, test, reason):
        self.case_time_taken = time.time() - self.case_start_time
        self.test_times.append((self.case_time_taken, test))
        super(TimeLoggingTestResult, self).addSkip(test, reason)

    def addExpectedFailure(self, test, err):
        self.case_time_taken = time.time() - self.case_start_time
        if self.showAll:
            self.stream.write("(%0.6fs) " % self.case_time_taken)
        self.test_times.append((self.case_time_taken, test))
        super(TimeLoggingTestResult, self).addExpectedFailure(test, err)

    def startTestRun(self):
        self.run_start_time = time.time()
        super(TimeLoggingTestResult, self).startTestRun()

    def stopTestRun(self):
        run_time_taken = time.time() - self.run_start_time
        super(TimeLoggingTestResult, self).stopTestRun()

        if self.test_times:
            # Top 10, if we have 10
            test_times = sorted(self.test_times, key=itemgetter(0), reverse=True)[:10]
            print("\nTop %d test times:" % len(test_times))
            for test_time, test in test_times:
                print("%0.6fs %s" % (test_time, test.id()))


class _TimeLoggingTestRunner(TextTestRunner):
    resultclass = TimeLoggingTestResult


