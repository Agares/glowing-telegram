import mpd

import icons
from blockcontent import BlockContent


class MpdBlock(object):
    def __init__(self):
        self.mpd_client = mpd.MPDClient(True)
        self.mpd_client.connect("localhost", 6600)
        self.is_playing = False
        self.artist = u""
        self.title = u""

        self.update()

    def update(self):
        current_song = self.mpd_client.currentsong()
        status = self.mpd_client.status()

        self.is_playing = status["state"] == "play"
        self.artist = current_song["artist"] if "artist" in current_song else ""
        self.title = current_song["title"] if "title" in current_song else ""

    def full_text(self):
        if self.artist == "" or self.title == "":
            return u""

        content = BlockContent()
        content.append_icon(icons.PLAY if self.is_playing else icons.PAUSE)
        content.append_text(u"  {0} - {1}".format(self.artist, self.title))

        return content

    def click(self):
        self.mpd_client.pause(int(self.is_playing))