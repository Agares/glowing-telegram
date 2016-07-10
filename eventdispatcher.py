from eventreader import EventReader


class EventDispatcher(object):
    def __init__(self, event_reader):
        assert isinstance(event_reader, EventReader)
        self.event_reader = event_reader

    def dispatch(self, blocks):
        event = self.event_reader.read()

        if event is None:
            return

        for block in blocks:
            if str(id(block)) != event['instance']:
                continue

            if 'click' not in dir(block):
                continue

            block.click()
