# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/guides/using-the-twitch-api/

from twitch.queries import V5Query as Qry
from twitch.queries import query


# TODO token as parameter
@query
def root():
    return Qry('')
