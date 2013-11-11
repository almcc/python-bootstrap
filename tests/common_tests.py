#!/usr/bin/env python

from unittest import TestCase
from mock import patch
import app.common as common


class StandAloneTests(TestCase):

    @patch('__builtin__.open')
    def test_login(self, mock_open):
        obj = common.Dummy()
        self.assertTrue(not obj.doStuff())
