#!/usr/bin/env python

from ..common import *
from ..extractor import VideoExtractor

import json

class MusicPlayOn(VideoExtractor):
    name = "MusicPlayOn"

    stream_types = [
        {'id': '720p HD'},
        {'id': '360p SD'},
    ]

    def prepare(self, **kwargs):
        content = get_content(self.url)

        self.title = match1(content,
                            r'setup\[\'title\'\] = "([^"]+)";')

        for s in self.stream_types:
            quality = s['id']
            src = match1(content,
                         r'src: "([^"]+)", "data-res": "%s"' % quality)
            if src is not None:
                url = 'http://en.musicplayon.com%s' % src
                self.streams[quality] = {'url': url}

site = MusicPlayOn()
download = site.download_by_url
# TBD: implement download_playlist
