from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class TestCalculatorE2E(unittest.TestCase):
    def setUp(self):
        # Automatically download and set up chromedriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://127.0.0.1:5000")  # Flask app URL

    def test_addition(self):
        driver = self.driver
        driver.find_element("name", "num1").send_keys("5")
        driver.find_element("name", "num2").send_keys("3")
        driver.find_element("name", "operation").send_keys("add")
        driver.find_element("xpath", "//button[text()='Calculate']").click()
        time.sleep(2)
        result = driver.find_element("tag name", "body").text
        self.assertIn("Result: 8", result)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
