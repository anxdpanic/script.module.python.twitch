# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/collections/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query
from twitch.api.parameters import Boolean, Cursor
from twitch import methods


@query
def get_collection_metadata(collection_id):
    q = Qry('collections/{collection_id}')
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    return q


@query
def get_collection(collection_id, include_all=Boolean.FALSE):
    q = Qry('collections/{collection_id}/items')
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    q.add_param(keys.INCLUDE_ALL_ITEMS, Boolean.validate(include_all), Boolean.FALSE)
    return q


@query
def get_collections(channel_id, limit=10, cursor='MA==', containing_item=None):
    q = Qry('channels/{channel_id}/collections')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.CURSOR, Cursor.validate(cursor), 'MA==')
    q.add_param(keys.CONTAINING_ITEM, containing_item, None)  # 'video:<video_id>'
    return q


@query
def create_collection(channel_id, title):
    q = Qry('channels/{channel_id}/collections', method=methods.POST)
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    q.add_data(keys.TITLE, title)
    return q


@query
def update_collection(collection_id, title):
    q = Qry('collections/{collection_id}', method=methods.PUT)
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    q.add_data(keys.TITLE, title)
    return q


@query
def create_collection_thumbnail(collection_id, item_id):
    q = Qry('collections/{collection_id}/thumbnail', method=methods.PUT)
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    q.add_data(keys.ITEM_ID, item_id)
    return q


@query
def create_collection(collection_id):
    q = Qry('collections/{collection_id}', method=methods.DELETE)
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    return q


@query
def add_to_collection(collection_id, video_id):
    q = Qry('collections/{collection_id}/items', method=methods.POST)
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    q.add_data(keys.ID, video_id)
    q.add_data(keys.TYPE, 'video')  # must be 'video'
    return q


@query
def delete_from_collection(collection_id, item_id):
    q = Qry('collections/{collection_id}/items/{item_id}', method=methods.DELETE)
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    q.add_urlkw(keys.ITEM_ID, item_id)
    return q


@query
def move_in_collection(collection_id, item_id, position):
    q = Qry('collections/{collection_id}/items/{item_id}', method=methods.PUT)
    q.add_urlkw(keys.COLLECTION_ID, collection_id)
    q.add_urlkw(keys.ITEM_ID, item_id)
    q.add_data(keys.POSITION, position)
    return q
