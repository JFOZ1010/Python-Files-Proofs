import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Search_Selenium(unittest.TestCase):

    #@classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        #pagina de selenium practice
        driver.get("http://demo-store.seleniumacademy.com")
        #driver.get_screenshot_as_png("http://demo-store.seleniumacademy.com", "selenium_practice.png")
        #driver.get_screenshot_as_file('/Screenshots/foo.png')
        driver.implicitly_wait(10)

    def search_tshirt(self):
        driver = self.driver
        search_field = driver.find_element(by="name", value="q")
        search_field.clear()
        search_field.send_keys("tee")
        search_field.submit()

        shirts = driver.find_elements(by="xpath", value='//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li[2]/div/h2/a')
        self.assertEqual(1, len(shirts))
    
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(by="name", value="q")
        search_field.clear()
        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements(by="xpath", value='//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        self.assertEqual(1, len(products)) #identifica si la cantidad de productos es 1 o no. 

    def test_search_text_field(self):
        #buscar con chromeDriverManger el elemento search
        pass
        #search_field = self.driver.find_element(by="id", value="search") #busca el elemento por id
        #search_field = self.driver.find_element(by="name", value="q") #busca el elemento por name

    #@classmethod
    def tearDownClass(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main(verbosity = 2)