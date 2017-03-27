# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/channels/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query
from twitch.api.parameters import Boolean, BroadcastType, Direction


@query
def by_id(channel_id):
    q = Qry('channels/{id}')
    q.add_urlkw(keys.ID, channel_id)
    return q


@query
def channel():
    raise NotImplementedError


@query
def editors(name):
    raise NotImplementedError


# TODO needs Authentication and put requests
@query
def update(name, status=None, game=None, delay=0):
    raise NotImplementedError


# TODO needs auth
@query
def delete(name):
    raise NotImplementedError


# TODO needs auth, needs POST request
@query
def commercial(name, length=30):
    raise NotImplementedError


@query
def teams(channel_id):
    q = Qry('channels/{id}/teams')
    q.add_urlkw(keys.ID, channel_id)
    return q


@query
def followers(channel_id, limit=25, offset=0, direction=Direction.DESC):
    q = Qry('channels/{id}/follows')
    q.add_urlkw(keys.ID, channel_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    return q


# Needs Authentication
@query
def subscribers(channel_id, limit=25, offset=0, direction=Direction.ASC):
    raise NotImplementedError


# Needs Authentication
@query
def subscription_status(channel_id, user_id):
    raise NotImplementedError


@query
def videos(channel_id, limit=10, offset=0,
           broadcast_type=BroadcastType.ARCHIVE, hls=Boolean.FALSE):
    q = Qry('channels/{id}/videos')
    q.add_urlkw(keys.ID, channel_id)
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.BROADCAST_TYPE, BroadcastType.validate(broadcast_type), BroadcastType.ARCHIVE)
    q.add_param(keys.HLS, Boolean.validate(hls), Boolean.FALSE)
    return q
