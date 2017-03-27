# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/users/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query
from twitch.api.parameters import Boolean, Direction, SortBy
from twitch import methods


@query
def by_id(user_id):
    q = Qry('users/{id}')
    q.add_urlkw(keys.ID, user_id)
    return q


# Needs Authentication
@query
def user():
    q = Qry('user')
    return q


# Needs Authentication
@query
def streams():
    raise NotImplementedError


@query
def follows(user_id, limit=25, offset=0, direction=Direction.DESC,
            sort_by=SortBy.CREATED_AT):
    q = Qry('users/{id}/follows/channels')
    q.add_urlkw(keys.ID, user_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    q.add_param(keys.SORT_BY, sort_by, SortBy.CREATED_AT)
    return q


@query
def follow_status(user_id, target_id):
    q = Qry('users/{id}/follows/channels/{target}')
    q.add_urlkw(keys.ID, user_id)
    q.add_urlkw(keys.TARGET, target_id)
    return q


# Needs Authentication, needs PUT
@query
def follow(user_id, target_id, notification=Boolean.FALSE):
    q = Qry('users/{id}/follows/channels/{target}', method=methods.PUT)
    q.add_urlkw(keys.ID, user_id)
    q.add_urlkw(keys.TARGET, target_id)
    q.add_data(keys.NOTIFICATION, Boolean.validate(notification), Boolean.FALSE)
    return q


# Needs Authentication, needs DELETE
@query
def unfollow(user_id, target_id):
    q = Qry('users/{id}/follows/channels/{target}', method=methods.DELETE)
    q.add_urlkw(keys.ID, user_id)
    q.add_urlkw(keys.TARGET, target_id)
    return q


# Needs Authentication
@query
def blocks(user_id, limit=25, offset=0):
    q = Qry('users/{id}/blocks')
    q.add_urlkw(keys.ID, user_id)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    return q


# Needs Authentication, needs PUT
@query
def add_block(user_id, target_id):
    q = Qry('users/{id}/blocks/{target}', method=methods.PUT)
    q.add_urlkw(keys.ID, user_id)
    q.add_urlkw(keys.TARGET, target_id)
    return q


# Needs Authentication, needs DELETE
@query
def del_block(user_id, target_id):
    q = Qry('users/{id}/blocks/{target}', method=methods.DELETE)
    q.add_urlkw(keys.ID, user_id)
    q.add_urlkw(keys.TARGET, target_id)
    return q


# Needs Authentication
@query
def subscription_status(user_id, channel_id):
    raise NotImplementedError
