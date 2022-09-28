import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#este script se encargará de añadir elementos y en caso tal de eliminarlos se dará click y se eliminarán

class RemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

    def test_remove_elements(self):
        driver = self.driver
        #elements_added = int(input('How many elements will you add? '))
        elements_added = 10
        #elements_removed = int(input('How many elements will you remove? '))
        elements_removed = 5
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(by="xpath", value='/html/body/div[2]/div/h3') 
        add_button.click()

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements than the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are 0 elements on screen")

if __name__ == "__main__":
    unittest.main(verbosity=2)        