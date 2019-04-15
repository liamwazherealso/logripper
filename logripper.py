import time
import logging
from itertools import count

logga = logging.getLogger("__name__")
logging.basicConfig(level=logging.INFO)


while True:
    for i in count():
        logga.info("Up up up! %s", i)
        if i > 1_000_000:
            break
    time.sleep(3600)
