import argparse
import os
import threading

from nx584 import api
from nx584 import controller

#custom standardized logging
import nx584.log_config
LOG = log_config.LOGGER
LOG.info('starting pynx584 controller')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config.ini',
                        metavar='FILE',
                        help='Path to config file')
    parser.add_argument('--connect', default=None,
                        metavar='HOST:PORT',
                        help='Host and port to connect for serial stream')
    parser.add_argument('--serial', default=None,
                        metavar='PORT',
                        help='Serial port to open for stream')
    parser.add_argument('--baudrate', default=38400, type=int,
                        metavar='BAUD',
                        help='Serial baudrate')
    parser.add_argument('--listen', default='127.0.0.1',
                        metavar='ADDR',
                        help='Listen address (defaults to 127.0.0.1)')
    parser.add_argument('--port', default=5007, type=int,
                        help='Listen port (defaults to 5007)')
    args = parser.parse_args()

    LOG.info('Client Ready')

    if args.connect:
        host, port = args.connect.split(':')
        ctrl = controller.NXController((host, int(port)),
                                       args.config)
    elif args.serial:
        ctrl = controller.NXController((args.serial, args.baudrate),
                                       args.config)
    else:
        LOG.error('Either host:port or serial and baudrate are required')
        return

    api.CONTROLLER = ctrl

    t = threading.Thread(target=ctrl.controller_loop)
    t.daemon = True
    t.start()

    api.app.run(debug=False, host=args.listen, port=args.port, threaded=True)
