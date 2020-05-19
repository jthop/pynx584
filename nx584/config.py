import os
import logging
import logging.handlers

__VERSION__ = '0.0.4'
LOG_FORMAT = '%(asctime)-15s %(module)s %(levelname)s %(message)s'
SYSLOG_HANDLER = logging.handlers.SysLogHandler(address = '/dev/log')
SYSLOG_LEVEL = logging.INFO
STREAM_HANDLER = logging.StreamHandler()
STREAM_LEVEL = logging.DEBUG
    
LOGGER = logging.getLogger(__name__)
formatter = logging.Formatter(LOG_FORMAT)

syslog = SYSLOG_HANDLER
syslog.setFormatter(formatter)
syslog.setLevel(SYSLOG_LEVEL)
LOGGER.addHandler(syslog)

istty = os.isatty(0)
if istty:
  stream = STREAM_HANDLER
  stream.setFormatter(formatter)
  stream.setLevel(STREAM_LEVEL)
  LOGGER.addHandler(stream)

  LOGGER.debug(f'Stream ready - pynx584 v{__VERSION__}')

LOGGER.info(f'pynx584 v{__VERSION__} ready')
