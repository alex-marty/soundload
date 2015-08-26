# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:31:07 2015

@author: Alexandre Marty
"""

import requests
import json

favorites_req = requests.get("https://api.hypem.com/v2/users/Macfli/favorites")
favs = json.loads(favorites_req.content)
print(favs.keys)
