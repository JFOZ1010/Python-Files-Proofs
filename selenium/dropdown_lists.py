import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element(by="id", value='select-language'))

        self.assertEqual(3, len(select_language.options)) #verifica que el numero de opciones sea 3

        for option in select_language.options:
            act_options.append(option.text) #agrega las opciones a la lista act_options, el texto de cada opcion

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German') #selecciona la opcion German, para que esté la page al idioma aleman

        self.assertTrue('store=german' in self.driver.current_url) #verifica que la url actual contenga la palabra german

        select_language = Select(self.driver.find_element(by="id", value='select-language'))  #volver a seleccionar el elemento

        select_language.select_by_index(0) #es el idioma ingles el indce 0
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
