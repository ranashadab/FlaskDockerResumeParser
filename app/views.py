import requests
from pyresparser import ResumeParser
import os
from flask import request
import re
import json
from app import app


@app.route('/parse', methods=['POST'])
def home():
    parse_url = request.form['url']
    try:
        headers = requests.get(parse_url).headers
        print(headers.get('Content-Type', ''))
        if('application/xml' in headers.get('Content-Type', '')):
            return {'status_code': 410,
                               'message': 'Link Expired'}
        doc_type = 'pdf' if 'pdf' in headers.get(
            'Content-Type', '') else 'docx' if 'officedocument' in headers.get('Content-Type',    '') else None
        if doc_type == None:
            return {'status_code': 406,
                               'message': 'Unknown File Type'}
        r = requests.get(parse_url, allow_redirects=True)
        open('temp.'+doc_type, 'wb').write(r.content)
        data = ResumeParser('temp.'+doc_type).get_extracted_data()
        if os.path.exists('temp.'+doc_type):
            os.remove('temp.'+doc_type)
        return {'status_code': 200,
                           'data': data}
    except:
        return {'status_code': 500,
                           'message': "Server Error!"}
