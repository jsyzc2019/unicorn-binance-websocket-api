#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unittest_binance_websocket_api.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://www.lucit.tech/unicorn-binance-websocket-api.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api
# Documentation: https://unicorn-binance-websocket-api.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2023, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
from unicorn_binance_websocket_api.restserver import BinanceWebSocketApiRestServer
from unicorn_binance_websocket_api.restclient import BinanceWebSocketApiRestclient
import logging
import unittest
import os
import time
import threading

import tracemalloc
tracemalloc.start(25)

BINANCE_COM_API_KEY = ""
BINANCE_COM_API_SECRET = ""

logging.getLogger("unicorn_binance_websocket_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

print(f"Starting unittests!")


class TestBinanceComManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\r\nTestBinanceComManager:")
        cls.ubwa = BinanceWebSocketApiManager(exchange="binance.us",
                                              disable_colorama=True,
                                              debug=True)
        cls.binance_com_api_key = BINANCE_COM_API_KEY
        cls.binance_com_api_secret = BINANCE_COM_API_SECRET

    @classmethod
    def tearDownClass(cls):
        cls.ubwa.stop_monitoring_api()
        cls.ubwa.stop_manager()
        print(f"\r\nTestBinanceComManager threads:")
        for thread in threading.enumerate():
            print(thread.name)
        print(f"TestBinanceComManager stopping:")

    def test_create_uri_miniticker_regular_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["!miniTicker"], ["arr"]),
                         'wss://stream.binance.us:9443/ws/!miniTicker@arr')

    def test_create_uri_miniticker_reverse_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["arr"], ["!miniTicker"]),
                         'wss://stream.binance.us:9443/ws/!miniTicker@arr')

    def test_create_uri_ticker_regular_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["!ticker"], ["arr"]),
                         'wss://stream.binance.us:9443/ws/!ticker@arr')

    def test_create_uri_ticker_reverse_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["arr"], ["!ticker"]),
                         'wss://stream.binance.us:9443/ws/!ticker@arr')

    def test_create_uri_userdata_regular_false_com(self):
        self.assertFalse(self.__class__.ubwa.create_websocket_uri(["!userData"], ["arr"]))

    def test_create_uri_userdata_reverse_false_com(self):
        self.assertFalse(self.__class__.ubwa.create_websocket_uri(["arr"], ["!userData"]))

    def test_create_uri_userdata_regular_com(self):
        if len(self.binance_com_api_key) == 0 or len(self.binance_com_api_secret) == 0:
            print("\r\nempty API key and/or secret: can not successfully test test_create_uri_userdata_regular_com() "
                  "for binance.com")
        else:
            stream_id = self.ubwa.get_new_uuid_id()
            self.__class__.ubwa._add_socket_to_socket_list(stream_id, ["!userData"], ["arr"])
            self.assertRegex(self.__class__.ubwa.create_websocket_uri(["!userData"], ["arr"],
                                                                      stream_id,
                                                                      self.binance_com_api_key,
                                                                      self.binance_com_api_secret),
                             r'wss://stream.binance.com:9443/ws/.')

    def test_create_uri_userdata_reverse_com(self):
        if len(self.binance_com_api_key) == 0 or len(self.binance_com_api_secret) == 0:
            print("\r\nempty API key and/or secret: can not successfully test test_create_uri_userdata_reverse_com() "
                  "for binance.com")
        else:
            self.stream_id = self.__class__.ubwa.get_new_uuid_id()
            self.__class__.ubwa._add_socket_to_socket_list(self.stream_id, ["arr"], ["!userData"])
            self.assertRegex(self.__class__.ubwa.create_websocket_uri(["arr"], ["!userData"],
                                                                      self.stream_id,
                                                                      self.binance_com_api_key,
                                                                      self.binance_com_api_secret),
                             'wss://stream.binance.com:9443/ws/.')

    def test_is_exchange_type_cex(self):
        self.assertEqual(self.__class__.ubwa.is_exchange_type("cex"), True)

    def test_is_exchange_type_dex(self):
        self.assertEqual(self.__class__.ubwa.is_exchange_type("dex"), False)

    def test_is_update_available(self):
        result = self.__class__.ubwa.is_update_available()
        is_valid_result = result is True or result is False
        self.assertTrue(is_valid_result, False)

    def test_is_manager_stopping(self):
        self.assertEqual(self.__class__.ubwa.is_manager_stopping(), False)

    def test_get_human_uptime(self):
        self.assertEqual(self.__class__.ubwa.get_human_uptime(60 * 60 * 60 * 61), "152d:12h:0m:0s")
        self.assertEqual(self.__class__.ubwa.get_human_uptime(60 * 60 * 24), "24h:0m:0s")
        self.assertEqual(self.__class__.ubwa.get_human_uptime(60 * 60), "60m:0s")
        self.assertEqual(self.__class__.ubwa.get_human_uptime(60), "60 seconds")

    def test_get_human_bytesize(self):
        self.assertEqual(self.__class__.ubwa.get_human_bytesize(1024 * 1024 * 1024 * 1024 * 1024), "1024.0 tB")
        self.assertEqual(self.__class__.ubwa.get_human_bytesize(1024 * 1024 * 1024 * 1024), "1024.0 gB")
        self.assertEqual(self.__class__.ubwa.get_human_bytesize(1024 * 1024 * 1024), "1024.0 mB")
        self.assertEqual(self.__class__.ubwa.get_human_bytesize(1024 * 1024), "1024.0 kB")
        self.assertEqual(self.__class__.ubwa.get_human_bytesize(1024), "1024 B")
        self.assertEqual(self.__class__.ubwa.get_human_bytesize(1), "1 B")

    def test_get_exchange(self):
        self.assertEqual(self.__class__.ubwa.get_exchange(), "binance.us")

    def test_get_listenkey_from_restclient(self):
        self.assertEqual(self.__class__.ubwa.get_listen_key_from_restclient("ID"), False)

    def test_delete_listen_key_by_stream_id(self):
        stream_id = self.__class__.ubwa.get_new_uuid_id()
        self.assertEqual(self.__class__.ubwa.delete_listen_key_by_stream_id(stream_id), False)

    def test_create_payload_subscribe(self):
        result = "[{'method': 'SUBSCRIBE', 'params': ['bnbbtc@kline_1m'], 'id': 1}]"
        stream_id = self.__class__.ubwa.get_new_uuid_id()
        self.assertEqual(str(self.__class__.ubwa.create_payload(stream_id, "subscribe",
                                                                ['kline_1m'], ['bnbbtc'])), result)

    def test_fill_up_space_centered(self):
        result = "==========test text=========="
        self.assertEqual(str(self.__class__.ubwa.fill_up_space_centered(30, "test text", "=")),
                         result)

    def test_fill_up_space_right(self):
        result = "|test text||||||||||||||||||||"
        self.assertEqual(str(self.__class__.ubwa.fill_up_space_right(30, "test text", "|")),
                         result)

    def test_fill_up_space_left(self):
        result = "||||||||||||||||||||test text|"
        self.assertEqual(str(self.__class__.ubwa.fill_up_space_left(30, "test text", "|")),
                         result)

# Todo:
#    def test_create_stream_userdata(self):
#        self.assertTrue(bool(self.__class__.ubwa.create_stream('arr', '!userData', stream_label="userDataBad",
#                                                               api_key="key", api_secret="secret")))

    def test_create_stream(self):
        self.assertTrue(bool(self.__class__.ubwa.create_stream(markets=['bnbbtc'], channels="trade",
                                                               stream_label="test_stream")))
        stream_id = self.__class__.ubwa.get_stream_id_by_label("test_stream")
        time.sleep(5)
        self.__class__.ubwa.unsubscribe_from_stream(stream_id, markets=['bnbbtc'])
        self.__class__.ubwa.unsubscribe_from_stream(stream_id, channels=['trade'])
        time.sleep(6)
        self.assertTrue(self.__class__.ubwa.set_restart_request(stream_id))
        self.__class__.ubwa.get_monitoring_status_icinga()
        self.__class__.ubwa.print_summary(title="Unittests")
        self.__class__.ubwa.print_stream_info(stream_id, title="Unittests")

    def test_restart_stream(self):
        self.assertFalse(bool(self.__class__.ubwa._restart_stream(self.__class__.ubwa.get_new_uuid_id())))

    def test_start_monitoring_api(self):
        with BinanceWebSocketApiManager(exchange="binance.com-testnet",
                                        high_performance=True,
                                        debug=True,) as ubwa:
            self.assertTrue(ubwa.start_monitoring_api())
            time.sleep(6)
            self.assertTrue(ubwa.stop_monitoring_api())


class TestBinanceComManagerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\r\nTestBinanceComManagerTest:")
        cls.ubwa = BinanceWebSocketApiManager(exchange="binance.com-testnet",
                                              high_performance=True,
                                              debug=True)
        cls.binance_com_testnet_api_key = BINANCE_COM_API_KEY
        cls.binance_com_testnet_api_secret = BINANCE_COM_API_SECRET

    @classmethod
    def tearDownClass(cls):
        cls.ubwa.stop_manager()
        print(f"\r\nTestBinanceComManagerTest threads:")
        for thread in threading.enumerate():
            print(thread.name)
        print(f"TestBinanceComManagerTest stopping:")

    def test_create_uri_miniticker_regular_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["!miniTicker"], ["arr"]),
                         'wss://testnet.binance.vision/ws/!miniTicker@arr')

    def test_create_uri_miniticker_reverse_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["arr"], ["!miniTicker"]),
                         'wss://testnet.binance.vision/ws/!miniTicker@arr')

    def test_create_uri_ticker_regular_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["!ticker"], ["arr"]),
                         'wss://testnet.binance.vision/ws/!ticker@arr')

    def test_create_uri_ticker_reverse_com(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["arr"], ["!ticker"]),
                         'wss://testnet.binance.vision/ws/!ticker@arr')

    def test_create_uri_userdata_regular_false_com(self):
        self.assertFalse(self.__class__.ubwa.create_websocket_uri(["!userData"], ["arr"]))

    def test_create_uri_userdata_reverse_false_com(self):
        self.assertFalse(self.__class__.ubwa.create_websocket_uri(["arr"], ["!userData"]))

    def test_create_uri_userdata_regular_com(self):
        if (len(self.__class__.binance_com_testnet_api_key) == 0 or
                len(self.__class__.binance_com_testnet_api_secret) == 0):
            print("\r\nempty API key and/or secret: can not successfully test test_create_uri_userdata_regular_com() "
                  "for binance.com-testnet")
        else:
            stream_id = self.__class__.ubwa.get_new_uuid_id()
            self.__class__.ubwa._add_socket_to_socket_list(stream_id, ["!userData"], ["arr"])
            self.assertRegex(self.__class__.ubwa.create_websocket_uri(["!userData"], ["arr"],
                                                                      stream_id,
                                                                      self.__class__.binance_com_testnet_api_key,
                                                                      self.__class__.binance_com_testnet_api_secret),
                             r'wss://testnet.binance.vision/ws/.')

    def test_create_uri_userdata_reverse_com(self):
        if (len(self.__class__.binance_com_testnet_api_key) == 0 or
                len(self.__class__.binance_com_testnet_api_secret) == 0):
            print("\r\nempty API key and/or secret: can not successfully test test_create_uri_userdata_reverse_com() "
                  "for binance.com-testnet")
        else:
            stream_id = self.__class__.ubwa.get_new_uuid_id()
            self.__class__.ubwa._add_socket_to_socket_list(stream_id, ["arr"], ["!userData"])
            self.assertRegex(self.__class__.ubwa.create_websocket_uri(["arr"], ["!userData"],
                                                                      stream_id,
                                                                      self.binance_com_testnet_api_key,
                                                                      self.binance_com_testnet_api_secret),
                             r'wss://stream.binance.com:9443/ws/.')

    def test_is_exchange_type_cex(self):
        self.assertEqual(self.__class__.ubwa.is_exchange_type("cex"), True)

    def test_is_exchange_type_dex(self):
        self.assertEqual(self.__class__.ubwa.is_exchange_type("dex"), False)

    def test_stop_manager(self):
        time.sleep(6)
        self.__class__.ubwa.stop_manager()


class TestBinanceOrgManagerTestnet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\r\nTestBinanceOrgManagerTestnet:")
        cls.ubwa = BinanceWebSocketApiManager(exchange="binance.org-testnet",
                                              debug=True,
                                              high_performance=True)
        cls.binance_com_api_key = BINANCE_COM_API_KEY
        cls.binance_com_api_secret = BINANCE_COM_API_SECRET

    @classmethod
    def tearDownClass(cls):
        cls.ubwa.stop_manager()
        print(f"\r\nTestBinanceOrgManagerTestnet threads:")
        for thread in threading.enumerate():
            print(thread.name)
        print(f"TestBinanceOrgManagerTestnet stopping:")

    def test_testnet(self):
        stream_id = self.__class__.ubwa.create_stream(['orders', 'transfers', 'accounts'],
                                                      "tbnb1unxhf8fat985ksajatfa5jea58j2kzg7mfy0e7")
        time.sleep(6)
        self.__class__.ubwa.unsubscribe_from_stream(stream_id, "tbnb1unxhf8fat985ksajatfa5jea58j2kzg7mfy0e7")

    def test_stop_manager(self):
        self.__class__.ubwa.stop_manager()


class TestBinanceOrgManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\r\nTestBinanceOrgManager:")
        cls.ubwa = BinanceWebSocketApiManager(exchange="binance.org",
                                              debug=True,
                                              high_performance=True)
        cls.binance_com_api_key = BINANCE_COM_API_KEY
        cls.binance_com_api_secret = BINANCE_COM_API_SECRET

    @classmethod
    def tearDownClass(cls):
        cls.ubwa.stop_manager()
        print(f"\r\nTestBinanceOrgManager threads:")
        for thread in threading.enumerate():
            print(thread.name)
        print(f"TestBinanceOrgManager stopping:")

    def test_create_uri_alltickers_regular_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["$all"], ["allTickers"]),
                         'wss://dex.binance.org/api/ws/$all@allTickers')

    def test_create_uri_alltickers_reverse_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["allTickers"], ["$all"]),
                         'wss://dex.binance.org/api/ws/$all@allTickers')

    def test_create_uri_allminitickers_regular_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["$all"], ["allMiniTickers"]),
                         'wss://dex.binance.org/api/ws/$all@allMiniTickers')

    def test_create_uri_allminitickers_reverse_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["allMiniTickers"], ["$all"]),
                         'wss://dex.binance.org/api/ws/$all@allMiniTickers')

    def test_create_uri_blockheight_regular_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["$all"], ["blockheight"]),
                         'wss://dex.binance.org/api/ws/$all@blockheight')

    def test_create_uri_blockheight_reverse_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["blockheight"], ["$all"]),
                         'wss://dex.binance.org/api/ws/$all@blockheight')

    def test_create_uri_single_trades_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["trades"], ["RAVEN-F66_BNB"]),
                         'wss://dex.binance.org/api/ws/RAVEN-F66_BNB@trades')

    def test_create_uri_single_marketdepth_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["marketDepth"], ["RAVEN-F66_BNB"]),
                         'wss://dex.binance.org/api/ws/RAVEN-F66_BNB@marketDepth')

    def test_create_uri_single_kline_1h_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["kline_1h"], ["RAVEN-F66_BNB"]),
                         'wss://dex.binance.org/api/ws/RAVEN-F66_BNB@kline_1h')

    def test_create_uri_single_ticker_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["ticker"], ["RAVEN-F66_BNB"]),
                         'wss://dex.binance.org/api/ws/RAVEN-F66_BNB@ticker')

    def test_create_uri_single_miniTicker_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(["miniTicker"], ["RAVEN-F66_BNB"]),
                         'wss://dex.binance.org/api/ws/RAVEN-F66_BNB@miniTicker')

    def test_create_uri_multi_org_subscribe(self):
        self.assertEqual(self.__class__.ubwa.create_websocket_uri(['trades', 'kline_1h'],
                                                                  ['RAVEN-F66_BNB', 'ANKR-E97_BNB']),
                         'wss://dex.binance.org/api/ws')

        stream_id = self.__class__.ubwa.create_stream(['trades', 'kline_1h'],
                                                      ['RAVEN-F66_BNB', 'ANKR-E97_BNB'])
        payload = self.__class__.ubwa.create_payload(stream_id, "subscribe", ['trades', 'kline_1h'],
                                                     ['RAVEN-F66_BNB', 'ANKR-E97_BNB'])
        self.assertEqual(str(payload),
                         "[{'method': 'subscribe', 'topic': 'trades', 'symbols': ['RAVEN-F66_BNB', 'ANKR-E97_BNB']}, "
                         "{'method': 'subscribe', 'topic': 'kline_1h', 'symbols': ['RAVEN-F66_BNB', 'ANKR-E97_BNB']}]")

    def test_create_uri_user_address_orders_single_org_subscribe(self):
        self.assertEqual(
            self.__class__.ubwa.create_websocket_uri('orders',
                                                     'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6'),
            'wss://dex.binance.org/api/ws/bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6')

    def test_create_uri_user_address_accounts_single_org_subscribe(self):
        self.assertEqual(
            self.__class__.ubwa.create_websocket_uri('accounts',
                                                     'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6'),
            'wss://dex.binance.org/api/ws/bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6')

    def test_create_uri_user_address_transfers_single_org_subscribe(self):
        self.assertEqual(
            self.__class__.ubwa.create_websocket_uri('transfers',
                                                     'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6'),
            'wss://dex.binance.org/api/ws/bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6')

    def test_create_uri_user_address_multi_org_subscribe(self):
        stream_id = self.__class__.ubwa.create_stream(['orders', 'transfers', 'accounts'],
                                                      'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6')
        payload = self.__class__.ubwa.create_payload(stream_id, 'subscribe',
                                                     ['orders', 'transfers', 'accounts'],
                                                     'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6')
        self.assertEqual(str(payload),
                         "[{'method': 'subscribe', 'topic': 'orders', "
                         "'address': 'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6'}, "
                         "{'method': 'subscribe', 'topic': 'transfers', "
                         "'address': 'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6'}, "
                         "{'method': 'subscribe', 'topic': 'accounts', "
                         "'address': 'bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6'}]")

    def test_create_misc_single_org_subscribe(self):
        stream_id = self.__class__.ubwa.create_stream(["trades"], ["RAVEN-F66_BNB"])
        payload = self.__class__.ubwa.create_payload(stream_id, 'subscribe', ['trades'], 'RAVEN-F66_BNB')
        self.assertEqual(str(payload),
                         "[{'method': 'subscribe', 'topic': 'trades', 'symbols': ['RAVEN-F66_BNB']}]")

    def test_create_misc_multi_org_subscribe(self):
        stream_id = self.__class__.ubwa.create_stream(["trades", 'kline_1m'], ["RAVEN-F66_BNB", "ANKR-E97_BNB"])
        payload = self.__class__.ubwa.create_payload(stream_id, 'subscribe',
                                                     ["trades", 'kline_1m'],
                                                     ["RAVEN-F66_BNB", "ANKR-E97_BNB"])
        self.assertEqual(str(payload),
                         "[{'method': 'subscribe', 'topic': 'trades', 'symbols': ['RAVEN-F66_BNB', 'ANKR-E97_BNB']}, "
                         "{'method': 'subscribe', 'topic': 'kline_1m', 'symbols': ['RAVEN-F66_BNB', 'ANKR-E97_BNB']}]")

    def test_create_misc_multi_org_unsubscribe(self):
        stream_id = self.__class__.ubwa.create_stream(["trades", 'kline_1m'], ["RAVEN-F66_BNB", "ANKR-E97_BNB"])
        payload = self.__class__.ubwa.create_payload(stream_id, 'unsubscribe',
                                                     ["trades", 'kline_1m'],
                                                     ["RAVEN-F66_BNB", "ANKR-E97_BNB"])
        self.assertEqual(str(payload),
                         "[{'method': 'unsubscribe', 'symbols': ['RAVEN-F66_BNB', 'ANKR-E97_BNB']}, "
                         "{'method': 'unsubscribe', 'topic': 'trades'}, "
                         "{'method': 'unsubscribe', 'topic': 'kline_1m'}]")

    def test_create_misc_single_org_unsubscribe(self):
        stream_id = self.__class__.ubwa.create_stream(["trades"], ["RAVEN-F66_BNB"])
        payload = self.__class__.ubwa.create_payload(stream_id, 'unsubscribe', ["trades"], ["RAVEN-F66_BNB"])
        self.assertEqual(str(payload),
                         "[{'method': 'unsubscribe', 'symbols': ['RAVEN-F66_BNB']}, "
                         "{'method': 'unsubscribe', 'topic': 'trades'}]")

    def test_is_exchange_type_cex(self):
        self.assertEqual(self.__class__.ubwa.is_exchange_type("cex"), False)

    def test_is_exchange_type_dex(self):
        self.assertEqual(self.__class__.ubwa.is_exchange_type("dex"), True)

    def test_create_payload(self):
        result = "[{'method': 'subscribe', 'topic': 'kline_1m', 'symbols': ['RAVEN-F66_BNB']}]"
        stream_id = self.__class__.ubwa.get_new_uuid_id()
        self.assertEqual(str(self.__class__.ubwa.create_payload(stream_id,
                                                                "subscribe",
                                                                ['kline_1m'],
                                                                ['RAVEN-F66_BNB'])),
                         result)

    def test_stop_manager(self):
        self.__class__.ubwa.stop_manager()


class TestApiLive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"\r\nTestApiLive:")
        cls.ubwa = BinanceWebSocketApiManager(exchange="binance.us",
                                              debug=True,
                                              enable_stream_signal_buffer=True,
                                              high_performance=True)

    @classmethod
    def tearDownClass(cls):
        cls.ubwa.stop_manager()
        print(f"\r\nTestApiLive threads:")
        for thread in threading.enumerate():
            print(thread.name)
        print(f"TestApiLive stopping:")

    def test_get_new_uuid_id(self):
        self.__class__.ubwa.get_new_uuid_id()

    def test_rest_binance_com(self):
        BinanceWebSocketApiRestclient(self.__class__.ubwa)

    def test_rest_binance_com_isolated_margin(self):
        self.__class__.ubwa = BinanceWebSocketApiManager(exchange="binance.com-isolated_margin",
                                                         high_performance=True)
        BinanceWebSocketApiRestclient(self.__class__.ubwa)
        self.__class__.ubwa.stop_manager()

    def test_rest_binance_com_isolated_margin_testnet(self):
        self.__class__.ubwa = BinanceWebSocketApiManager(exchange="binance.com-isolated_margin-testnet",
                                                         high_performance=True)
        BinanceWebSocketApiRestclient(self.__class__.ubwa)
        self.__class__.ubwa.stop_manager()

    def test_invalid_exchange(self):
        from unicorn_binance_websocket_api.exceptions import UnknownExchange
        try:
            ubwa = BinanceWebSocketApiManager(exchange="invalid-exchange.com", high_performance=True)
            ubwa.stop_manager()
        except UnknownExchange:
            pass

# Todo: Needs a proxy ...
#    def test_isolated_margin(self):
#        self.__class__.ubwa = BinanceWebSocketApiManager(exchange="binance.com-isolated_margin", high_performance=True)
#        stream_id = self.__class__.ubwa.create_stream('arr', '!userData', symbols="CELRBTC",
#                                                      api_key="key", api_secret="secret")
#        time.sleep(10)
#        print("\r\n")
#        self.__class__.ubwa.print_stream_info(stream_id)
#        self.__class__.ubwa.stop_manager()

    def test_live_run(self):
        self.__class__.ubwa.get_active_stream_list()
        self.__class__.ubwa.get_limit_of_subscriptions_per_stream()
        self.__class__.ubwa.get_stream_list()

        markets = ['xrpbearbusd', 'zeceth', 'cndbtc', 'dashbtc', 'atompax', 'perlbtc', 'ardreth', 'zecbnb',
                   'bchabctusd',
                   'usdsbusdt', 'winbnb', 'xzcxrp', 'bchusdc', 'wavesbnb', 'kavausdt', 'btsusdt', 'chzbnb', 'tusdbnb',
                   'xtzbusd', 'bcptusdc', 'dogebnb', 'eosbearusdt', 'ambbnb', 'wrxbnb', 'poabtc', 'wanbtc', 'ardrbtc',
                   'icnbtc',
                   'tusdusdt', 'atombusd', 'nxseth', 'bnbusdt', 'trxxrp', 'erdpax', 'erdbtc', 'icxbusd', 'nulsbtc',
                   'hotusdt',
                   'wavespax', 'zilbnb', 'arnbtc', 'nulsusdt', 'wintrx', 'npxsbtc', 'busdtry', 'qtumbnb', 'eosbtc',
                   'xlmpax',
                   'tomobnb', 'eosbnb', 'engbtc', 'linketh', 'xrpbtc', 'fetbtc', 'stratusdt', 'navbnb', 'bcneth',
                   'yoyobtc',
                   'nanobnb', 'saltbtc', 'tfuelusdc', 'skybnb', 'fuelbtc', 'bnbusdc', 'inseth', 'btcpax', 'batbtc',
                   'rlceth',
                   'arketh', 'ltcpax', 'ltcbusd', 'duskbtc', 'mftusdt', 'bntusdt', 'mdabtc', 'enjbtc', 'poabnb',
                   'nanobusd',
                   'paxtusd', 'hotbtc', 'bcdbtc', 'beambnb', 'trxeth', 'omgbnb', 'cdtbtc', 'eosusdc', 'dashbusd',
                   'cocosbtc',
                   'dasheth', 'xrptusd', 'atomtusd', 'rcneth', 'rpxeth', 'xlmusdc', 'aionbusd', 'nxsbtc', 'chateth',
                   'repbtc',
                   'tctusdt', 'linkusdt', 'nasbtc', 'usdsusdc', 'xvgbtc', 'elfeth', 'ctxcbtc', 'cmteth', 'gnteth',
                   'usdspax',
                   'zilbtc', 'batpax', 'stratbtc', 'xzcbtc', 'iotausdt', 'etcbnb', 'ankrusdt', 'xlmeth', 'loombtc',
                   'erdusdc',
                   'rdnbnb', 'icneth', 'vetbtc', 'cvcusdt', 'ftmpax', 'ethbullusdt', 'edoeth', 'steemeth', 'gobnb',
                   'hsrbtc',
                   'ambbtc', 'bchabcbtc', 'dntbtc', 'btctusd', 'denteth', 'snglsbtc', 'eosbullusdt', 'xlmtusd',
                   'tnteth',
                   'sysbnb', 'renusdt', 'zrxusdt', 'xlmbtc', 'stormbtc', 'ncashbnb', 'omgusdt', 'troyusdt', 'venbtc',
                   'modbtc',
                   'dogepax', 'ontusdc', 'eurbusd', 'tctbnb', 'gxsbtc', 'celrbnb', 'adausdt', 'beambtc', 'elfbtc',
                   'celrbtc',
                   'rvnusdt', 'poaeth', 'wavesusdc', 'trxbnb', 'trxusdc', 'ethbearusdt', 'ethpax', 'bateth', 'kavabtc',
                   'paxbtc', 'trigbnb', 'btcusdc', 'oneusdc', 'xrptry', 'stxusdt', 'strateth', 'lendeth', 'neousdc',
                   'mithusdt', 'btcngn', 'blzeth', 'evxeth', 'dnteth', 'grsbtc', 'arneth', 'iotabnb', 'waneth',
                   'xtzbnb',
                   'subeth', 'btsbtc', 'cvceth', 'ethusdc', 'etctusd', 'cloakbtc', 'grseth', 'eospax', 'cdteth',
                   'bchusdt',
                   'lskusdt', 'enjbusd', 'drepbtc', 'manaeth', 'tomousdt', 'algobnb', 'wtceth', 'linkpax', 'batbnb',
                   'sceth',
                   'rvnbusd', 'cvcbnb', 'manabtc', 'gasbtc', 'stxbtc', 'cloaketh', 'neotusd', 'lrceth', 'thetabtc',
                   'dogeusdt',
                   'aionbnb', 'viabtc', 'keyeth', 'nanoeth', 'ncasheth', 'bgbpusdc', 'ltobnb', 'snmeth', 'adabtc',
                   'btseth',
                   'qtumbusd', 'wtcbnb', 'dcrbtc', 'fttbnb', 'paxbnb', 'insbtc', 'gntbnb', 'etheur', 'dashusdt',
                   'rcnbtc',
                   'btcusdt', 'wanusdt', 'powrbnb', 'xmrbnb', 'trigeth', 'xzceth', 'bchbtc', 'qspbnb', 'scbnb',
                   'mcoeth',
                   'powrbtc', 'algotusd', 'ankrbtc', 'tusdeth', 'keybtc', 'usdcusdt', 'ftmusdc', 'atombnb', 'zenbtc',
                   'dockbtc',
                   'neobtc', 'phbbnb', 'bnbpax', 'brdbnb', 'trxusdt', 'trxbusd', 'mtlbtc', 'ftmtusd', 'perlusdc',
                   'mithbnb',
                   'eosbullbusd', 'reqeth', 'bccbnb', 'veneth', 'loombnb', 'trxpax', 'usdcpax', 'stormusdt', 'ognbtc',
                   'gvtbtc',
                   'iotaeth', 'naseth', 'drepusdt', 'gvteth', 'wrxusdt', 'bchabcpax', 'ongbtc', 'usdcbnb', 'dgdeth',
                   'salteth',
                   'mtleth', 'bcnbnb', 'neblbnb', 'wanbnb', 'ontusdt', 'npxsusdt', 'mftbtc', 'eosbearbusd', 'bntbtc',
                   'gtoeth',
                   'modeth', 'etcusdc', 'veteth', 'bcptpax', 'atomusdc', 'duskpax', 'kavabnb', 'lunbtc', 'adxbtc',
                   'bnteth',
                   'funbtc', 'knceth', 'dogebtc', 'bchsvpax', 'bcpttusd', 'osteth', 'oaxeth', 'wabibtc', 'appcbtc',
                   'qkcbtc',
                   'nanousdt', 'wingsbtc', 'hbarusdt', 'eurusdt', 'waveseth', 'asteth', 'linkbusd', 'btttusd',
                   'zecusdc',
                   'bnbusds', 'linkbtc', 'venusdt', 'hotbnb', 'usdtrub', 'tctbtc', 'ankrpax', 'btctry', 'adabnb',
                   'polybtc',
                   'bcceth', 'enjeth', 'bnbbusd', 'repbnb', 'bullusdt', 'vitebtc', 'btgbtc', 'renbtc', 'thetausdt',
                   'troybtc',
                   'dentbtc', 'ostbtc', 'nxsbnb', 'mithbtc', 'xmrbtc', 'tomobtc', 'nulseth', 'phbbtc', 'duskbnb',
                   'yoyoeth',
                   'ontbusd', 'btgeth', 'etcusdt', 'atomusdt', 'hcbtc', 'brdbtc', 'fttbtc', 'celrusdt', 'lskbnb',
                   'phbpax',
                   'xtzbtc', 'batusdt', 'viteusdt', 'trxbtc', 'bchtusd', 'xtzusdt', 'ftmbtc', 'enjbnb', 'arkbtc',
                   'wavesusdt',
                   'ftmusdt', 'neobusd', 'stormbnb', 'luneth', 'gntbtc', 'gtousdt', 'chzusdt', 'sntbtc', 'bandbnb',
                   'hoteth',
                   'wingseth', 'mcobtc', 'docketh', 'drepbnb', 'eosusdt', 'eostusd', 'npxseth', 'thetaeth', 'iotxbtc',
                   'phxbnb',
                   'enjusdt', 'tfuelbnb', 'mcobnb', 'ontpax', 'dcrbnb', 'batusdc', 'snglseth', 'qlcbtc', 'qspeth',
                   'cndeth',
                   'appcbnb', 'wprbtc', 'sysbtc', 'iostusdt', 'btceur', 'mtlusdt', 'ethrub', 'tfuelpax', 'maticusdt',
                   'ftmbnb',
                   'xrpbusd', 'iotxusdt', 'tusdbtusd', 'trigbtc', 'atombtc', 'bchpax', 'eosbusd', 'zileth', 'gtotusd',
                   'xrpbullusdt', 'onetusd', 'algobtc', 'bchsvusdt', 'gtopax', 'etceth', 'vibebtc', 'bttusdt', 'repeth',
                   'iostbnb', 'usdttry', 'btsbnb', 'ankrbnb', 'dltbnb', 'snteth', 'linktusd', 'nknusdt', 'rpxbtc',
                   'rdneth',
                   'cocosusdt', 'etcbusd', 'btttrx', 'bandbtc', 'steembnb', 'zecpax', 'viabnb', 'cosbnb', 'mtheth',
                   'xrpusdc',
                   'xemeth', 'pivxbnb', 'phxbtc', 'zilusdt', 'poeeth', 'bnbeur', 'bandusdt', 'vetbnb', 'lendbtc',
                   'xlmbnb',
                   'duskusdt', 'mfteth', 'funusdt', 'adabusd', 'perlbnb', 'btcbusd', 'ltobtc', 'nasbnb', 'algousdt',
                   'zeneth',
                   'bchsvusdc', 'mcousdt', 'venbnb', 'hceth', 'fetusdt', 'edobtc', 'mftbnb', 'cosusdt', 'arpausdt',
                   'xmrusdt',
                   'ctxcusdt', 'bqxbtc', 'npxsusdc', 'icxbnb', 'bchbnb', 'phbusdc', 'tomousdc', 'nulsbnb', 'rcnbnb',
                   'arpabnb',
                   'qtumbtc', 'keyusdt', 'agibtc', 'mblbtc', 'eoseth', 'tusdbtc', 'aioneth', 'storjbtc', 'lsketh',
                   'bchsvbtc',
                   'bntbusd', 'ncashbtc', 'mblbnb', 'polybnb', 'aebnb', 'ltceth', 'dogeusdc', 'wpreth', 'syseth',
                   'bcnbtc',
                   'ognusdt', 'nanobtc', 'astbtc', 'zrxeth', 'adxeth', 'gxseth', 'ethbearbusd', 'onepax', 'scbtc',
                   'icxbtc',
                   'ontbnb', 'qlceth', 'btsbusd', 'rlcbtc', 'chatbtc', 'wabibnb', 'renbnb', 'xrpbullbusd', 'wavesbtc',
                   'funeth',
                   'rlcbnb', 'phxeth', 'winbtc', 'storjeth', 'wavesbusd', 'iostbtc', 'icxeth', 'adatusd', 'nknbnb',
                   'btcrub',
                   'pivxbtc', 'perlusdt', 'bullbusd', 'bttusdc', 'bcptbtc', 'aebtc', 'ethusdt', 'ltousdt', 'subbtc',
                   'thetabnb',
                   'blzbtc', 'tfuelusdt', 'evxbtc', 'hbarbtc', 'ambeth', 'winusdt', 'qtumeth', 'dgdbtc', 'adaeth',
                   'busdusdt',
                   'xrpbnb', 'adapax', 'usdsbusds', 'cocosbnb', 'navbtc', 'rvnbtc', 'tnbbtc', 'bnbbtc', 'neopax',
                   'bearusdt',
                   'usdstusd', 'snmbtc', 'rvnbnb', 'gtobnb', 'phbtusd', 'hcusdt', 'btcusds', 'reqbtc', 'ognbnb',
                   'lrcbtc',
                   'xrpeth', 'loometh', 'zectusd', 'vibeeth', 'gobtc', 'bnbtry', 'bcdeth', 'qkceth', 'neoeth',
                   'paxusdt',
                   'bchsvtusd', 'fetbnb', 'yoyobnb', 'xlmbusd', 'skyeth', 'paxeth', 'ltcbtc', 'xvgeth', 'tnbeth',
                   'stratbusd',
                   'agieth', 'xlmusdt', 'lskbtc', 'bearbusd', 'hsreth', 'ctxcbnb', 'oaxbtc', 'qspbtc', 'iotxeth',
                   'qlcbnb',
                   'algousdc', 'etcpax', 'fueleth', 'aionusdt', 'xmreth', 'maticbtc', 'dashbnb', 'oneusdt', 'brdeth',
                   'viaeth',
                   'omgeth', 'ankrtusd', 'usdsusdt', 'ethtusd', 'wavestusd', 'iosteth', 'cmtbnb', 'ostbnb', 'ltcusdt',
                   'ethtry',
                   'zrxbtc', 'bchabcusdt', 'onebnb', 'beamusdt', 'nebleth', 'bcptbnb', 'adxbnb', 'ontbtc', 'bttbnb',
                   'dockusdt',
                   'bccbtc', 'omgbtc', 'algopax', 'neousdt', 'xrprub', 'busdngn', 'appceth', 'dentusdt', 'xzcbnb',
                   'tfueltusd',
                   'xembnb', 'arpabtc', 'ankrusdc', 'adausdc', 'kmdeth', 'troybnb', 'bnbeth', 'ltcusdc', 'databtc',
                   'blzbnb',
                   'naveth', 'btcbbtc', 'battusd', 'bnbngn', 'bchbusd', 'busdrub', 'ltctusd', 'vetbusd', 'ongbnb',
                   'fttusdt',
                   'bccusdt', 'ongusdt', 'engeth', 'usdctusd', 'etcbtc', 'gtousdc', 'mdaeth', 'vitebnb', 'erdusdt',
                   'dltbtc',
                   'bnbtusd', 'wtcbtc', 'xrpusdt', 'xrpeur', 'agibnb', 'trxtusd', 'ethbullbusd', 'iotabtc', 'xembtc',
                   'bchabcusdc', 'duskusdc', 'xrppax', 'mblusdt', 'kmdbtc', 'neblbtc', 'maticbnb', 'bnbrub', 'bcpteth',
                   'bttbtc', 'stxbnb', 'dlteth', 'onteth', 'vetusdt', 'ppteth', 'ethbtc', 'onebtc', 'ethbusd', 'zecbtc',
                   'erdbnb', 'xrpbearusdt', 'stratbnb', 'cmtbtc', 'cvcbtc', 'kncbtc', 'rpxbnb', 'zenbnb', 'cndbnb',
                   'ardrbnb',
                   'bchabcbusd', 'ltcbnb', 'pivxeth', 'skybtc', 'tntbtc', 'poebtc', 'steembtc', 'icxusdt', 'tfuelbtc',
                   'chzbtc',
                   'vibeth', 'winusdc', 'gtobtc', 'linkusdc', 'batbusd', 'rdnbtc', 'dataeth', 'bttpax', 'zrxbnb',
                   'vibbtc',
                   'neobnb', 'cosbtc', 'powreth', 'rlcusdt', 'hbarbnb', 'wabieth', 'bqxeth', 'aionbtc', 'aeeth',
                   'mthbtc',
                   'wrxbtc', 'pptbtc', 'nknbtc', 'zecusdt', 'stormeth', 'qtumusdt']

        channels = ['kline_1m', 'kline_5m', 'kline_15m', 'kline_30m', 'kline_1h', 'kline_12h', 'kline_1w', 'trade',
                    'miniTicker', 'depth20']

        self.__class__.ubwa.create_stream(False, False, stream_label="error")

        stream_id1 = ""
        for channel in channels:
            stream_id1 = self.__class__.ubwa.create_stream(channel, markets, output="UnicornFy")

        time.sleep(6)
        self.__class__.ubwa.set_restart_request(stream_id1)
        time.sleep(6)
        self.__class__.ubwa.set_restart_request(stream_id1)

        restserver = BinanceWebSocketApiRestServer(self.__class__.ubwa)
        restserver.get("icinga")
        restserver.get("invalid")
        del restserver

        markets = ['xrpbearbusd', 'zeceth', 'cndbtc', 'dashbtc', 'atompax', 'perlbtc', 'ardreth', 'zecbnb',
                   'erdbnb', 'xrpbearusdt', 'stratbnb', 'cmtbtc', 'cvcbtc', 'kncbtc', 'rpxbnb', 'zenbnb', 'cndbnb',
                   'wrxbtc', 'pptbtc', 'nknbtc', 'zecusdt', 'stormeth', 'qtumusdt']

        streams = []
        for channel in channels:
            stream_id = self.__class__.ubwa.create_stream(channel, markets, stream_buffer_name=channel,
                                                          ping_interval=10, ping_timeout=10, close_timeout=5)
            streams.append(stream_id)

        stream_id2 = streams.pop()
        self.__class__.ubwa.create_stream('depth20', markets, stream_buffer_name=True)
        time.sleep(6)
        self.__class__.ubwa.stop_stream_as_crash(streams.pop())
        self.__class__.ubwa.create_websocket_uri(False, False, stream_id1)
        self.__class__.ubwa.unsubscribe_from_stream(stream_id2, markets="erdbnb")
        self.__class__.ubwa.unsubscribe_from_stream(stream_id2, channels="trade")
        self.__class__.ubwa.pop_stream_data_from_stream_buffer()
        self.__class__.ubwa.pop_stream_data_from_stream_buffer()
        self.__class__.ubwa.pop_stream_data_from_stream_buffer()
        self.__class__.ubwa.pop_stream_data_from_stream_buffer(stream_buffer_name="invalid")
        stream_id_1_1 = self.__class__.ubwa.replace_stream(streams.pop(), 'trade', 'kncbtc', "name")
        self.__class__.ubwa.replace_stream(stream_id_1_1, 'trade', 'kncbtc', "name2",
                                           new_ping_interval=10, new_ping_timeout=10, new_close_timeout=5)
        self.__class__.ubwa.get_results_from_endpoints()
        self.__class__.ubwa.get_used_weight()
        self.__class__.ubwa.get_start_time()
        self.__class__.ubwa.get_stream_label(stream_id1)
        self.__class__.ubwa.get_stream_label(False)
        self.__class__.ubwa.get_keep_max_received_last_second_entries()
        request_id = self.__class__.ubwa.get_stream_subscriptions(stream_id2)
        self.__class__.ubwa.get_result_by_request_id(request_id)
        self.__class__.ubwa.get_reconnects()
        self.__class__.ubwa.get_errors_from_endpoints()
        self.__class__.ubwa.get_monitoring_status_plain()
        self.__class__.ubwa.get_ringbuffer_error_max_size()
        self.__class__.ubwa.get_ringbuffer_result_max_size()
        self.__class__.ubwa.set_ringbuffer_error_max_size(200)
        self.__class__.ubwa.set_ringbuffer_result_max_size(300)
        self.__class__.ubwa.set_stream_label(stream_id2, "blub")
        self.__class__.ubwa._add_stream_to_stream_list(self.__class__.ubwa.get_new_uuid_id(),
                                                       'trade', 'btceth')
        self.__class__.ubwa._restart_stream(stream_id1)
        self.__class__.ubwa.delete_stream_from_stream_list(stream_id1)
        self.__class__.ubwa.delete_listen_key_by_stream_id(stream_id1)
        self.__class__.ubwa.is_update_availabe_unicorn_fy()
        self.__class__.ubwa.get_version_unicorn_fy()
        self.__class__.ubwa.create_payload(stream_id2, "invalid", channels="trade")
        time.sleep(6)
        self.__class__.ubwa.get_result_by_request_id(request_id)
        self.__class__.ubwa.get_result_by_request_id()
        self.__class__.ubwa.set_keep_max_received_last_second_entries(30)
        self.__class__.ubwa.stop_stream_as_crash(stream_id2)
        time.sleep(6)
        print(f"Waiting for {stream_id2} has started")
        self.__class__.ubwa.wait_till_stream_has_started(stream_id2)
        print(f"Done!")
        self.__class__.ubwa.stop_stream(stream_id2)
        self.__class__.ubwa.add_to_ringbuffer_error("test")
        self.__class__.ubwa.add_to_ringbuffer_result("test")
        self.__class__.ubwa.get_number_of_free_subscription_slots(stream_id2)
        self.__class__.ubwa.get_most_receives_per_second()
        self.__class__.ubwa.get_number_of_streams_in_stream_list()
        self.__class__.ubwa.is_update_availabe_check_command()
        print(f"Waiting for {stream_id2} has stopped")
        self.__class__.ubwa.wait_till_stream_has_stopped(stream_id2)
        print(f"Done!")
        self.__class__.ubwa.print_stream_info(stream_id2)
        self.__class__.ubwa.print_summary()
        self.__class__.ubwa.print_summary_to_png(".", 12.5)
        self.__class__.ubwa.get_latest_release_info()
        self.__class__.ubwa.get_latest_release_info_check_command()
        self.__class__.ubwa.set_private_dex_config("bnb1v566f3avl2ud5z0jepazsrguzkj367snlx4jm6")
        self.__class__.ubwa.get_version()
        self.__class__.ubwa.help()
        self.__class__.ubwa.get_current_receiving_speed_global()
        self.__class__.ubwa.remove_ansi_escape_codes("test text")
        self.__class__.ubwa.pop_stream_signal_from_stream_signal_buffer()

        from unicorn_binance_rest_api import BinanceRestApiManager

        with BinanceRestApiManager(exchange="binance.us") as ubra:
            markets = []
            data = ubra.get_all_tickers()
            for item in data:
                markets.append(item['symbol'])
        self.__class__.ubwa.create_stream("trade", markets, stream_label="too much!")

        self.__class__.ubwa.stop_manager()


if __name__ == '__main__':
    unittest.main()
