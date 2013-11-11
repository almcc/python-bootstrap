#!/usr/bin/env python

from unittest import TestCase
from mock import patch
import app.common as common


class DummyTests(TestCase):

    @patch('__builtin__.open')
    def test_state(self, mock_open):
        obj = common.Dummy()
        self.assertTrue(obj.getState())

    @patch('__builtin__.open')
    def test_not_off(self, mock_open):
        obj = common.Dummy()
        self.assertFalse(obj.isOff())
