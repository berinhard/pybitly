import unittest
from bitly_api import API
from mock import Mock, patch_object

__all__ = [
    'TestBitlyAPIClientFunctions',
    'TestShortenAPI',
]

class TestBitlyAPIClientFunctions(unittest.TestCase):

    def setUp(self):
        self.api = API()
        self.parameters = {
            'login': 'my_login',
            'apiKey': 'R_thisismycrazyapikey',
            'longUrl': 'http://www.bernardofontes.net',
        }

    def test_get_rest_method_parameters_return_expected_string(self):
        expected = 'login=my_login&apiKey=R_thisismycrazyapikey&longUrl=http://www.bernardofontes.net'
        self.assertEquals(self.api._get_rest_method_parameters(self.parameters), expected)

    def test_get_api_method_parameters_url_works_for_shorten(self):
        expected = 'http://api.bit.ly/v3/shorten?login=my_login&apiKey=R_thisismycrazyapikey&longUrl=http://www.bernardofontes.net'
        self.assertEquals(self.api._get_api_method_url('shorten', self.parameters), expected)

def mocked_API_request_failure(status_code):
    mocked_api_response = {
        'status_code': status_code,
        'status_txt': 'something happened',
        'url': 'http://bit.ly/hash',
    }
    return Mock(return_value=(mocked_api_response))

class TestShortenAPI(unittest.TestCase):

    def setUp(self):
        self.api = API()

    @patch_object(API, '_invoke_api', mocked_API_request_failure(200))
    def test_shorten_api_response_200(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        self.assertEquals(api_response['status_code'], 200)
        self.assertTrue(api_response.has_key('url'))
        self.assertTrue(api_response['url'])

    @patch_object(API, '_invoke_api', mocked_API_request_failure(403))
    def test_shorten_api_response_403(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        self.assertEquals(api_response['status_code'], 403)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertEquals(api_response['error_message'], 'Rate limit exceeded')

    @patch_object(API, '_invoke_api', mocked_API_request_failure(503))
    def test_shorten_api_response_503(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        self.assertEquals(api_response['status_code'], 503)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertEquals(api_response['error_message'], 'Unknow error or temporary unavailability')

    @patch_object(API, '_invoke_api', mocked_API_request_failure(500))
    def test_shorten_api_response_500(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        self.assertEquals(api_response['status_code'], 500)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Invalid request format' in api_response['error_message'])

if __name__ == '__main__':
    unittest.main()
