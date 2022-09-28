import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30) #espera implicita de 30 segundos, para que cargue la pagina
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_new_user(self):
        driver = self.driver
        driver.find_element(by="xpath", value='/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click() #se hace un click para que se desplieuge.
        driver.find_element(by="link text", value='Log In').click() #se hace un click para que se desplieuge.

        submit_button = driver.find_element(by="xpath", value='/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span') #se hace un click para que se desplieuge.
        self.assertTrue(submit_button.is_displayed() and submit_button.is_enabled()) #se verifica que el boton este habilitado y visible.   
        submit_button.click() #hacemos click en el boton de crear cuenta

        #utilizar typos para encontrar title
        self.assertEqual('Create New Customer Account', driver.title) #verificamos que el titulo sea el correcto

        #vamos a escribir en cada uno de los campos de texto: 
        #first name
        first_name = driver.find_element(by="id", value="firstname")
        self.assertTrue(first_name.is_enabled() and first_name.is_displayed())
        first_name.send_keys("Test")
        #middle name
        middle_name = driver.find_element(by="id", value="middlename")
        self.assertTrue(middle_name.is_enabled() and middle_name.is_displayed())
        middle_name.send_keys("Test2")
        #last name
        last_name = driver.find_element(by="id", value="lastname")
        self.assertTrue(last_name.is_enabled() and last_name.is_displayed())
        last_name.send_keys("Apellido_Test3")
        #email
        email = driver.find_element(by="id", value="email_address")
        self.assertTrue(email.is_enabled() and email.is_displayed())
        email.send_keys("testSelenium20222@platzi.com")
        #password
        password = driver.find_element(by="id", value="password")
        self.assertTrue(password.is_enabled() and password.is_displayed())
        password.send_keys("1235")
        #confirmation password
        confirmation_password = driver.find_element(by="id", value="confirmation")
        self.assertTrue(confirmation_password.is_enabled() and confirmation_password.is_displayed())
        confirmation_password.send_keys("1235")
        #click en el boton de registrarse
        submit_button = driver.find_element(by="xpath", value='/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')
        self.assertTrue(submit_button.is_displayed() and submit_button.is_enabled()) #se verifica que el boton este habilitado y visible.
        submit_button.click() #hacemos click en el boton de crear cuenta


    def tearDown(self):
        self.driver.implicitly_wait(60)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)