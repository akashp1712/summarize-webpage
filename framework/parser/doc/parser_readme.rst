===================================
Description of the parser framework
===================================

.. contents::
  :local:

Introduction
------------
Parser is a parser for custom HTML like language which generates **list of Paragraph**.

Following is the code example of the custom language:

.. code-block:: html

  <header>This is header.</header>
  <ul><li>This is a list point1.</li><li>This is a list point2.</li></ul>
  <p>This is paragraph with <b>bold</b> text inside.</p>

Each Paragraph object can be either of **header, ul or p** type, these are the root tags.

**<b>** is child tag and can occue inside any of the root tags. (makes most sense when occurs inside **li or p** tags)

Algorithm
---------------
**1. Parsing the text**

It extends HTMLParser and overrides the methods (``handle_starttag``, ``handle_endtag``, ``handle_data``) to process the tags and data.

**2. Creating the paragraphs**

For every root tag (``header``, ``ul``, ``p``), it creates new paragraph object and adds content/data, which is implemented in the overridden methods.

Usage
-----

**1. Parse the text**

.. code-block:: python

    parseer = Parser()
    parser.feed(custom_language_text)

**2. Access the list of paragraph**

.. code-block:: python

    for paragraph in parser.paragraphs:
        print(pg.text)

**3. Useful methods**


.. code-block:: python

    # Get the content of the Paragraph
    paragraph.text # returns content text without any tags

    # Know the paragraph type
    paragraph.get_root_tag() # returns `header`, `ul` or `p`

    # Alternatively any of the below property method

    paragrpah.is_heading() # returns True/False

    paragrpah.is_list_set() # returns True/False

    paragrpah.is_paragraph() # returns True/False

    # Get the list of highlighted words or phrases in Paragraph
    paragraph.get_highlighted()
    i.e, ["NLP", "Artificial Intelligence", "data science and human language"]

    # Get the array of list points inside <ul> tag
    paragraph.get_list_array()




