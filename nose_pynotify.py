"""
This module implements a pynotify-based notification system for nose tests.
Please see README.md for licensing info, an installation guide, and usage.
"""

import pynotify
import os
import sys

from nose.plugins import Plugin

class PyNotify(Plugin):
  """Subclass of nose.plugins.Plugin that displays a notification at the end
  of test suites, whenever enabled."""

  enabled = False
  name = "pynotify"
  score = 2

  def __init__(self):
    """Constructor"""
    # Run parent class' constructor
    super(PyNotify, self).__init__()

    # Generate msg title
    self.cwd = os.getcwd()

  def addError(self, test, err):
    """Called upon encountering an error"""
    # Display error msg
    title = test.shortDescription() or self.cwd
    n = pynotify.Notification(title,
            "Error: " + str(err[0].__name__) +
            "\n" + str(err[1]), 'gtk-no')
    n.show()

  def addFailure(self, test, err):
    """Called upon encountering a failure"""
    # Display failure msg
    title = test.shortDescription() or self.cwd
    n = pynotify.Notification(title,
            "Failed: " + str(err[0].__name__) +
            "\n" + str(err[1]), 'gtk-no')
    n.show()

  def begin(a):
    """Called before running any tests, used for initialization"""
    # Initialize pynotify
    pynotify.init(os.getcwd())

  def options(self, parser, env):
    """Called to allow plugin to register command line options with the parser."""
    # TODO: add option to of avoiding individual error/failure notifications
    Plugin.options(self, parser, env)

  def finalize(self, result):
    """Called upon the completion of all tests"""
    # Grab numbers of types of test results
    errors = len(result.errors)
    failures = len(result.failures)
    successes = result.testsRun - errors - failures

    # Choose icon
    icon_name = "gtk-yes" if result.wasSuccessful() else "gtk-no"

    # Generate and show the message at the end of the test
    msg = "%s success%s, %s error%s, %s failure%s"
    n = pynotify.Notification(self.cwd,
                              msg % (successes,
                                     self.plural(successes, special=True),
                                     errors,
                                     self.plural(errors),
                                     failures,
                                     self.plural(failures)),
                              icon_name)
    n.show()    

  def plural(self, n, special=False):
    """Returns empty string if n == 1, otherwise the 's' needed as a suffix"""
    suffix = "s" if not special else "es"
    return suffix if (n == 0 or n > 1) else ""
