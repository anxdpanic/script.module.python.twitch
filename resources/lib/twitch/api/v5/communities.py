# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/communities/

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
    q = Qry('communities')
    q.add_param(keys.NAME, name)
    return q


@query
def by_id(community_id):
    q = Qry('communities/{id}')
    q.add_urlkw(keys.ID, community_id)
    return q
