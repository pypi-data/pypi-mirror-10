# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import copy
try:
    import simplejson as json
except ImportError:
    import json

import six
import requests

from teambition import api
from teambition.api.base import APIDescriptor, TeambitionAPI
from teambition.utils import JSONEncoder, JSONDecoder


class APIClientMeta(type):

    def __new__(cls, class_name, bases, attrs):
        for b in bases:
            if not hasattr(b, '_api_endpoints'):
                continue

            for k, v in b.__dict__.items():
                if k in attrs:
                    continue
                if isinstance(v, APIDescriptor):
                    attrs[k] = copy.deepcopy(v)

        cls = super(APIClientMeta, cls).__new__(cls, class_name, bases, attrs)
        cls._api_endpoints = {}

        for name, api in cls.__dict__.items():
            if isinstance(api, TeambitionAPI):
                api.add_to_class(cls, name)

        return cls


class Teambition(six.with_metaclass(APIClientMeta)):
    """
    Teambition API 客户端
    """

    API_BASE_URL = 'https://api.teambition.com/'

    # API endpoints
    oauth = api.OAuth()
    """:doc:`oauth`"""
    projects = api.Projects()
    """:doc:`projects`"""
    tasklists = api.Tasklists()
    """:doc:`tasklists`"""
    stages = api.Stages()
    """:doc:`stages`"""
    tasks = api.Tasks()
    """:doc:`tasks`"""
    users = api.Users()
    """:doc:`users`"""
    organizations = api.Organizations()
    """:doc:`organizations`"""
    stagetemplates = api.StageTemplates()
    """:doc:`stagetemplates`"""
    teams = api.Teams()
    """:doc:`teams`"""
    subtasks = api.Subtasks()
    """:doc:`subtasks`"""
    messages = api.Messages()
    """:doc:`messages`"""
    posts = api.Posts()
    """:doc:`posts`"""
    collections = api.Collections()
    """:doc:`collections`"""
    works = api.Works()
    """:doc:`works`"""
    events = api.Events()
    """:doc:`events`"""
    tags = api.Tags()
    """:doc:`tags`"""
    objectlinks = api.ObjectLinks()
    """:doc:`objectlinks`"""
    activities = api.Activities()
    """:doc:`activities`"""
    webhooks = api.Webhooks()
    """:doc:`webhooks`"""

    def __init__(self, client_id, client_secret, access_token=None):
        """
        初始化 Teambition API Client

        :param client_id: 申请应用时分配的 client_id
        :param client_secret: 申请应用时分配的 client_secret
        :param access_token: 可选，access_token
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = access_token

    def _request(self, method, endpoint, **kwargs):
        if not endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=endpoint
            )
        else:
            url = endpoint

        if 'params' not in kwargs:
            kwargs['params'] = {}
        if 'access_token' not in kwargs['params'] and self.access_token:
            kwargs['params']['access_token'] = self.access_token
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(
                kwargs['data'],
                ensure_ascii=False,
                cls=JSONEncoder
            )
            body = body.encode('utf-8')
            kwargs['data'] = body

        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
        if 'Authorization' not in kwargs['headers']:
            kwargs['headers']['Authorization'] = 'OAuth2 {0}'.format(
                self.access_token
            )

        res = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        res.raise_for_status()
        result = res.json(cls=JSONDecoder)
        return result

    def get(self, endpoint, **kwargs):
        return self._request('get', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request('post', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request('put', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request('delete', endpoint, **kwargs)

    @property
    def access_token(self):
        """
        获取 access_token

        :return: access_token
        """
        return self._access_token

    @access_token.setter
    def access_token(self, token):
        """
        设置 access_token

        :param token: access_token
        """
        self._access_token = token
