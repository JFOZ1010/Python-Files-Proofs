from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from google_page import GooglePage

@classmethod
class TestGoogle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_google(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')
        self.assertEqual('Platzi', google.keyboard)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)

