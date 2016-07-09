import os

import colors
import icons
from blockcontent import BlockContent


class SystemLoad:
    def __init__(self):
        self.load = 0.0
        self.update()

    def update(self):
        self.load = os.getloadavg()[0]

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.BOLT)
        content.append_text("  {0:2.2f}".format(self.load))

        return content

    def color(self):
        return colors.NORMAL