#data driven testing, es desarrollas pruebas en
#base al codigo existente para validar en que esecenarios pasan o fallan. 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from ddt import ddt, data, unpack
import csv

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    #read the first line
    reader = csv.reader(data_file)
    next(reader, None) #skip the headers

    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    #@data(('dress', 6), ('music', 5)) #
    @data(*get_data('test_data.csv'))
    @unpack #obtener la info
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element(by="name", value="q")
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_element(by="xpath", value='//h2[@class="product-name"]/a')
        #print('Se encontró la cantidad de productos', self.len(products))
        expected_count = int(expected_count)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(by="class name", value="note-msg")
            self.assertEqual("Your search returns no results.", message)

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

        print(f"Found {len(products)} products")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)