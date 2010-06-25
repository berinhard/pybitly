import unittest
from bitly_api import API

class TestBitlyAPIClient(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def test_get_rest_method_parameters_return_expected_string(self):
        parameters = {
            'login': 'my_login',
            'apiKey': 'R_thisismycrazyapikey',
            'longUrl': 'www.bernardofontes.net',
        }
        expected = 'login=my_login&apiKey=R_thisismycrazyapikey&longUrl=www.bernardofontes.net'
        self.assertEquals(self.api._get_rest_method_parameters(parameters), expected)

if __name__ == '__main__':
    unittest.main()
