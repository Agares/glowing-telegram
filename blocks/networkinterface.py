import netifaces

import icons
from blockcontent import BlockContent


class NetworkInterface(object):
    def __init__(self, interface_name, icon=icons.WIFI):
        self.icon = icon
        self.interface_name = interface_name
        self.address = ""
        self.update()

    def update(self):
        addresses = netifaces.ifaddresses(self.interface_name)
        if not (netifaces.AF_INET in addresses):
            self.address = None
            return

        self.address = addresses[netifaces.AF_INET][0]["addr"]

    def full_text(self):
        content = BlockContent()
        if self.address is None:
            return content

        content.append_icon(self.icon)
        content.append_text("  ")
        content.append_text(self.address)

        return content
