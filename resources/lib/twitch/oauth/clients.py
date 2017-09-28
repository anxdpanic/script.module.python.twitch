# -*- encoding: utf-8 -*-

from twitch import CLIENT_ID, CLIENT_SECRET

from six.moves.urllib_parse import urlsplit, urlencode


class MobileClient:
    _base_url = 'https://api.twitch.tv/kraken/oauth2/{0}'

    def __init__(self, client_id='', client_secret=''):
        self.client_id = client_id if client_id else CLIENT_ID
        self.client_secret = client_secret if client_secret else CLIENT_SECRET

    def prepare_request_uri(self, redirect_uri='http://localhost:3000/', scope=list(), force_verify=False, state=''):
        params = {'response_type': 'token',
                  'client_id': self.client_id,
                  'redirect_uri': redirect_uri,
                  'scope': ' '.join(scope),
                  'force_verify': str(force_verify).lower(),
                  'state': state}
        params = urlencode(params)
        url = '{base_uri}?{params}'.format(base_uri=self._base_url.format('authorize'), params=params)
        return url

    def prepare_token_uri(self, scope=list()):
        params = {'client_id': self.client_id,
                  'client_secret': self.client_secret,
                  'scope': ' '.join(scope)}
        params = urlencode(params)
        url = '{base_uri}?{params}'.format(base_uri=self._base_url.format('token'), params=params)
        return url

    def prepare_revoke_uri(self, token):
        params = {'client_id': self.client_id,
                  'token': token}
        params = urlencode(params)
        url = '{base_uri}?{params}'.format(base_uri=self._base_url.format('revoke'), params=params)
        return url

    @staticmethod
    def parse_implicit_response(url):
        pairs = urlsplit(url).fragment.split('&')
        fragment = dict()
        for pair in pairs:
            key, value = pair.split('=')
            fragment[key] = value
        return {'access_token': fragment.get('access_token'), 'scope': fragment.get('scope', '').split('+'), 'state': fragment.get('state')}
