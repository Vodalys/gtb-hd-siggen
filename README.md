# gtbhdsiggen
A python lib and tool to control Gefen HD Pattern Signal Generator on Linux

## From python

    >>> from gtbhdsiggen import HDSignalGenerator
    >>> siggen = HDSignalGenerator('/dev/ttyUSB0')
    >>> siggen.get_timings()
    '1280x720p@60'
    >>> siggen.get_pattern()
    'Color Bar'
    >>> siggen.set_timings(35)
    >>> siggen.set_pattern(15)

## From shell

Get timings and pattern:

    $ ./gtbhdsiggen-ctl --get-timings --get-pattern
    Timings: 1920x1080p@50
    Pattern: SMPTE Color Bar

Set timings and pattern:

    $ ./gtbhdsiggen-ctl --set-timings=26 --set-pattern=14
    $ ./gtbhdsiggen-ctl --get-timings --get-pattern
    Timings: 1280x720p@60
    Pattern: Color Bar

Help:

    $ ./gtbhdsiggen-ctl --help
    usage: gtbhdsiggen-ctl [-h] [-v] [--firmware-version] [-d DEVICE] [-t]
                           [-T TIMINGS] [-p] [-P PATTERN]

    A tool to control Gefen HD Pattern Signal Generator

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         display log information
      --firmware-version    return firmware version

    serial:
      -d DEVICE, --device DEVICE
                            serial device to use

    timings:
      1: 640x480@60 2: 640x480@72 3: 640x480@75 4: 640x480@85 5: 800x600@56 6:
      800x600@60 7: 800x600@72 8: 800x600@75 9: 800x600@85 10: 1024x768@60 11:
      1024x768@70 12: 1024x768@75 13: 1024x768@85 14: 1280x960@60 15:
      1280x960@85 16: 1280x1024@60 17: 1280x1024@75 18: 1280x1024@85 19:
      1600x1200@60 20: 1920x1200@60 21: 720x480i@59 22: 720x480i@60 23:
      720x480p@59 24: 720x480p@60 25: 1280x720p@59 26: 1280x720p@60 27:
      1920x1080i@59 28: 1920x1080i@60 29: 1920x1080p@59 30: 1920x1080p@60 31:
      720x576i@50 32: 720x576p@50 33: 1280x720p@50 34: 1920x1080i@50 35:
      1920x1080p@50 36: 1920x1080p@23 37: 1920x1080p@24 38: 1366x768@60 39:
      1366x768@50

      -t, --get-timings     return current timings
      -T TIMINGS, --set-timings TIMINGS
                            set timings

    pattern:
      1: White 2: Blue 3: Red 4: Magenta 5: Green 6: Cyan 7: Yellow 8: Black 9:
      Red Settings 10: Green Settings 11: Blue Settings 12: Gray Settings 13:
      Color Settings 14: Color Bar 15: SMPTE Color Bar 16: Split Bar 17: RGB
      Delay 18: Gray-8 19: Gray-11 20: Gray-32 21: Gray-256 22: H.Gray-11 23: V
      LineONOFF 24: H LineONOFF 25: MULTI-BURST 26: Dual Needle 27: PLUGE-1 28:
      PLUGE-2 29: PLUGE-3 30: PLUGE-4 31: PLUGE-5 32: GRID 33: Cross Hatch 34:
      GRAY-256-R 35: GRAY-256-G 36: GRAY-256-B 37: CIRCLES 38: EDID Analysis 39:
      AUDIO 40: HDCP 41: Motion 42: In Timing 43: In Video 44: In Audio 45:
      SystemSetup

      -p, --get-pattern     return current pattern
      -P PATTERN, --set-pattern PATTERN
                            set pattern
