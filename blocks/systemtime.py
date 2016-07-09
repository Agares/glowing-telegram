import time

import icons
from blockcontent import BlockContent


class SystemTime(object):
    def __init__(self):
        pass

    def update(self):
        pass

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.CALENDAR)
        content.append_text("  ")
        content.append_text(time.strftime("%Y-%m-%d %H:%M:%S"))

        return content
