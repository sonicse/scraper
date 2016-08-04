from html.parser import HTMLParser

skip_tags = {'script', 'head', 'link', 'meta'}

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_content = False

    def handle_starttag(self, tag, attrs):
        self.is_content = tag not in skip_tags
        #if tag not in skip_tags:
            #for key, value in attrs:
            #    if key =='id' and value == 'foo':
                    #self.is_content = True

    def handle_data(self, data):
        if self.is_content:
            print(data)

    def handle_endtag(self, tag):
        self.is_content = False
