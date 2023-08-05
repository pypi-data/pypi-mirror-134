# detect test environment and add path for local testing
# this should be the first import in __init__.py
from lib_detect_testenv import *

if is_testenv_active():  # pragma: no cover
    add_path_to_syspath(__file__)

# put Your imports here
from .lib_shopware6_api_base import *
from .lib_shopware6_api_base_criteria import *

# __init__conf__ needs to be imported after Your imports, otherwise we would create circular import on the cli script,
# which is reading some values from __init__conf__
from . import __init__conf__

__title__ = __init__conf__.title
__version__ = __init__conf__.version
__name__ = __init__conf__.name
__url__ = __init__conf__.url
__author__ = __init__conf__.author
__author_email__ = __init__conf__.author_email
__shell_command__ = __init__conf__.shell_command
