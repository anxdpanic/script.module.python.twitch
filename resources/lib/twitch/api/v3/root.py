# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://dev.twitch.tv/docs/v3/reference/root/

from twitch.queries import V3Query as Qry
from twitch.queries import query


# TODO token as parameter
@query
def root():
    return Qry('')
