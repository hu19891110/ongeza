#!/usr/bin/env python
"""
    tests.formatter_tests
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2015 by gregorynicholas.
    :license: MIT, see LICENSE for more details.
"""
from __future__ import unicode_literals
import unittest
from mock import patch, MagicMock
from tests.testcase import BumpTestCase

import bump
from bump import version
from bump.config import BumpConfig
from bump.project import Project


class SummaryFormatterTests(BumpTestCase):
    pass


if __name__ == "__main__":
    unittest.main(exit=False)
