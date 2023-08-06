import re

SMPTE_NDF_REGEX = re.compile(r'^(?:-)?(?:(?:(?:(\d\d{1}):){1}([0-5]?\d):){1}([0-5]?\d):){1}(\d?\d\d{1}){1}$')
SMPTE_DF_REGEX = re.compile(r'^(?:-)?(?:(?:(?:(\d\d{1}):){1}([0-5]?\d):){1}([0-5]?\d);){1}(\d?\d\d{1}){1}$')
SMPTE_REGEX = re.compile(r'^(?:-)?(?:(?:(?:(\d\d{1}):){1}([0-5]?\d):){1}([0-5]?\d);?:?){1}(\d?\d\d{1}){1}$')
SRT_REGEX = re.compile(r'^(?:-)?(?:(?:(?:(\d\d{1}):){1}([0-5]?\d):){1}([0-5]?\d),){1}(\d\d\d){1}$')
FFMPEG_REGEX = re.compile(r'^(?:-)?(?:(?:(?:(\d\d{1}):){1}([0-5]?\d):){1}([0-5]?\d)\.){1}(\d?\d+){1}$')
DLP_REGEX = re.compile(r'^(?:-)?(?:(?:(?:(\d\d{1}):){1}([0-5]?\d):){1}([0-5]?\d):){1}([0-2][0-4]\d{1}){1}$')
FCPX_REGEX = re.compile(r'^(?:-)?(\d+)[/]?(\d+)?s$')
FRAME_REGEX = re.compile(r'^(\d+?)f?$')
TIME_REGEX = re.compile(r'^(\d+?(\.{1})\d+?|\d+?)s?$')


