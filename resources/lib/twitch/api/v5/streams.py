# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/streams/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query
from twitch.api.parameters import StreamType


@query
def by_id(channel_id, stream_type=StreamType.LIVE):
    q = Qry('streams/{id}')
    q.add_urlkw(keys.ID, channel_id)
    q.add_param(keys.STREAM_TYPE, StreamType.validate(stream_type), StreamType.LIVE)
    return q


@query
def all(game=None, channel_ids=None, community_id=None, language=None, limit=25, offset=0, client_id=None):
    q = Qry('streams')
    q.add_param(keys.GAME, game)
    q.add_param(keys.CHANNEL, channel_ids)
    q.add_param(keys.COMMUNITY_ID, community_id)
    q.add_param(keys.LANGUAGE, language)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.CLIENT_ID, client_id)
    return q


@query
def featured(limit=25, offset=0):
    q = Qry('streams/featured')
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    return q


@query
def summary(game=None):
    q = Qry('streams/summary')
    q.add_param(keys.GAME, game)
    return q


# Needs Authentication
@query
def followed(stream_type=StreamType.LIVE, limit=25, offset=0):
    q = Qry('streams/followed')
    q.add_param(keys.STREAM_TYPE, StreamType.validate(stream_type), StreamType.LIVE)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    return q
