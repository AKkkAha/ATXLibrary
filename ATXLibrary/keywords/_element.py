# -*- coding: utf-8 -*-

from ATXLibrary.locators import ElementFinder
from .keywordgroup import KeywordGroup
from robot.libraries.BuiltIn import BuiltIn
import ast
from unicodedata import normalize
from uiautomator2 import UIAutomatorServer

try:
    basestring  # attempt to evaluate basestring


    def isstr(s):
        return isinstance(s, basestring)
except NameError:
    def isstr(s):
        return isinstance(s, str)


class _ElementKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()
        self._bi = BuiltIn()

    def clear_ext(self, locator):
        """Clears the text field identified by `locator`.

        See `introduction` for details about locating elements.
        """
        self._info("Clear text field '%s'" % locator)
        self.clear_text(locator)