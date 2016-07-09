import pulsectl

import colors
import icons
from blockcontent import BlockContent


class PulseAudio:
    def __init__(self, sink_index=1):
        self.pulse = pulsectl.Pulse()
        self.sink_index = sink_index
        self.volume = 0
        self.muted = False
        self.update()

    def update(self):
        sinks = self.pulse.sink_list()
        sink = sinks[self.sink_index]

        self.volume = self.pulse.volume_get_all_chans(sink)
        self.muted = sink.mute

    def full_text(self):
        content = BlockContent()
        content.append_icon(icons.VOLUME_OFF if self.muted else icons.VOLUME_UP)
        content.append_text("  {0:3.0f}%".format(self.volume*100), colors.MUTED if self.muted else colors.NORMAL)

        return content
