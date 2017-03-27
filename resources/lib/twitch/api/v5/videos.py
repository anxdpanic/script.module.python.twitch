# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/videos/

from twitch import keys
from twitch.api.parameters import BroadcastType, Period
from twitch.queries import V5Query as Qry
from twitch.queries import query


@query
def by_id(video_id):
    q = Qry('videos/{id}')
    q.add_urlkw(keys.ID, video_id)
    return q


@query
def top(limit=10, offset=0, game=None, period=Period.WEEK):
    q = Qry('videos/top')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.GAME, game)
    q.add_param(keys.PERIOD, Period.validate(period), Period.WEEK)
    return q


# Needs Authentication
@query
def followed(limit=10, offset=0,
             broadcast_type=BroadcastType.ARCHIVE):
    q = Qry('videos/followed')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.BROADCAST_TYPE, BroadcastType.validate(broadcast_type), BroadcastType.ARCHIVE)
    return q
