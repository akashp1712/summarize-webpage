import traceback
from time import strftime

from flask import Flask, request, jsonify, make_response, render_template

from config.cfg_handler import CfgHandler
from config.cfg_utils import fetch_base_url
from framework.justext.core import justextHTML
from framework.parser.parser import Parser
from implementation import word_frequency_summarize_parser

# Initialize the Flask application
app = Flask(__name__)


# REST Service methods


# handle undefined routes
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        app.logger.info('%s %s %s %s %s %s',
                        ts,
                        request.remote_addr,
                        request.method,
                        request.scheme,
                        request.full_path,
                        response.status)
    return response


@app.errorhandler(Exception)
def exceptions(exception):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    app.logger.error('%s %s %s %s %s ERROR:%s \n%s',
                     ts,
                     request.remote_addr,
                     request.method,
                     request.scheme,
                     request.full_path,
                     str(exception),
                     tb)

    return make_response(jsonify({'error': str(exception)}))


@app.route('/')
def index():
    base_url = fetch_base_url(CfgHandler())
    return render_template('index.html', base_url=base_url)


# `summarize` method takes webpage url as argument and returns the summarized text as json object
@app.route('/v1/summarize', methods=['GET'])
def summarize():
    app.logger.debug('summarize(): requested')
    if 'url' not in request.args:
        return make_response(jsonify({'error': str('Bad Request: argument `url` is not available')}), 400)

    url = request.args['url']

    if not url:  # if url is empty
        return make_response(jsonify({'error': str('Bad Request: `url` is empty')}), 400)

    summary = ""

    try:
        # Fetch web content
        web_text = justextHTML(html_text=None, web_url=url)

        # Parse it via parser
        parser = Parser()
        parser.feed(web_text)

        # summary = facebook_parser_word_frequency_summarize.run_summarization(parser.paragraphs)
        summary = word_frequency_summarize_parser.run_summarization(parser.paragraphs)

    except Exception as ex:
        app.logger.error('summarize(): error while summarizing: ' + str(ex) + '\n' + traceback.format_exc())
        pass

    return make_response(jsonify({'summary': summary}))


if __name__ == '__main__':

    app.run(
        host="localhost"
    )
