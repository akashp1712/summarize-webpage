# summarize_webpage
###### A Flask application that summarize webpage using Natural Language Processing powered by [nlp-akash](https://github.com/akashp1712/nlp-akash).

## Index

* [Motivation](#motivation)
* [Requirements](#requirements)
* [Installation](#installation)
* [Language And Tools](#language-and-tools)
* [Implementation](#implementation)
* [Contribution](#contribution)

### Motivation

Motivation of this project to make production ready API for Text Summarization.
This project implements basic algorithm for extractive text summarization using Python.

### How to start

You need to manually clone or download this repository. Project is ready to run (with some requirements).

You need to run ```app.py``` file in your development environment.

>Open http://127.0.0.1:5000/, customize project files and **have fun**.


## Requirements

The suggested way is to use ```python virtual environment```. The project is developed using ```python 3.7.1```

### Included modules support

##### Python
This project uses very simple <b>python web framework called [Flask](http://flask.pocoo.org/)</b>, which is very eay to learn ad adopt.

The <b>[NLTK](https://www.nltk.org) - Natural Language ToolKit</b> is used for the Text Summarization Algorithm implementation.

##### HTML

The HTML Template used in this project is <b>[Stanley](https://templatemag.com/stanley-bootstrap-freelancer-template/) - Bootstrap Freelancer Template</b>.

##### JavaScript

- Vanilla Javascript

##### CSS

- Vanilla CSS

### Installation
Run requirements.txt to install the required python packages.

```
$ pip install -r requirements.txt
```

## Project Structure 
```
|───config/
|───framework/
|───implementaion/
|───static/
|───templates/
|───app.py
|───wsgi.py
```

#### Implementation

----
    ├──framework
    | |──justext
    | |──parser


 > jusText (the original framework) is developed by [`miso-belica`](https://github.com/miso-belica)

- ``justext`` is modified code from [`jusText`](https://github.com/miso-belica/jusText) which is a Heuristic based boilerplate removal tool.
 The original code is modified to parse some of the tags ``(i.e, <P>, <li>, <b>, <H1>...<H6>), etc``
 
    - Please note that, this project only uses English stopwords from the original project.
 
 
- We're using jusText framework to download the webcontent and parse it using ``parser``.

  - ``parser`` creates list of ``Paragraph`` object which has following properties:
  
    
    1. is_heading -> boolean
       :: returns true if paragraph is heading (<H1>...<H6>) 
    
   
    2. is_list_set -> boolean 
       :: returns true if paragraph is list tag (<li>)


    3. is_paragraph -> boolean
       :: returns true if paragraph is paragraph tag (<p>)

    4. is_first_paragraph(self):
       :: returns true if the paragraph is the first paragraph from the content.

    5. text(self):
       :: get the text content of the paragraph without any tags

 ---
 
    ├──implementaion
    | |──word_frequency_summarize_parser.py
    
  This is the core module of this project: The implementation of the Summarization Algorithm.
  
[**Word_Frequency_Summarization:**](https://github.com/akashp1712/nlp-akash/blob/master/text-summarization/Word_Frequency_Summarization.py) Summarization implementation using word frequency. <br/>
* ##### Please refer the Article: [Text summarization in 5 steps using NLTK](https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65) 
  
> <b>Important:</b> This project has implemented slightly modified version of the Algorithm, where scoring the sentences method considers the web Text properties such as Header or list text.

> i.e, it gives more weighing to Header or Bold text than normal text. 

 ---
 
    ├──app.py
    
The app.py 
    



### Contribution

Feel free to raise an issue for bug or feature request And pull request for any kind of improvements.
