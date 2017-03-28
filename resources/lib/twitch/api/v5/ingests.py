# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/ingests/

from twitch.queries import V5Query as Qry
from twitch.queries import query


# required scope: none
@query
def get_ingest_servers():
    q = Qry('ingests')
    return q
