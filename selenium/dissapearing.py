import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Dissapearing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(by="link text", value="Disappearing Elements").click()
        #driver.find_element(by="xpath", value='/html/body/div[2]/div/div[2]/div/div[2]/div[1]/button').click()

    def test_name_element(self):
        driver = self.driver
        options = []
        menu = 5
        attempts = 1
        while len(options) < 5:
            options.clear()
            for i in range(menu):
                try:
                    option_name = driver.find_element(by="xpath", value=f'/html/body/div[2]/div/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i+1} is NOT FOUND")
                    attempts += 1
                    driver.refresh()
        print(f"Finished in {attempts} attempts")

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)