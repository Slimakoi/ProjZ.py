__title__ = 'ProjZ.py'
__author__ = 'Slimakoi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020-2020 Slimakoi'
__version__ = '0.0.6.1'

from .client import Client
from .socket import Callbacks
from .lib.util import device, exceptions, headers, helpers, objects
from requests import get
from json import loads

if __version__ != loads(get("https://pypi.python.org/pypi/ProjZ.py/json").text)["info"]["version"]:
    print(exceptions.LibraryUpdateAvailable)