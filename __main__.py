#!/usr/bin/python2
# coding=utf-8
import json
import time
import sys

import config
from eventdispatcher import EventDispatcher
from eventreader import EventReader


def block_to_dict(b):
    return {
        "full_text": unicode(b.full_text()),
        "markup": "pango",
        "name": type(b).__name__,
        "instance": str(id(b))
    }


if __name__ == "__main__":
    event_dispatcher = EventDispatcher(EventReader())
    print json.dumps({"version": 1, "click_events": True})
    print "["

    while True:
        for block in config.blocks:
            block.update()

        event_dispatcher.dispatch(config.blocks)

        serializable_block_content = map(block_to_dict, config.blocks)
        print json.dumps(serializable_block_content) + ","

        sys.stdout.flush()
        time.sleep(0.25)
