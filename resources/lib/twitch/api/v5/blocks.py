# -*- encoding: utf-8 -*-
# https://github.com/justintv/Twitch-API/blob/master/v3_resources/blocks.md

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query


# Needs Authentification
@query
def by_id(identification, limit=25, offset=0):
    q = Qry('users/{id}/blocks')
    q.add_urlkw(keys.ID, identification)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    return q


# Needs Authentification, needs PUT
@query
def add_block(identification, target):
    q = Qry('users/{id}/blocks/{target}', method='PUT')
    q.add_urlkw(keys.ID, identification)
    q.add_urlkw(keys.TARGET, target)
    return q


# Needs Authentification, needs DELETE
@query
def del_block(identification, target):
    q = Qry('users/{id}/blocks/{target}', method='DELETE')
    q.add_urlkw(keys.ID, identification)
    q.add_urlkw(keys.TARGET, target)
    return q
