# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/games/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query


# required scope: none
@query
def get_top(limit=10, offset=0):
    q = Qry('games/top')
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.OFFSET, offset, 0)
    return q
