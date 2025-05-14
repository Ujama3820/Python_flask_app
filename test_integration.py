import unittest
import requests

class TestCalculatorAPI(unittest.TestCase):

    BASE_URL = "http://127.0.0.1:5000"  # Flask app URL
    
    def test_add_api(self):
        response = requests.post(f"{self.BASE_URL}/api/add", json={"a": 2, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 5)

    def test_subtract_api(self):
        response = requests.post(f"{self.BASE_URL}/api/subtract", json={"a": 5, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 2)

    def test_multiply_api(self):
        response = requests.post(f"{self.BASE_URL}/api/multiply", json={"a": 2, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 6)

    def test_divide_api(self):
        response = requests.post(f"{self.BASE_URL}/api/divide", json={"a": 6, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 2)

    def test_divide_by_zero_api(self):
        response = requests.post(f"{self.BASE_URL}/api/divide", json={"a": 6, "b": 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Cannot divide by zero')

if __name__ == '__main__':
    unittest.main()
