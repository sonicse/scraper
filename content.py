class Content:
    def __init__(self):
        self.is_content = False
        self.text = ''
        self.words = 0
        self.href_words = 0
        self.words_in_wrapped_lines = 0
        self.lines = 0
        self.line_len = 0
        self.line_words = 0
        self.calculated = False

    def text_density(self):
        if not self.calculated:
            self.calculate()
        return self.words_in_wrapped_lines / self.lines

    def link_density(self):
        if self.href_words == 0:
            return 0
        return self.href_words / self.words

    def set_data(self, data, is_href):
        if data:
            self.text += ' ' + data

        for word in data.split():
            self.words += 1
            if is_href:
                self.href_words += 1
            word_len = len(word)
            self.line_len += word_len + 1
            if self.line_len > 80:
                self.lines += 1
                self.line_len = word_len
                self.line_words = 1

    def set_href(self, href):
        self.text += ' [' + href + ']'

    def calculate(self):
        if self.lines == 0:
            self.words_in_wrapped_lines = self.words
            self.lines = 1
        else:
            self.words_in_wrapped_lines = self.words - self.line_words
        self.calculated = True
