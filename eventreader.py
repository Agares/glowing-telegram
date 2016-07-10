import json
import select
import sys


class EventReader(object):
    def __init__(self):
        self.poller = select.poll()
        self.poller.register(sys.stdin, select.POLLIN)

    def read(self):
        if not self.poller.poll(250):
            return None

        line = sys.stdin.readline().strip()
        if line == "[":
            return None

        return json.loads(line.strip(","))
