import urllib.request
from urllib.error import URLError, HTTPError
import parser2

url = 'https://lenta.ru/news/2016/08/04/peskov_medved'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(url, None, headers)
try:
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    parser = parser2.Parser()
    parser.feed(content)

except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
