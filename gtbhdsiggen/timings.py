from .exceptions import HDSignalGeneratorException

class TimingsException(HDSignalGeneratorException):
    pass

class TimingsMixin(object):
    def find_timings(self, timings):
        for key, value in self.TIMINGS.iteritems():
            if value == timings:
                return key
        raise TimingsException("Timings %s is not supported" % timings)

    def get_timings(self):
        response = self._execute('TIM999')
        index = self._parsenum(response)
        try:
            return self.TIMINGS[index]
        except KeyError as e:
            raise TimingsException("Received timings index is unknown", e)

    def set_timings(self, timings):
        index = self.find_timings(timings)
        req = self._formatreq('TIM', index)
        resp = self._execute(req)
        if req != resp:
            raise TimingsException("Failed to set timings")

    TIMINGS = {
        1: "640x480@60",
        2: "640x480@72",
        3: "640x480@75",
        4: "640x480@85",
        5: "800x600@56",
        6: "800x600@60",
        7: "800x600@72",
        8: "800x600@75",
        9: "800x600@85",
        10: "1024x768@60",
        11: "1024x768@70",
        12: "1024x768@75",
        13: "1024x768@85",
        14: "1280x960@60",
        15: "1280x960@85",
        16: "1280x1024@60",
        17: "1280x1024@75",
        18: "1280x1024@85",
        19: "1600x1200@60",
        20: "1920x1200@60",
        21: "720x480i@59",
        22: "720x480i@60",
        23: "720x480p@59",
        24: "720x480p@60",
        25: "1280x720p@59",
        26: "1280x720p@60",
        27: "1920x1080i@59",
        28: "1920x1080i@60",
        29: "1920x1080p@59",
        30: "1920x1080p@60",
        31: "720x576i@50",
        32: "720x576p@50",
        33: "1280x720p@50",
        34: "1920x1080i@50",
        35: "1920x1080p@50",
        36: "1920x1080p@23",
        37: "1920x1080p@24",
        38: "1366x768@60",
        39: "1366x768@50"
    }

