# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/videos/

from twitch import keys
from twitch.api.parameters import BroadcastType, Period
from twitch.queries import V5Query as Qry
from twitch.queries import HiddenApiQuery as HQry
from twitch.queries import query


# required scope: none
@query
def by_id(video_id):
    q = Qry('videos/{video_id}')
    q.add_urlkw(keys.VIDEO_ID, video_id)
    return q


# required scope: none
@query
def get_top(limit=10, offset=0, game=None, period=Period.WEEK, broadcast_type=BroadcastType.HIGHLIGHT):
    q = Qry('videos/top')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.GAME, game)
    q.add_param(keys.PERIOD, Period.validate(period), Period.WEEK)
    q.add_param(keys.BROADCAST_TYPE, BroadcastType.validate(broadcast_type))
    return q


# required scope: user_read
@query
def get_followed(limit=10, offset=0, broadcast_type=BroadcastType.HIGHLIGHT):
    q = Qry('videos/followed')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.BROADCAST_TYPE, BroadcastType.validate(broadcast_type))
    return q


# required scope: none
# undocumented / unsupported
@query
def _by_id(video_id):
    q = HQry('videos/{video_id}')
    q.add_urlkw(keys.VIDEO_ID, video_id)
    return q
