# -*- encoding: utf-8 -*-

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query


@query
def top(limit=10, cursor=0):
    q = Qry('communities/top')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.CURSOR, cursor, 0)
    return q


@query
def by_name(name):
    q = Qry('communities?name={communities}')
    q.add_urlkw(keys.COMMUNITIES, name)
    return q


@query
def by_id(identification):
    q = Qry('communities/{id}')
    q.add_urlkw(keys.ID, identification)
    return q
