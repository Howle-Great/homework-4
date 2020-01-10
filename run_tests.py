import sys
import unittest

from tests.LoginTest import LoginTest
from tests.SettingsTest import SettingsTest
from tests.MainTest import MainTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest)
        unittest.makeSuite(SettingsTest)
        unittest.makeSuite(MainTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
