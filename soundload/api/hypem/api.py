# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import json

import finch
from . import models


BASE_URL = "https://api.hypem.com/v2"


class Tracks(finch.Collection):
    model = models.Track

    def __init__(self, itemid, *args, **kwargs):
        self.itemid = itemid
        super(Tracks, self).__init__(*args, **kwargs)

    @property
    def url(self):
        return "{base}/tracks/{itemid}".format(base=BASE_URL,
                                               itemid=self.itemid)

    def decode(self, response):
        return json.loads(response.body)


if __name__ == "__main__":
    tracks =
