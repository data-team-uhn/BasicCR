#!/usr/bin/python

import os
import basic_text_matcher
from werkzeug.utils import secure_filename

def loadfromrequest(request, trained_models_path):
    for arg in ['id_file', 'title_file']:
        if arg not in request.json:
            raise Exception("Missing parameters")
        if type(request.json[arg]) != str:
            raise Exception("Improper parameter data type")

    id_file = os.path.join(trained_models_path, secure_filename(request.json['id_file']))
    title_file = os.path.join(trained_models_path, secure_filename(request.json['title_file']))
    this_model = {}
    this_model['object'] = basic_text_matcher.BasicTextMatcher(id_file, title_file)
    this_model['threshold'] = 1.0
    return this_model
