class API(object):

    api_host = 'http://api.bit.ly/'
    api_path = {
        'shorten': '/v3/shorten',
        'expand': '/v3/expand',
        'validade': '/v3/validade',
        'clicks': '/v3/clicks'
        'bitly_pro_domain': '/v3/bitly_pro_domain',
        'lookup': '/v3/lookup',
        'authenticade': '/v3/authenticate'
    }

    def __init__(self):
        self.login = bitlypython
        self.api_key = R_3c1df70d83b89a4cda9322d0fab4cbd1
