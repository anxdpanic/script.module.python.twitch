# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://github.com/justintv/Twitch-API/blob/master/v3_resources/ingests.md

from twitch.queries import V3Query as Qry
from twitch.queries import query


@query
def get():
    q = Qry('ingests')
    return q
