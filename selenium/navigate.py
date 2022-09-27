import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Navigate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element(by="name", value="q")
        search_field.clear()

        search_field.send_keys("platzi")
        search_field.submit()

        #hacer scroll
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #driver.find_element(by="link text", value="Imágenes").click()
        
        #ingresar al sitio de platzi por la url
        platzi_click = driver.get("https://platzi.com")

        search_platzi = driver.find_element(by="class name", value="NewSearch-input")
        search_platzi.click()
        search_platzi.send_keys("python Django")
        search_platzi.submit()
        sleep(3)
        #driver.back() #regresa a la pagina anterior
        #driver.forward() #avanza a la pagina siguiente
        #driver.refresh() #refresca la pagina

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)