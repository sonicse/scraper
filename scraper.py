import sys
import urllib.request
from urllib.error import URLError, HTTPError
import parser2
import classifier
import formatter
import io

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'https://lenta.ru/news/2016/08/04/peskov_medved/'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(url, None, headers)
try:
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
    parser = parser2.Parser2()
    parser.feed(data)
    classifier.classifier(parser.contents)
    text = ''
    for content in parser.contents:
        if content.is_content and content.text:
            text += content.text + '{'+ str(content.is_content) +'}' + '\n'
    text = formatter.format(text)
    with io.open('result.txt', 'w', encoding='utf8') as f:
        f.write(text)
    f.close()

except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
