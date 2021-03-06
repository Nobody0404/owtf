from __future__ import absolute_import, unicode_literals

import re
from collections import namedtuple as NamedTuple

from owtf.utils.logger import OWTFLogger

__version__ = "2.4.0"
__homepage__ = "https://github.com/owtf/owtf"
__docformat__ = "markdown"


version_info_t = NamedTuple("version_info_t", [
    "major",
    "minor",
    "patch",
])

# bumpversion can only search for {current_version}
# so we have to parse the version here.
_temp = re.match(r"(\d+)\.(\d+).(\d+)(\.(.+))?", __version__).groups()
VERSION = version_info = version_info_t(
    int(_temp[0]), int(_temp[1]), int(_temp[2]))
del _temp

OWTFLogger().enable_logging()
