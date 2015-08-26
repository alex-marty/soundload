# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from booby import Model, fields


class Track(Model):
    """
    Model for a track from the Hypem API.

    Example track json data as returned by a Hypem API call to
    https://api.hypem.com/v2/tracks/2cr8m:
    {
        itemid: "2cr8m",
        artist: "Axwell/\Ingrosso",
        title: "Sun Is Shining (M-22 Remix)",
        dateposted: 1439439109,
        siteid: 14143,
        sitename: "POP ON AND ON",
        posturl: "http://poponandon.com/remix-alert-alesso-ingrosso-sun-is-shining-m-22-remix/",
        postid: 2739879,
        loved_count: 491,
        posted_count: 2,
        thumb_url: "http://static-ak.hypem.net/thumbs_new/a7/2739879.jpg",
        thumb_url_medium: "http://static-ak.hypem.net/thumbs_new/a7/2739879_120.jpg",
        thumb_url_large: "http://static-ak.hypem.net/thumbs_new/4f/2738767_320.jpg",
        time: 364,
        description: "Axwell /\ Ingrosso’s “Sun Is Shining” receives the remix treatment from M-22 and the result is pretty fucking epic. M-22 bring the feels here, the build and the drop create a driving energy that commands hands-in-the-air action! Get into the vibes below v",
        itunes_link: "http://hypem.com/go/itunes_search/Axwell/\Ingrosso"
    }
    """

    itemid = fields.String()
    artist = fields.String()
    title = fields.String()
    dateposted = fields.Integer()
    siteid = fields.Integer()
    sitename = fields.String()
    posturl = fields.String()
    postid = fields.Integer()
    loved_count = fields.Integer()
    posted_count = fields.Integer()
    thumb_url = fields.String()
    thumb_url_medium = fields.String()
    thumb_url_large = fields.String()
    time = fields.Integer()
    description = fields.String()
    itunes_link = fields.String()

    ts_loved = fields.Integer()
    p_id = fields.Integer()

    def is_favorite(self):
        return self.ts_loved is not None

if __name__ == "__main__":
    import requests
    from pyutils import jsonutils
    from pprint import pprint
    track_dict = jsonutils.load_file("C:/Users/Utilisateur/Dropbox/Dev/soundload/data/examples/api.track.item_id.json")
    t = Track(**track_dict)
    print(t)
    print(t.is_valid)

    favs = requests.get("https://api.hypem.com/v2/users/Macfli/favorites").json()
    pprint([t for t in favs if "p_id" in t or "ts_loved" in t])
    f = [Track(**t) for t in favs]
    print(f)
    nv = [t for t in f if not t.is_valid]
    t = f[0]
    print([t for t in f if t.p_id is not None])


