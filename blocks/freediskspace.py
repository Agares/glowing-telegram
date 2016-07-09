import os

import icons
from blockcontent import BlockContent


class FreeDiskSpace(object):
    def __init__(self, mountpoint="/"):
        self.mountpoint = mountpoint
        self.available_space = 0
        self.update()

    def update(self):
        stat = os.statvfs(self.mountpoint)
        self.available_space = stat.f_bavail * stat.f_bsize

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.HDD_O)
        content.append_text("  " + self.mountpoint)
        content.append_text(" {0:2.1f} GB".format(self.available_space / (1024 ** 3)))

        return content
