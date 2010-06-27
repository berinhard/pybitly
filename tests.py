import unittest
from bitly_api import API
from mock import Mock, patch

__all__ = [
    'TestBitlyAPIClientFunctions',
    'TestShortenAPI',
    'TestExpandAPI',
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

    def test_get_rest_method_parameters_with_list_return_expected_string(self):
        self.parameters['listParam'] = ['value_1', 'value_2']
        expected = 'listParam=value_1&listParam=value_2&login=my_login&apiKey=R_thisismycrazyapikey&longUrl=http://www.bernardofontes.net'
        self.assertEquals(self.api._get_rest_method_parameters(self.parameters), expected)

    def test_get_api_method_parameters_url_works_for_shorten(self):
        expected = 'http://api.bit.ly/v3/shorten?login=my_login&apiKey=R_thisismycrazyapikey&longUrl=http://www.bernardofontes.net'
        self.assertEquals(self.api._get_api_method_url('shorten', self.parameters), expected)

def mocked_API_request_failure(status_code):
    mocked_api_response = {
        'status_code': status_code,
        'data':{
            'status_txt': 'something happened',
            'url': 'http://bit.ly/hash',
        }
    }
    return Mock(return_value=(mocked_api_response))

class TestShortenAPI(unittest.TestCase):

    def setUp(self):
        self.api = API()

    @patch.object(API, '_invoke_api', mocked_API_request_failure(200))
    def test_shorten_api_response_200(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        status_code = api_response['status_code']
        self.assertEquals(status_code, 200)
        self.assertTrue(api_response.has_key('url'))
        self.assertTrue(api_response['url'])

    @patch.object(API, '_invoke_api', mocked_API_request_failure(403))
    def test_shorten_api_response_403(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        status_code = api_response['status_code']
        self.assertEquals(status_code, 403)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Rate limit exceeded' in api_response['error_message'])

    @patch.object(API, '_invoke_api', mocked_API_request_failure(503))
    def test_shorten_api_response_503(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        status_code = api_response['status_code']
        self.assertEquals(status_code, 503)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Unknow error or temporary unavailability' in api_response['error_message'])

    @patch.object(API, '_invoke_api', mocked_API_request_failure(500))
    def test_shorten_api_response_500(self):
        api_response = self.api.shorten('http://www.bernardofontes.net')
        status_code = api_response['status_code']
        self.assertEquals(status_code, 500)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Invalid request format' in api_response['error_message'])

def mocked_expand_API_request_failure(status_code):
    mocked_api_response = {
        'status_code': status_code,
        'data':{
            'expand':[
                {
                    'long_url': 'http://www.bernardofontes.net',
                    'short_url': 'http://bit.ly/hash',
                },
                {
                    'long_url': 'http://www.bernardofontes.net/blog',
                    'short_url': 'http://bit.ly/hash2',
                },
            ]
        }
    }
    return Mock(return_value=(mocked_api_response))

class TestExpandAPI(unittest.TestCase):

    def setUp(self):
        self.api = API()

    @patch.object(API, '_invoke_api', mocked_expand_API_request_failure(200))
    def test_expand_api_response_200(self):
        api_response = self.api.expand(['http://bit.ly/hash', 'http://bit.ly/hash2'])
        status_code = api_response['status_code']
        self.assertEquals(status_code, 200)
        self.assertTrue(api_response.has_key('expand'))
        self.assertTrue(len(api_response['expand']) == 2)

    @patch.object(API, '_invoke_api', mocked_expand_API_request_failure(403))
    def test_expand_api_response_403(self):
        api_response = self.api.expand(['http://bit.ly/hash', 'http://bit.ly/hash2'])
        status_code = api_response['status_code']
        self.assertEquals(status_code, 403)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Rate limit exceeded' in api_response['error_message'])

    @patch.object(API, '_invoke_api', mocked_expand_API_request_failure(503))
    def test_expand_api_response_503(self):
        api_response = self.api.expand(['http://bit.ly/hash', 'http://bit.ly/hash2'])
        status_code = api_response['status_code']
        self.assertEquals(status_code, 503)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Unknow error or temporary unavailability' in api_response['error_message'])

    @patch.object(API, '_invoke_api', mocked_expand_API_request_failure(500))
    def test_expand_api_response_500(self):
        api_response = self.api.expand(['http://bit.ly/hash', 'http://bit.ly/hash2'])
        status_code = api_response['status_code']
        self.assertEquals(status_code, 500)
        self.assertTrue(api_response.has_key('error_message'))
        self.assertTrue('Invalid request format' in api_response['error_message'])

if __name__ == '__main__':
    unittest.main()
