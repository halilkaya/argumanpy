#!/usr/bin/env python
# coding: utf-8

"""
Response model
"""
class Response(object):

    def __init__(self, obj=None):
        self._count = obj['count'] if obj is not None else None
        self._next = obj['next'] if obj is not None else None
        self._previous = obj['previous'] if obj is not None else None
        self._results = obj['results'] if obj is not None else None
        self.keys = ['count', 'next', 'previous', 'results']


    # count
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @count.deleter
    def count(self):
        del self._count


    # next
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @next.deleter
    def next(self):
        del self._next


    # previous
    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value

    @previous.deleter
    def previous(self):
        del self._previous


    # results
    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        self._results = value

    @results.deleter
    def results(self):
        del self._results



"""
Argument model
"""
class Argument(object):

    def __init__(self, obj=None):
        self._id = obj['id'] if obj is not None else None
        self._user = obj['user'] if obj is not None else None
        self._title = obj['title'] if obj is not None else None
        self._slug = obj['slug'] if obj is not None else None
        self._description = obj['description'] if obj is not None else None
        self._owner = obj['owner'] if obj is not None else None
        self._sources = obj['sources'] if obj is not None else None
        self._premises = obj['premises'] if obj is not None else None
        self._date_creation = obj['date_creation'] if obj is not None else None
        self._absolute_url = obj['absolute_url'] if obj is not None else None
        self._report_count = obj['report_count'] if obj is not None else None
        self._is_featured = obj['is_featured'] if obj is not None else None
        self._is_published = obj['is_published'] if obj is not None else None
        self.keys = ['id', 'user', 'title', 'slug', 'description', 'owner',
                     'sources', 'premises', 'date_creation', 'absolute_url',
                     'report_count', 'is_featured', 'is_published']


    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id


    # user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @user.deleter
    def user(self):
        del self._user


    # title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @title.deleter
    def title(self):
        del self._title


    # slug
    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, value):
        self._slug = value

    @slug.deleter
    def slug(self):
        del self._slug


    # description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @description.deleter
    def description(self):
        del self._description


    # owner
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @owner.deleter
    def owner(self):
        del self._owner


    # sources
    @property
    def sources(self):
        return self._sources

    @sources.setter
    def sources(self, value):
        self._sources = value

    @sources.deleter
    def sources(self):
        del self._sources


    # premises
    @property
    def premises(self):
        return self._premises

    @premises.setter
    def premises(self, value):
        self._premises = value

    @premises.deleter
    def premises(self):
        del self._premises


    # date_creation
    @property
    def date_creation(self):
        return self._date_creation

    @date_creation.setter
    def date_creation(self, value):
        self._date_creation = value

    @date_creation.deleter
    def date_creation(self):
        del self._date_creation


    # absolute_url
    @property
    def absolute_url(self):
        return self._absolute_url

    @absolute_url.setter
    def absolute_url(self, value):
        self._absolute_url = value

    @absolute_url.deleter
    def absolute_url(self):
        del self._absolute_url


    # report_count
    @property
    def report_count(self):
        return self._report_count

    @report_count.setter
    def report_count(self, value):
        self._report_count = value

    @report_count.deleter
    def report_count(self):
        del self._report_count


    # is_featured
    @property
    def is_featured(self):
        return self._is_featured

    @is_featured.setter
    def is_featured(self, value):
        self._is_featured = value

    @is_featured.deleter
    def is_featured(self):
        del self._is_featured


    # is_published
    @property
    def is_published(self):
        return self._is_published

    @is_published.setter
    def is_published(self, value):
        self._is_published = value

    @is_published.deleter
    def is_published(self):
        del self._is_published



"""
Premise model
"""
class Premise(object):

    def __init__(self, obj=None):
        self._id = obj['id'] if obj is not None else None
        self._user = obj['user'] if obj is not None else None
        self._text = obj['text'] if obj is not None else None
        self._sources = obj['sources'] if obj is not None else None
        self._parent = obj['parent'] if obj is not None else None
        self._absolute_url = obj['absolute_url'] if obj is not None else None
        self._premise_type = obj['premise_type'] if obj is not None else None
        self._date_creation = obj['date_creation'] if obj is not None else None
        self._supporters = obj['supporters'] if obj is not None else None
        self.keys = ['id', 'user', 'text', 'sources', 'parent', 'absolute_url',
                     'premise_type', 'date_creation', 'supporters']


    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id


    # user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @user.deleter
    def user(self):
        del self._user


    # text
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @text.deleter
    def text(self):
        del self._text


    # sources
    @property
    def sources(self):
        return self._sources

    @sources.setter
    def sources(self, value):
        self._sources = value

    @sources.deleter
    def sources(self):
        del self._sources


    # parent
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @parent.deleter
    def parent(self):
        del self._parent


    # absolute_url
    @property
    def absolute_url(self):
        return self._absolute_url

    @absolute_url.setter
    def absolute_url(self, value):
        self._absolute_url = value

    @absolute_url.deleter
    def absolute_url(self):
        del self._absolute_url


    # premise_type
    @property
    def premise_type(self):
        return self._premise_type

    @premise_type.setter
    def premise_type(self, value):
        self._premise_type = value

    @premise_type.deleter
    def premise_type(self):
        del self._premise_type


    # date_creation
    @property
    def date_creation(self):
        return self._date_creation

    @date_creation.setter
    def date_creation(self, value):
        self._date_creation = value

    @date_creation.deleter
    def date_creation(self):
        del self._date_creation


    # supporters
    @property
    def supporters(self):
        return self._supporters

    @supporters.setter
    def supporters(self, value):
        self._supporters = value

    @supporters.deleter
    def supporters(self):
        del self._supporters



"""
User model
"""
class User(object):

    def __init__(self, obj=None):
        self._id = obj['id'] if obj is not None else None
        self._username = obj['username'] if obj is not None else None
        self._absolute_url = obj['absolute_url'] if obj is not None else None
        self._avatar = obj['avatar'] if obj is not None else None
        self.keys = ['id', 'username', 'absolute_url', 'avatar']


    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id


    # username
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @username.deleter
    def username(self):
        del self._username


    # absolute_url
    @property
    def absolute_url(self):
        return self._absolute_url

    @absolute_url.setter
    def absolute_url(self, value):
        self._absolute_url = value

    @absolute_url.deleter
    def absolute_url(self):
        del self._absolute_url


    # avatar
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value

    @avatar.deleter
    def avatar(self):
        del self._avatar
