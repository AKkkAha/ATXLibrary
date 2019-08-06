# -*- cofing: utf-8 -*-

import os
from ATXLibrary.keywords import *
from ATXLibrary.version import VERSION

__version__ = VERSION


class ATXLibrary(
    _LoggingKeywords,
    _RunOnFailureKeywords,
    _ElementKeywords,
    _ScreenshotKeywords,
    _ApplicationManagementKeywords,
    _WaitingKeywords,
    _TouchKeywords,
    _KeyeventKeywords,
    _AndroidUtilsKeywords,
):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self, timeout=5, run_on_failure='Capture Page Screenshot'):
        for base in ATXLibrary.__bases__:
            base.__init__(self)
        self.set_atx_timeout(timeout)
        self.register_keyword_to_run_on_failure(run_on_failure)