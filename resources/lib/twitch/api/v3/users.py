# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://dev.twitch.tv/docs/v3/reference/users/

from twitch import keys
from twitch.queries import V3Query as Qry
from twitch.queries import query


@query
def by_name(name):
    q = Qry('users/{user}')
    q.add_urlkw(keys.USER, name)
    return q


# Needs Authentification
@query
def user():
    raise NotImplementedError


# Needs Authentification
@query
def streams():
    raise NotImplementedError


# Needs Authentification
@query
def videos():
    raise NotImplementedError
