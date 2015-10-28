#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from models import Response, Argument, User, Premise
import json
import requests


class Authentication(object):

    """
    Authentication class logs you in, registers or updates your profile.
    login method uses only username and password and register method uses
    all information on credentials.txt
    """

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))
        self.credentials = json.load(open('credentials.json', 'r'))

    def login(self):
        """
        Logs you in.
        After logging in, creates a file token.txt if not exists and puts
        your access token to use it later.
        It uses username and password which are placed in credentials.json file.
        """
        data = {}
        data['username'] = self.credentials['username']
        data['password'] = self.credentials['password']
        result = requests.post(url=self.api['login_url'], data=data)
        if result.ok:
            token = result.json()['token']
            token_file = open('token.txt', 'w')
            token_file.write(token)
            return 'You\'re successfully logged in! Your token: %s' % token
        return result.text

    def register(self):
        """
        Registers you to arguman.org
        If registration is successfull, it logs you in.
        """
        headers = {'Content-Type': 'application/json'}
        result = requests.post(url=self.api['registration_url'], data=self.credentials)
        if result.ok:
            print('You\'re successfully registered!')
            self.login()
        return result.text

    def update_profile(self, data):
        """
        Updates your profile by using information in credentials.json file.
        data parameters will have what you want to update on your profile.
        If you want to change your password, you must put your password in both
        new_password1 and new_password2 keys.
        """
        token = 'Bearer %s' % open('token.txt', 'r').read()
        headers = {
            'Content-Type': 'application/json',
            'Authentication': token
        }
        result = requests.put(url=self.api['user_url'], data=data, headers=headers)
        if result.ok:
            return 'Your profile has been successfully updated.'
        return result.text


class Me(object):

    """
    Me class gets personal information for you. Such as your followers.
    """

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))
        self.credentials = json.load(open('credentials.json', 'r'))
        self.url = None
        self.followers = []

    def fetch_followers(self):
        """
        Fetches your followers. Please call get_all_followers() to get your all
        followers.
        """
        url = self.api['followers_url'].format(username=self.credentials['username']) if not self.url else self.url
        result = requests.get(url).json()
        response = Response()
        [ setattr(response, key, result[key]) for key in response.keys ]
        return response

    def get_all_followers(self):
        """
        Gets all your followers. It stores your followers in followers variable.
        After you call this method, you can use followers variable.
        """
        followers = self.fetch_followers()
        [ self.followers.append(User(follower)) for follower in followers.results ]
        if followers.next:
            self.url = followers.next
            self.get_all_followers()


class Arguman(object):

    """
    Main class of ArgumanPy. You can fetch all arguments.
    """

    def __init__(self):
        self.api = json.load(open('api.json', 'r'))
        self.url = None
        self.arguments = []

    def fetch_arguments(self):
        """
        Fetches arguments. Please call get_all_arguments() to get all arguments.
        """
        url = self.api['arguments_url'] if not self.url else self.url
        result = requests.get(url).json()
        response = Response()
        [ setattr(response, key, result[key]) for key in response.keys ]
        return response

    def get_all_arguments(self):
        """
        Gets all arguments and premises belong to it. It stores result in
        arguments variable. After you call this method, you can use arguments
        variable.
        """
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
