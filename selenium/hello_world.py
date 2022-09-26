import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('http://www.wikipedia.org')

    #el decorador ayuda para que se pueda ejecutar el metodo, en una sola instancia, sin tener que crear una nueva instancia, en una sola ventana.
    @classmethod 
    def tearDownClass(cls):
        cls.driver.quit() # Cerrar el navegador, porque si no se queda abierto

if __name__ == '__main__':
     #Este solo lo usaré cuando necesité guardar los reportes en un html ->
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
    unittest.main(verbosity = 2)