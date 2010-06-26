import sys
from bitly_api import API

def call_shorten_api():
    api = API()
    try:
        long_url = sys.argv[2]
        response = api.shorten(long_url)
        if response.has_key('error_message'):
            print response['error_message']
        else:
            print 'Shorten URL: %s' % response['data']['url']
    except IndexError:
        print 'Long URL is missing'

if len(sys.argv) < 2:
    print "Digit 'pybitly --help' to get instructions"
    sys.exit(0)

parameter = sys.argv[1]
if parameter == '--shorten':
    call_shorten_api()
else:
    print "Digit 'pybitly --help' to get instructions"
