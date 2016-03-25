from __future__ import print_function

import requests


class InvalidField(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Torn(object):

    def __init__(self, apikey, apitype):
        """Torn User API modeled as a class.

        Args:
            apikey (string): API key from TORN. Required for all API calls.

        """
        self.apikey = apikey
        self.apitype = apitype
        self.apiid = None
        self.selections = None

    def __getattr__(self, attr):
        """Request field information as an attribute.

        Returns:
            str: Returns string of pretty formatted json response.

        Exception:
            InvalidField: Can raise if attr is not valid.

        """
        if attr in self.selections:
            if attr == 'overview':
                sel = ''
            else:
                sel = attr
            payload = {'key': self.apikey, 'selections': sel}
            return requests.get('http://api.torn.com/%s/%s' % (
                self.apitype,
                self.apiid
            ), params=payload)
        else:
            raise InvalidField()


class User(Torn):

    def __init__(self, apikey):
        """Torn User API modeled as a class.

        Args:
            apikey (string): API key from TORN. Required for all API calls.

        """
        self.apikey = apikey
        self.apitype = 'user'
        self.apiid = ''
        self.selections = [
            'attacks',     'attacksfull',   'bars',      'basic',
            'battlestats', 'bazaar',        'cooldowns', 'crimes',
            'display',     'education',     'events',    'hof',
            'honors',      'icons',         'inventory', 'medals',
            'messages',    'money',         'networth',  'notifications',
            'perks',       'personalstats', 'profile',   'properties',
            'stocks',      'travel',        'workstats'
        ]


class Property(Torn):

    def __init__(self, apikey, apiid):
        """Torn User API modeled as a class.

        Args:
            apikey (string): API key from TORN. Required for all API calls.
            apiid (int): ID of property.

        """
        self.apikey = apikey
        self.apitype = 'property'
        self.apiid = str(apiid)
        self.selections = [
            'property'
        ]
