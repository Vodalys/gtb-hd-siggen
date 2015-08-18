from .exceptions import HDSignalGeneratorException

class OutputFormatException(HDSignalGeneratorException):
    pass

class OutputFormatMixin(object):
    def find_format(self, name):
        for key, value in self.OUTPUT_FORMATS.iteritems():
            if value == name:
                return key
        raise OutputFormatException("Output format %s is not supported" % name)

    def get_output_format(self):
        response = self._execute('OUT999')
        index = self._parsenum(response)
        try:
            return self.OUTPUT_FORMATS[index]
        except KeyError as e:
            raise OutputFormatException("Received output format index is unknown", e)

    def set_output_format(self, name):
        index = self.find_format(name)
        req = self._formatreq('OUT', index)
        resp = self._execute(req)
        if req != resp:
            raise OutputFormatException("Failed to set output format")

    OUTPUT_FORMATS = {
        1: "PC",
        2: "HD",
        3: "DVI",
        4: "HDMI"
    }

