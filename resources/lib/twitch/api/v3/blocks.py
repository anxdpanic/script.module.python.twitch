# -*- encoding: utf-8 -*-
# deprecated @ Feb. 14, 2017
# discontinued @ Feb. 13, 2018
# https://dev.twitch.tv/docs/v3/reference/blocks/

from twitch.queries import query


# Needs Authentication
@query
def by_name(user):
    raise NotImplementedError


# Needs Authentication, needs PUT
@query
def add_block(user, target):
    raise NotImplementedError


# Needs Authentication, needs DELETE
@query
def del_block(user, target):
    raise NotImplementedError
