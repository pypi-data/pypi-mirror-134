from .version import get_version

VERSION = (0, 1, 1, 'alpha', 1)

__version__ = get_version(VERSION)

from . import expressions  # NOQA
