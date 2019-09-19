from html.parser import HTMLParser

from framework.parser.paragraph import Paragraph
from framework.parser.utils import normalize_whitespace

HIGHLIGHTED_TAGS = ['b']
PARAGRAPH_TAGS = ['header', 'p', 'ul']
LIST_TAGS = ['li']


class Parser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.paragraphs = []
        self.paragraph = None
        self.temp_content = ''

        self.is_highlighted = False
        self.is_list = False

    # Override
    def error(self, message):
        pass

    # Methods to create paragraphs: STARTS
    def _start_new_paragraph(self, root_tag):
        """
        Create new Paragraph object which contains empty string
        :param root_tag: root tag of the paragraph (<header>, <ul> or <p>)
        """
        self.paragraph = Paragraph(root_tag)

    def _append_to_paragraph(self, content):
        """
        Append content to the paragraph.
        :param content: paragraph content
        """
        if self.paragraph is not None:
            self.paragraph.append_text(content)

    def _end_the_paragraph(self):
        """
        Add the paragraph in the list of Paragraph
        """
        if self.paragraph and self.paragraph.contains_text():
            self.paragraph.paragraph_location = len(self.paragraphs)
            self.paragraphs.append(self.paragraph)

    # Methods to create paragraphs: ENDS

    # Utility methods to add extra information to paragraphs: STARTS
    def _append_highlighted(self, content):
        """
        Append highlighted words to the highlighted array in Paragraph

        :param content: highlighted word or phrase
        """
        if self.paragraph is not None:
            self.paragraph.append_highlighted(content)

    # Utility methods to add extra information to paragraphs: ENDS

    # Override
    def handle_starttag(self, tag, attrs):

        if tag in PARAGRAPH_TAGS:
            self._start_new_paragraph(tag)

        elif tag in HIGHLIGHTED_TAGS:
            self.is_highlighted = True

        elif tag in LIST_TAGS:
            self.is_list = True

    # Override
    def handle_endtag(self, tag):

        if self.paragraph is not None and not self.is_list:
            self._append_to_paragraph(self.temp_content)
            self.temp_content = ''

        if tag in PARAGRAPH_TAGS:
            self._end_the_paragraph()

        elif tag in HIGHLIGHTED_TAGS:
            self.is_highlighted = False

        elif tag in LIST_TAGS:
            self.is_list = False

    # Override
    def handle_data(self, data):
        cleaned_data = normalize_whitespace(data)

        # the temporary content will be added at the time of end tag.
        self.temp_content += cleaned_data

        if self.is_highlighted:
            self._append_highlighted(cleaned_data)
