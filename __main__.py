#!/usr/bin/python
# coding=utf-8
import json
import time
import sys

import config


def block_to_dict(b):
    return {"full_text": unicode(b.full_text()), "markup": "pango"}


if __name__ == "__main__":
    print json.dumps({"version": 1})
    print "["

    while True:
        for block in config.blocks:
            block.update()

        serializable_block_content = map(block_to_dict, config.blocks)
        print json.dumps(serializable_block_content) + ","

        sys.stdout.flush()
        time.sleep(0.25)
