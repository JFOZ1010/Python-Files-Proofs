import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Prueba(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.netflix.com/co/login")
    driver.find_element(by="id", value="email").send_keys("juan10@gmail.com")
    #driver.find_element(by="email").send_keys("juan10@gmail.com")
    #driver.("password").send_keys("12345678")
    driver.implicitly_wait(10)
    driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)