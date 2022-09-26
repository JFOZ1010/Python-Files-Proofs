import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AssertionTest(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.implicitly_wait(10)

    def test_search_field(self):
        #self.driver.get("http://demo-store.seleniumacademy.com")

        # Verificar si el elemento esta presente en la pagina
        self.assertTrue(self.is_element_present(By.NAME, "q"))

        # Verificar si el elemento esta presente en la pagina
        self.assertTrue(self.is_element_present(By.NAME, "btnK"))

    def test_language_option(self):
        #self.driver.get("http://demo-store.seleniumacademy.com")

        # Verificar si el elemento esta presente en la pagina
        self.assertTrue(self.is_element_present(By.ID, "select-language")) #el id se llama select-language y asi es como lo añadimos.

    def is_element_present(self, how, what): #how es el tipo de elemento, y what es el valor del elemento
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

    
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)