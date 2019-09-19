import re

from framework.parser.utils import normalize_whitespace


class Paragraph(object):
    """Object representing one block of text in HTML."""

    def __init__(self, root_tag):
        self.root_tag = root_tag
        self.text_nodes = []
        self.highlighted = []
        self.paragraph_location = -1

    @property
    def is_heading(self):
        return self.root_tag == "header"

    @property
    def is_list_set(self):
        return self.root_tag == "ul"

    @property
    def is_paragraph(self):
        return self.root_tag == "p"

    @property
    def is_first_paragraph(self):
        return self.paragraph_location == 0

    @property
    def text(self):
        text = "".join(self.text_nodes)
        return normalize_whitespace(text.strip())

    def __len__(self):
        return len(self.text)

    def contains_text(self):
        return bool(self.text_nodes)

    def append_text(self, text):
        text = normalize_whitespace(text)
        if len(text) > 0:
            self.text_nodes.append(text)
        return text

    def append_highlighted(self, text):
        self.highlighted.append(text)

    # getters
    def get_root_tag(self):
        return self.root_tag

    def get_highlighted(self):
        return self.highlighted

    def get_list_array(self):
        return self.text_nodes

    def get_quotes(self):
        return re.findall(r'"([^"]*)"', self.text)

    def contains_quotes(self):
        return bool(re.findall(r'"([^"]*)"', self.text))

