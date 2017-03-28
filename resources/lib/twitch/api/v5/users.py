# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/users/

from twitch import keys, methods
from twitch.api.parameters import Boolean, Direction, SortBy
from twitch.queries import V5Query as Qry
from twitch.queries import query


# Needs Authentication
@query
def get_user():
    q = Qry('user')
    return q


@query
def get_user_by_id(user_id):
    q = Qry('users/{user_id}')
    q.add_urlkw(keys.USER_ID, user_id)
    return q


@query
def get_user_emotes(user_id):
    q = Qry('users/{user_id}/emotes')
    q.add_urlkw(keys.USER_ID, user_id)
    return q


@query
def check_subscription_by_channel(user_id, channel_id):
    q = Qry('users/{user_id}/subscriptions/{channel_id}')
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


@query
def get_user_follows(user_id, limit=25, offset=0, direction=Direction.DESC,
                     sort_by=SortBy.CREATED_AT):
    q = Qry('users/{user_id}/follows/channels')
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    q.add_param(keys.SORT_BY, sort_by, SortBy.CREATED_AT)
    return q


@query
def check_follows_by_channel(user_id, channel_id):
    q = Qry('users/{user_id}/follows/channels/{channel_id}')
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


# Needs Authentication, needs PUT
@query
def follow_channel(user_id, channel_id, notifications=Boolean.FALSE):
    q = Qry('users/{user_id}/follows/channels/{channel_id}', method=methods.PUT)
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_data(keys.NOTIFICATIONS, Boolean.validate(notifications), Boolean.FALSE)
    return q


# Needs Authentication, needs DELETE
@query
def unfollow_channel(user_id, channel_id):
    q = Qry('users/{user_id}/follows/channels/{channel_id}', method=methods.DELETE)
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


# Needs Authentication
@query
def get_user_blocks(user_id, limit=25, offset=0):
    q = Qry('users/{user_id}/blocks')
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    return q


# Needs Authentication, needs PUT
@query
def block_user(user_id, target_id):
    q = Qry('users/{user_id}/blocks/{target_id}', method=methods.PUT)
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_urlkw(keys.TARGET_ID, target_id)
    return q


# Needs Authentication, needs DELETE
@query
def unblock_user(user_id, target_id):
    q = Qry('users/{user_id}/blocks/{target_id}', method=methods.DELETE)
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_urlkw(keys.TARGET_ID, target_id)
    return q


@query
def create_connection_to_vhs(identifier):
    q = Qry('user/vhs', method=methods.PUT)
    q.add_data(keys.IDENTIFIER, identifier)
    return q


@query
def check_connection_to_vhs():
    q = Qry('user/vhs')
    return q


@query
def delete_connection_to_vhs():
    q = Qry('user/vhs', method=methods.DELETE)
    return q
