# -*- encoding: utf-8 -*-

from twitch.logging import log  # NOQA

log.warning('By using this module you are violating the Twitch TOS')  # NOQA

from twitch import keys
from twitch.api.parameters import Boolean
from twitch.parser import m3u8, clip_embed
from twitch.queries import ClipsQuery, HiddenApiQuery, UsherQuery
from twitch.queries import query


@query
def channel_token(channel):
    q = HiddenApiQuery('channels/{channel}/access_token')
    q.add_urlkw(keys.CHANNEL, channel)
    q.add_param(keys.NEED_HTTPS, Boolean.TRUE)
    return q


@query
def vod_token(video_id):
    q = HiddenApiQuery('vods/{vod}/access_token')
    q.add_urlkw(keys.VOD, video_id)
    q.add_param(keys.NEED_HTTPS, Boolean.TRUE)
    return q


@query
def _legacy_video(video_id):
    q = HiddenApiQuery('videos/{id}')
    q.add_urlkw(keys.ID, video_id)
    return q


@m3u8
@query
def live(channel):
    token = channel_token(channel)

    q = UsherQuery('api/channel/hls/{channel}.m3u8')
    q.add_urlkw(keys.CHANNEL, channel)
    q.add_param(keys.SIG, token[keys.SIG])
    q.add_param(keys.TOKEN, token[keys.TOKEN])
    q.add_param(keys.ALLOW_SOURCE, Boolean.TRUE)
    q.add_param(keys.ALLOW_SPECTRE, Boolean.TRUE)
    return q


@m3u8
@query
def _vod(video_id):
    video_id = video_id[1:]

    token = vod_token(video_id)

    q = UsherQuery('vod/{id}')
    q.add_urlkw(keys.ID, video_id)
    q.add_param(keys.NAUTHSIG, token[keys.SIG])
    q.add_param(keys.NAUTH, token[keys.TOKEN])
    q.add_param(keys.ALLOW_SOURCE, Boolean.TRUE)
    return q


def video(video_id):
    if video_id.startswith('videos'):
        video_id = 'v' + video_id[6:]
        return _vod(video_id)
    elif video_id.startswith('v'):
        return _vod(video_id)
    elif video_id.startswith(('a', 'c')):
        return _legacy_video(video_id)
    else:
        raise NotImplementedError('Unknown Video Type')


@clip_embed
@query
def clip(slug):
    q = ClipsQuery('embed')
    q.add_param(keys.CLIP, slug)
    return q
