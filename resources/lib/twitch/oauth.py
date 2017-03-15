# -*- encoding: utf-8 -*-

from twitch import CLIENT_ID
from twitch import scopes
from oauthlib.oauth2 import MobileApplicationClient


class MobileClient:
    _auth_base_url = 'https://api.twitch.tv/kraken/oauth2/authorize'

    def __init__(self, client_id=''):
        self.client_id = client_id if client_id else CLIENT_ID
        self.client = MobileApplicationClient(client_id=client_id)
        self.parse_request_uri_response = self.client.parse_request_uri_response

    def prepare_request_uri(self, redirect_uri='http://localhost:3000/', scope=list()):
        return self.client.prepare_request_uri(self._auth_base_url, redirect_uri=redirect_uri, scope=scope)
