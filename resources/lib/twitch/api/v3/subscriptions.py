# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://dev.twitch.tv/docs/v3/reference/subscriptions/

from twitch.api.parameters import Direction
from twitch.queries import query


# Needs Authentication
@query
def by_channel(channel, limit=25, offset=0, direction=Direction.ASC):
    raise NotImplementedError


# Needs Authentication
@query
def channel_to_user(channel, user):
    raise NotImplementedError


# Needs Authentication
@query
def user_to_channel(user, channel):
    raise NotImplementedError
