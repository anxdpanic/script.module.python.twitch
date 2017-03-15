# -*- encoding: utf-8 -*-
# https://github.com/justintv/Twitch-API/blob/master/v3_resources/follows.md

from twitch import keys
from twitch.api.parameters import Direction, SortBy
from twitch.queries import V5Query as Qry
from twitch.queries import query
from twitch.api.parameters import Boolean


@query
def by_channel(name, limit=25, offset=0, direction=Direction.DESC):
    q = Qry('channels/{channel}/follows')
    q.add_urlkw(keys.CHANNEL, name)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    return q


@query
def by_id(identification, limit=25, offset=0, direction=Direction.DESC,
            sort_by=SortBy.CREATED_AT):
    q = Qry('users/{id}/follows/channels')
    q.add_urlkw(keys.ID, identification)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    q.add_param(keys.SORT_BY, sort_by, SortBy.CREATED_AT)
    return q


@query
def status(identification, target):
    q = Qry('users/{id}/follows/channels/{target}')
    q.add_urlkw(keys.ID, identification)
    q.add_urlkw(keys.TARGET, target)
    return q


# Needs Auth, needs PUT
@query
def follow(identification, target, notification=Boolean.FALSE):
    q = Qry('users/{id}/follows/channels/{target}', method='PUT')
    q.add_urlkw(keys.ID, identification)
    q.add_urlkw(keys.TARGET, target)
    q.add_data('notification', notification)
    return q


# Needs Auth, needs DELETE
@query
def unfollow(identification, target):
    q = Qry('users/{id}/follows/channels/{target}', method='DELETE')
    q.add_urlkw(keys.ID, identification)
    q.add_urlkw(keys.TARGET, target)
    return q

# Needs Auth
@query
def streams():
    raise NotImplementedError
