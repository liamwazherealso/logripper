import os
import random
import sys
import time
import os
import datetime
import logging
import random
import string
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

time_range = [datetime.datetime.now()]
chars=string.ascii_uppercase + string.digits

LIMIT = int(os.environ.get('LOG_LIMIT'))

logga.info("Logripper run of {} logs.".format(LIMIT))
h = ''.join(random.choice(chars) for x in range(8))
for i in range(LIMIT):
    logga.info("TEST LOG %s", h)
    if i % 1000 == 0:
        time.sleep(random.random())

time_range.append([datetime.datetime.now()])