#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import json
import os
import re

import gevent
from gevent import queue

from redylitics.endpoints import update_channels, update_videos, update_video_ads, read_channels, read_videos, read_video_ads
from redylitics.utils import LOGGER, GIF

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs


# init the gevent queue
CHANNEL_QUEUE = queue.Queue()
VIDEO_QUEUE = queue.Queue()
VIDEO_AD_QUEUE = queue.Queue()
FLUSH_INTERVAL = os.environ.get("REDYLITICS_FLUSH_INTERVAL", 10)  # seconds

# endpoint regexes
REDYLITICS_REFERER_EXTRACT_REGEX = os.environ.get("REDYLITICS_REFERER_EXTRACT_REGEX", ".*")
REDYLITICS_REFERER_ANCHORED_REGEX = os.environ.get("REDYLITICS_REFERER_ANCHORED_REGEX", ".*")
REFERER_EXTRACT_REGEX = re.compile(REDYLITICS_REFERER_EXTRACT_REGEX)
REFERER_ANCHORED_REGEX = re.compile(REDYLITICS_REFERER_ANCHORED_REGEX)

UPDATE_CHANNEL_REGEX = re.compile(r"^/pageview\.gif$")
UPDATE_VIDEO_REGEX = re.compile(r"^/video\.gif$")
UPDATE_VIDEO_AD_REGEX = re.compile(r"^/video-ad\.gif$")

READ_CHANNEL_REGEX = re.compile(r"^/pageview\.json$")
READ_VIDEO_REGEX = re.compile(r"^/video\.json$")
READ_VIDEO_AD_REGEX = re.compile(r"^/video-ad\.json$")


# get http referer
def get_referer(env):
    try:
        ref = env["HTTP_REFERER"]
    except KeyError:
        return None
    if REFERER_ANCHORED_REGEX.search(ref):
        matches = REFERER_EXTRACT_REGEX.findall(ref)
        if len(matches):
            return matches[0]
    return None


# update page views
def channel_counts():
    while 1:
        gevent.sleep(FLUSH_INTERVAL)
        channels = Counter()
        while 1:
            try:
                channel = CHANNEL_QUEUE.get_nowait()
                channels[channel] += 1
            except queue.Empty:
                break
            except Exception as e:
                LOGGER.exception(e)
                break
        if len(channels):
            gevent.spawn(update_channels, channels)


# update videos
def video_counts():
    while 1:
        gevent.sleep(FLUSH_INTERVAL)
        videos = Counter()
        while 1:
            try:
                video = VIDEO_QUEUE.get_nowait()
                videos[video] += 1
            except queue.Empty:
                break
            except Exception as e:
                LOGGER.exception(e)
                break
        if len(videos):
            gevent.spawn(update_videos, videos)


# update video ads
def video_ad_counts():
    while 1:
        gevent.sleep(FLUSH_INTERVAL)
        video_ads = Counter()
        while 1:
            try:
                ad = VIDEO_AD_QUEUE.get_nowait()
                video_ads[ad] += 1
            except queue.Empty:
                break
            except Exception as e:
                LOGGER.exception(e)
                break
        if len(video_ads):
            gevent.spawn(update_video_ads, video_ads)


# create the wait loops
gevent.spawn(channel_counts)
gevent.spawn(video_counts)
gevent.spawn(video_ad_counts)


# main loop
def application(env, start_response):
    # get the request path
    path = env["PATH_INFO"].lower()

    # get the query params
    try:
        params = parse_qs(env["QUERY_STRING"])
    except KeyError:
        params = None

    # get the http referer header
    referer = get_referer(env)

    # update page views
    if UPDATE_CHANNEL_REGEX.match(path) and referer:
        start_response("200 OK", [("Content-Type", "image/gif")])
        yield GIF
        CHANNEL_QUEUE.put(referer)

    # update videos
    elif UPDATE_VIDEO_REGEX.match(path) and referer and params:
        start_response("200 OK", [("Content-Type", "image/gif")])
        yield GIF
        video = params.get("video", [None])[0]
        event = params.get("event", [None])[0]
        VIDEO_QUEUE.put((video, event))

    # update video ads
    elif UPDATE_VIDEO_AD_REGEX.match(path) and referer and params:
        start_response("200 OK", [("Content-Type", "image/gif")])
        yield GIF
        video = params.get("video_ad", [None])[0]
        event = params.get("event", [None])[0]
        VIDEO_AD_QUEUE.put((video, event))

    # read page views
    elif READ_CHANNEL_REGEX.match(path) and params:
        channel = params.get("channel", [None])[0]
        res, ok = read_channels(channel)
        if ok:
            start_response("200 OK", [("Content-Type", "application/json")])
            yield json.dumps(res)
        else:
            start_response("400 Bad Request", [("Content-Type", "application/json")])
            json.dumps({"error": res})

    # read videos
    elif READ_VIDEO_REGEX.match(path) and params:
        video = params.get("video", [None])[0]
        event = params.get("event", [None])[0]
        res, ok = read_videos(video, event)
        if ok:
            start_response("200 OK", [("Content-Type", "application/json")])
            yield json.dumps(res)
        else:
            start_response("400 Bad Request", [("Content-Type", "application/json")])
            json.dumps({"error": res})

    # read video ads
    elif READ_VIDEO_AD_REGEX.match(path) and params:
        video = params.get("video_ad", [None])[0]
        event = params.get("event", [None])[0]
        res, ok = read_video_ads(video, event)
        if ok:
            start_response("200 OK", [("Content-Type", "application/json")])
            yield json.dumps(res)
        else:
            start_response("400 Bad Request", [("Content-Type", "application/json")])
            json.dumps({"error": res})

    # bologna
    else:
        start_response("403 Forbidden", [("Content-Type", "text/plain")])
        yield "(\/) (°,,,°) (\/)"
