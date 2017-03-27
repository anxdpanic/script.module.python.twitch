# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/chat/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query


@query
def emoticons_by_set(emotesets=list()):
    q = Qry('chat/emoticon_images')
    q.add_param(keys.EMOTESETS, emotesets, list())
    return q


@query
def badges(name):
    q = Qry('chat/{channel}/badges')
    q.add_urlkw(keys.CHANNEL, name)
    return q


@query
def emoticons():
    q = Qry('chat/emoticons')
    return q
