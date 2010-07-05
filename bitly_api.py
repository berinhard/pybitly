from httplib2 import Http
import json
import sys

class API(object):

    api_host = 'http://api.bit.ly'
    api_path = {
        'shorten': '/v3/shorten',
        'expand': '/v3/expand',
        'clicks': '/v3/clicks',
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
        response = self._invoke_api(api_url)
        return self._prepare_response(response)

    def expand(self, short_urls):
        parameters = {
            'login': self.login,
            'apiKey': self.api_key,
            'shortUrl': short_urls,
        }
        api_url = self._get_api_method_url('expand', parameters)
        response = self._invoke_api(api_url)
        return self._prepare_response(response)

    def clicks(self, short_urls):
        parameters = {
            'shortUrl': short_urls
        }
        api_url = self._get_api_method_url('clicks', parameters)
        response = self._invoke_api(api_url)
        return self._prepare_response(response)

    def _prepare_response(self, response):
        status_code = response['status_code']
        if status_code!= 200:
            response['error_message'] = self._get_errror_message(status_code, response)
        else:
            response.update(response.pop('data'))
        return response

    def _get_rest_method_parameters(self, parameters):
        parameters_url = ''
        for parameter, value in parameters.items():
            if isinstance(value, list):
                parameters_url += ''.join(['%s=%s&' % (parameter, v) for v in value])
            else:
                parameters_url += '%s=%s&' % (parameter, value)
        return parameters_url[:-1]

    def _get_api_method_url(self, method, parameters):
        base_path = self.api_host + self.api_path[method]
        parameters_url = self._get_rest_method_parameters(parameters)
        return base_path + '?' + parameters_url

    def _invoke_api(self, url):
        http = Http()
        try:
            response = http.request(url, "GET")
            response = json.loads(response[1])
            return response
        except Exception as e:
            return {'status_code':503}

    def _get_errror_message(self, status_code, response):
        error_message = ''
        if status_code == 403:
            error_message = 'ERROR 403: Rate limit exceeded'
        elif status_code == 503:
            error_message = 'ERROR 503: Unknow error or temporary unavailability'
        elif status_code == 500:
            error_message = 'ERROR 500: Invalid request format'
            if response.has_key('status_txt'):
                error_message += ': %s' % response['status_txt']
        return error_message
