import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
    
    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(by="name", value="q")
        search_field.clear()


        search_field.send_keys("tee")
        search_field.submit()
        driver.find_element(by="class name", value="link-compare").click()
        driver.find_element(by="link text", value="Clear All").click()

        alert = driver.switch_to_alert() #switch_alert() es un metodo que nos permite cambiar de ventana   
        alert_text = alert.text

        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
        alert.accept() #para ejecutar el test, en la terminal escribir: python3 -m unittest -v selenium/alerts_popup.py  
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

