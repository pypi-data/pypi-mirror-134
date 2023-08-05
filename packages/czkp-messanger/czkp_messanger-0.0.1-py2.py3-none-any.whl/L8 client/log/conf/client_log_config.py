"""
This module for logging settings client.py module.

Variables
---------
path
    Path to the log file.
logger
    Declaration logger 'chat.client'.
formatter
    Set format for log string.
handler
    Declaration sending logging output to a disk file.
handler.setFormatter(formatter)
    Set ``formatter`` for a format logger settings.
logger.setLevel(LOG_LVL)
    Set logging level for a ``logger``.
logger.addHandler(handler)
    Set ``handler`` for a ``logger``.
"""

import logging
import os
import sys

from common.settings import LOG_LVL

path = os.path.abspath(os.path.join(__file__, '../..'))
path = os.path.join(path, 'logs/client.log')
logger = logging.getLogger('chat.client')
formatter = logging.Formatter('%(asctime)-25s %(levelname)-10s %(module)-15s %(message)s')
handler = logging.FileHandler(path, encoding='utf-8')
handler.setFormatter(formatter)
logger.setLevel(LOG_LVL)
logger.addHandler(handler)

if __name__ == '__main__':
    stream = logging.StreamHandler(sys.stderr)
    stream.setLevel(logging.DEBUG)
    stream.setFormatter(formatter)
    logger.addHandler(stream)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
