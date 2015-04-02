from .exceptions import HDSignalGeneratorException

class PatternException(HDSignalGeneratorException):
    pass

class PatternMixin(object):
    def get_pattern(self):
        response = self._execute('PAT999')
        index = self._parsenum(response)
        try:
            return self.PATTERNS[index]
        except KeyError as e:
            raise PatternException("Received pattern index is unknown", e)

    def set_pattern(self, index):
        #FIXME Check index?
        req = self._formatreq('PAT', index)
        resp = self._execute(req)
        if req != resp:
            raise PatternException("Failed to set pattern")

    PATTERNS = {
        1: "White",
        2: "Blue",
        3: "Red",
        4: "Magenta",
        5: "Green",
        6: "Cyan",
        7: "Yellow",
        8: "Black",
        9: "Red Settings",
        10: "Green Settings",
        11: "Blue Settings",
        12: "Gray Settings",
        13: "Color Settings",
        14: "Color Bar",
        15: "SMPTE Color Bar",
        16: "Split Bar",
        17: "RGB Delay",
        18: "Gray-8",
        19: "Gray-11",
        20: "Gray-32",
        21: "Gray-256",
        22: "H.Gray-11",
        23: "V LineONOFF",
        24: "H LineONOFF",
        25: "MULTI-BURST",
        26: "Dual Needle",
        27: "PLUGE-1",
        28: "PLUGE-2",
        29: "PLUGE-3",
        30: "PLUGE-4",
        31: "PLUGE-5",
        32: "GRID",
        33: "Cross Hatch",
        34: "GRAY-256-R",
        35: "GRAY-256-G",
        36: "GRAY-256-B",
        37: "CIRCLES",
        38: "EDID Analysis",
        39: "AUDIO",
        40: "HDCP",
        41: "Motion",
        42: "In Timing",
        43: "In Video",
        44: "In Audio",
        45: "SystemSetup"
    }

