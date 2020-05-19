import os
import logging
import logging.handlers

__VERSION__ = '0.0.5'
LOG_FORMAT = '%(asctime)-15s %(module)s %(levelname)s %(message)s'
SYSLOG_HANDLER = logging.handlers.SysLogHandler(address = '/dev/log')
STREAM_HANDLER = logging.StreamHandler()
    
LOGGER = logging.getLogger('pynx584')
LOGGER.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOG_FORMAT)

syslog = SYSLOG_HANDLER
syslog.setFormatter(formatter)
syslog.setLevel(logging.INFO)
LOGGER.addHandler(syslog)

istty = os.isatty(0)
if istty:
  stream = STREAM_HANDLER
  stream.setFormatter(formatter)
  stream.setLevel(logging.DEBUG)
  LOGGER.addHandler(stream)
  LOGGER.debug(f'Stream ready - pynx584 v{__VERSION__}')

LOGGER.info(f'pynx584 v{__VERSION__} ready')
