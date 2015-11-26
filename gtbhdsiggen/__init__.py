from .timings import TimingsMixin
from .pattern import PatternMixin
from .output_format import OutputFormatMixin
from .exceptions import HDSignalGeneratorException

import serial
import logging

logger = logging.getLogger(__name__)

class HDSignalGenerator(TimingsMixin, PatternMixin, OutputFormatMixin):
    def __init__(self, device):
        if not device:
            raise HDSignalGeneratorException("Invalid serial device: %s" % device)
        self.serial = serial.Serial(device, 19200, 8, 'N', 1, timeout=5)

    def _execute(self, msg, readsize=6):
        """Send msg and waits for response of readsize bytes"""
        self.serial.flushInput()
        logger.debug("[%s] >> %s" % (self.serial.name, msg))
        self.serial.write(msg)
        response = self.serial.read(readsize)
        logger.debug("[%s] << %s" % (self.serial.name, response))
        return response

    def _parsenum(self, msg):
        return int(msg[3:])

    def _formatreq(self, prefix, number):
        return '%.3s%03.3d' % (prefix, number)

    def get_firmware_version(self):
        response = self._execute('VER999')
        return self._parsenum(response)/10.0

