#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ''
secret = ''

spot_client = Client(key, secret, show_header=True)
logging.info(spot_client.withdraw(coin='BNB', amount=0.01, address=''))
