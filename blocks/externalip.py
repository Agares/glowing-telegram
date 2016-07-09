import urllib2

import time

import icons
from blockcontent import BlockContent


class ExternalIp:
    def __init__(self):
        self.ip = "0.0.0.0"
        self.last_update = 0

    def update(self):
        now = time.time()

        if(now - self.last_update) > 60:
            self.ip = urllib2.urlopen("http://utils.agares.info/remoteip.php").read()
            self.last_update = now

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.GLOBE)
        content.append_text("  " + self.ip)

        return content
