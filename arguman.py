#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from models import Response, Argument, User, Premise
import json
import requests


class Authentication(object):

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))
        self.credentials = json.load(open('credentials.json', 'r'))

    def login(self):
        result = requests.post(url=self.api['login_url'], data=self.credentials)
        if result.ok:
            token = result.json()['token']
            token_file = open('token.txt', 'w')
            token_file.write(token)
            return 'You\'re successfully logged in! Your token: %s' % token
        return result.text


class Me(object):

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))
        self.url = None
        self.followers = []

    def fetch_followers(self, username):
        url = self.api['followers_url'].format(username=username) if not self.url else self.url
        result = requests.get(url).json()
        response = Response()
        [ setattr(response, key, result[key]) for key in response.keys ]
        return response

    def get_all_followers(self, username):
        followers = self.fetch_followers(username)
        [ self.followers.append(User(follower)) for follower in followers.results ]
        if followers.next:
            self.url = followers.next
            self.get_all_followers(username)


class Arguman(object):

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))
        self.url = None
        self.arguments = []

    def fetch_arguments(self):
        url = self.api['arguments_url'] if not self.url else self.url
        result = requests.get(url).json()
        response = Response()
        [ setattr(response, key, result[key]) for key in response.keys ]
        return response

    def get_all_arguments(self):
        arguments = self.fetch_arguments()
        for argument in arguments.results:
            a = Argument(argument)
            a.user = User(a.user)
            premises = []
            for premise in a.premises:
                prms = Premise(premise)
                prms.user = User(prms.user)
                premises.append(prms)
            a.premises = premises
            self.arguments.append(a)
        if arguments.next:
            self.url = arguments.next
            self.get_all_arguments()
