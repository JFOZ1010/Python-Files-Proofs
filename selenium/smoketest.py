from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from Assertion import AssertionTest
from test_search_page import Search_Selenium

assertionTest = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(Search_Selenium)

smoke_test = TestSuite([assertionTest, search_test])
#
kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test) #ejecuta el test