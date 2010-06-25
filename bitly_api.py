from httplib2 import Http
import json
import sys

class API(object):

    api_host = 'http://api.bit.ly'
    api_path = {
        'shorten': '/v3/shorten',
        'expand': '/v3/expand',
        'validade': '/v3/validade',
        'clicks': '/v3/clicks',
        'bitly_pro_domain': '/v3/bitly_pro_domain',
        'lookup': '/v3/lookup',
        'authenticade': '/v3/authenticate'
    }

    def __init__(self):
        self.login = 'bitlypython'
        self.api_key = 'R_3c1df70d83b89a4cda9322d0fab4cbd1'

    def shorten(self, long_url):
        parameters = {
            'login': self.login,
            'apiKey': self.api_key,
            'longUrl': long_url,
        }
        api_url = self._get_api_method_url('shorten', parameters)
        response = json.loads(self._invoke_api(api_url))
        if response['status_code'] == 403:
            print 'Rate limit exceeded'
        elif response['status_code'] == 503:
            print 'Unknow error or temporary unavailability'
        elif response['status_code'] == 500:
            print 'Invalid request format: %s' % response['status_txt']
        elif response['status_code'] == 200:
            print 'Shorten URL: %s' % response[data][url]

    def _get_rest_method_parameters(self, parameters):
        parameters_url = ''
        for parameter, value in parameters.items():
            parameters_url += '%s=%s&' % (parameter, value)
        return parameters_url[:-1]

    def _get_api_method_url(self, method, parameters):
        base_path = self.api_host + self.api_path[method]
        parameters_url = self._get_rest_method_parameters(parameters)
        return base_path + '/' + parameters_url

    def _invoke_api(self, url):
        http = Http()
        try:
            response = http.request(url, "GET")
            response = response[1]
            return response
        except Exception as e:
            print 'A connection error happenned'
            sys.exit(0)
