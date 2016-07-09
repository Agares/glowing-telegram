import mpd

import icons
from blockcontent import BlockContent


class MpdBlock:
    def __init__(self):
        self.mpd_client = mpd.MPDClient(True)
        self.mpd_client.connect("localhost", 6600)
        self.is_playing = False
        self.artist = ""
        self.title = ""

        self.update()

    def update(self):
        current_song = self.mpd_client.currentsong()
        status = self.mpd_client.status()

        self.is_playing = status["state"] == "play"
        self.artist = current_song["artist"]
        self.title = current_song["title"]

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.PLAY if self.is_playing else icons.PAUSE)
        content.append_text("  {0} - {1}".format(self.artist, self.title))

        return content
