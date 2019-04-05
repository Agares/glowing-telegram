import urllib.request, urllib.error, urllib.parse

import time

import icons
from blockcontent import BlockContent


class ExternalIp(object):
    def __init__(self):
        self.ip = "unknown"
        self.last_update = 0

    def update(self):
        now = time.time()

        if(now - self.last_update) > 60:
            try:
                self.ip = urllib.request.urlopen("http://utils.agares.info/remoteip.php", None, 1).read()
            except:
                self.ip = "unknown"

            self.last_update = now

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.GLOBE)
        content.append_text("  " + self.ip)

        return content
