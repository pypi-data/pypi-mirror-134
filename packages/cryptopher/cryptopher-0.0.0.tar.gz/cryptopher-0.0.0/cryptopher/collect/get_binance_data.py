#!/usr/bin/env python
# Copyright (c) Cryptopher.

from binance.client import Client
import numpy as np
import pandas as pd
from datetime import datetime

class GetBinanceData():
    """
    Get cryptocurrency data from binance exchange through python-binance
    """
    def __init__(self, tf: str, start_date: str):
        """
        Args:
            tf (string): timeframe
            start_date (string): first date or datetime to collect data
        """
        self.map_tf(tf)
        self.start_date = start_date
        api_key = api_secret = '1'
        self.client = Client(api_key, api_secret)
        self.all_sym = [x['symbol'] for x in self.client.get_exchange_info()['symbols']]

    def map_tf(self, tf):
        map_dict = {'1h': Client.KLINE_INTERVAL_1HOUR, '2h': Client.KLINE_INTERVAL_2HOUR, '4h': Client.KLINE_INTERVAL_4HOUR,
        '6h': Client.KLINE_INTERVAL_6HOUR, '12h': Client.KLINE_INTERVAL_12HOUR, '1d': Client.KLINE_INTERVAL_1DAY,
        '1w': Client.KLINE_INTERVAL_1WEEK}
        self.timeframe = map_dict[tf]

    @property
    def get_all_symbol(self):
        return self.all_sym

    def get_data(self, target_name, tf=None, start=None):
        """
        Get data
        Args:
            target_name (string): cryptocurrency pair
            tf (string): timeframe
            start (string): first date or datetime
        Return:
            df (pd.DataFrame): cryptocurrency pair information (datetime, open, close, high, low, trading_volume)
        """
        if tf is None:
            tf = self.timeframe
        if start is None:
            start = self.start_date
        print('Process:',target_name,tf,start)
        if target_name not in self.all_sym:
            print(f'Not Found: {target_name}')
            return pd.DataFrame(data, columns=['A', 'B', 'C'])
        bars = self.client.get_historical_klines(target_name, tf, start)
        return GetBinanceData.prep_data(bars)

    def prep_data(bars):
        for idx, line in enumerate(bars):
            del line[6:]
            line = [float(l) for l in line]
            line[0] = int(line[0])/1000
            bars[idx] = line
        df = pd.DataFrame(bars, columns=['Datetime','open','high','low','close','trade_volume'])
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df['Datetime'] = df.Datetime.apply(lambda x : datetime.fromtimestamp(x))
        return df
