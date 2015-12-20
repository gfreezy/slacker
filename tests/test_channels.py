#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import unittest

from mock import patch

from slacker import Channels, Response


class TestUtils(unittest.TestCase):

    @patch('slacker.BaseAPI._request')
    def test_get_channel_id(self, mock_request):
        text = {
            'ok': 'true',
            'channels': [
                {'name': 'general', 'id': 'C111'},
                {'name': 'random', 'id': 'C222'}
            ]
        }
        json_to_text = json.dumps(text)

        mock_request.return_value = Response(
            json_to_text,
        )

        channels = Channels(token='aaa')

        self.assertEqual(
            'C111', channels.get_channel_id('general')
        )

    @patch('slacker.BaseAPI._request')
    def test_get_channel_id_without_channel(self, mock_request):
        text = {
            'ok': 'true',
            'channels': [
                {'name': 'general', 'id': 'C111'},
                {'name': 'random', 'id': 'C222'}
            ]
        }
        json_to_text = json.dumps(text)

        mock_request.return_value = Response(
            json_to_text,
        )

        channels = Channels(token='aaa')

        self.assertEqual(
            None, channels.get_channel_id('fake_group')
        )
