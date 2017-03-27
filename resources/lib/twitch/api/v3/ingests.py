# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://dev.twitch.tv/docs/v3/reference/ingests/

from twitch.queries import V3Query as Qry
from twitch.queries import query


@query
def get():
    q = Qry('ingests')
    return q
