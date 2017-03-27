# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/ingests/

from twitch.queries import V5Query as Qry
from twitch.queries import query


@query
def get():
    q = Qry('ingests')
    return q
