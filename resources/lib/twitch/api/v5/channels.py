# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/channels/

from twitch import keys, methods
from twitch.queries import V5Query as Qry
from twitch.queries import query
from twitch.api.parameters import Boolean, BroadcastType, Cursor, Direction, Duration, Language, VideoSort


@query
def get_channel():
    q = Qry('channels')
    return q


@query
def get_channel_by_id(channel_id):
    q = Qry('channels/{channel_id}')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


@query
def update_channel(channel_id, status=None, game=None, delay=None, channel_feed_enabled=None):
    q = Qry('channels/{channel_id}', method=methods.PUT)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    channel = {}
    if status is not None:
        channel[keys.STATUS] = status
    if game is not None:
        channel[keys.GAME] = game
    if delay is not None:
        channel[keys.DELAY] = delay
    if channel_feed_enabled is not None:
        channel[keys.CHANNEL_FEED_ENABLED] = Boolean.validate(channel_feed_enabled)
    q.add_data(keys.CHANNEL, channel)
    return q


@query
def get_channel_editors(channel_id):
    q = Qry('channels/{channel_id}/editors')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


@query
def get_channel_followers(channel_id, limit=25, offset=0, cursor='MA==', direction=Direction.DESC):
    q = Qry('channels/{channel_id}/follows')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.CURSOR, Cursor.validate(cursor), 'MA==')
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    return q


@query
def get_channel_teams(channel_id):
    q = Qry('channels/{channel_id}/teams')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


# Needs Authentication
@query
def get_channel_subscribers(channel_id, limit=25, offset=0, direction=Direction.ASC):
    q = Qry('channels/{channel_id}/subscriptions')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    return q


# Needs Authentication
@query
def check_channel_subscription(channel_id, user_id):
    q = Qry('channels/{channel_id}/subscriptions/{user_id}')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_urlkw(keys.USER_ID, user_id)
    return q


@query
def get_channel_videos(channel_id, limit=10, offset=0,
                       broadcast_type=BroadcastType.HIGHLIGHT,
                       hls=Boolean.FALSE, sort_by=VideoSort.TIME,
                       language=Language.ALL):
    q = Qry('channels/{id}/videos')
    q.add_urlkw(keys.ID, channel_id)
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.BROADCAST_TYPE, BroadcastType.validate(broadcast_type))
    q.add_param(keys.SORT, VideoSort.validate(sort_by), VideoSort.TIME)
    q.add_param(keys.LANGUAGE, Language.validate(language), Language.ALL)
    q.add_param(keys.HLS, Boolean.validate(hls), Boolean.FALSE)
    return q


@query
def start_commercial(channel_id, duration=30):
    q = Qry('channels/{channel_id}/commercial', method=methods.POST)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_data(keys.DURATION, Duration.validate(duration))
    return q


@query
def reset_stream_key(channel_id):
    q = Qry('channels/{channel_id}/stream_key', method=methods.DELETE)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


@query
def get_channel_community(channel_id):
    q = Qry('channels/{channel_id}/community')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


@query
def set_channel_community(channel_id, community_id):
    q = Qry('channels/{channel_id}/community/{community_id}', method=methods.PUT)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    return q


@query
def delete_channel_from_community(channel_id):
    q = Qry('channels/{channel_id}/community', method=methods.DELETE)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q
