import os
import random
import sys
import time
import logging
from logstash_formatter import LogstashFormatterV1
from itertools import count

if any("KUBERNETES" in k for k in os.environ):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(LogstashFormatterV1())
    logging.root.setLevel("INFO")
    logging.root.addHandler(handler)
else:
    logging.basicConfig(level=logging.INFO)

logga = logging.getLogger("__name__")


while True:
    for i in count():
        logga.info("Up up up! %s", i)
        if i % 1000 == 0:
            time.sleep(random.random())
        if i >= 1_000_000:
            break
    time.sleep(3600)
