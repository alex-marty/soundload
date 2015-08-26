# -*- coding: utf-8 -*-

from pprint import pprint

from api.hypemapi import HypemAPI

hm = HypemAPI()
print(hm.get_favorites("Macfli"))
