"""
Videoplayer API.
"""

import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def play(video,offset,duration):
    logger.info("play(video=%s,offset=%s,duration=%s)",video,offset,duration)
    time.sleep(duration)