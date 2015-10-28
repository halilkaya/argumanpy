#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from models import Response, Argument, User, Premise
import json
import requests


class Arguman(object):

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))

    def fetch_arguments(self):
        result = requests.get(self.api['arguments_url']).json()
        response = Response()
        [ setattr(response, key, result[key]) for key in response.keys ]
        return response

    def get_arguments(self):
        result = []
        for argument in self.fetch_arguments().results:
            arg = Argument(argument)
            arg.user = User(arg.user)
            result.append(arg)
        return result
