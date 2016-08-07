from html.parser import HTMLParser
import content


skip_tags = {'script', 'head', 'link', 'meta', 'style', 'aside', 'nav'}
inline_tags = {'span', 'i', 'a'}


class Parser2(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.skip = False
        self.body = False
        self.inline = False
        self.href = None
        self.content = content.Content()
        self.contents = [self.content]

    def handle_starttag(self, tag, attrs):
        self.skip |= tag in skip_tags
        self.inline &= tag in inline_tags
        if tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    self.href = value
        else:
            self.href = None

        if tag == 'body':
            self.body = True

    def handle_data(self, data):
        if self.skip or not self.body:
            return

        if not self.inline:
            if self.content.text:
                self.content = content.Content()
                self.contents.append(self.content)
                self.inline = True

        self.content.set_data(' '.join(data.split()), self.href)

        if self.href:
            self.content.set_href(self.href)


    def handle_endtag(self, tag):
        #XXX:не решена проблема вложенности пропускаемых тэгов
        self.skip &= tag not in skip_tags
        self.inline &= (tag in inline_tags)
        self.href = None
        if tag == 'body':
            self.body = False