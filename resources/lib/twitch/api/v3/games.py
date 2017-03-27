# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://dev.twitch.tv/docs/v3/reference/games/

from twitch import keys
from twitch.queries import V3Query as Qry
from twitch.queries import query


@query
def top(limit=10, offset=0):
    q = Qry('games/top')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    return q
