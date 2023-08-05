#!/usr/bin/env python
# Copyright (c) Cryptopher.

import pandas as pd

class BackTest:
    """
    Backtest analysis
    """
    def __init__(self, percent_fee: float = 0.1000):
        """
        Args:
            percent_fee (float): percent premium rate per trading order
        """
        self.fee = percent_fee/100

    def compute_state_asset(self, prices, signals, invest):
        """
        Compute each state portfolio valuation (No. asset, Port value, Fee)
        Args:
            prices (list, pandas): series of prices
            signals (list, pandas): series of signals
            invest (float): investment valuation
        Return:
            assets (dict of list): dictionary of each state portfolio valuation
        """
        # Init results
        premium = self.fee
        asset = [0 for i in range(len(prices))]
        value = [0 for i in range(len(prices))]
        fee = [0 for i in range(len(prices))]
        a = 0

        # Compute each state
        for idx, s in enumerate(signals):
            p = prices[idx] # current price
            f = 0 # fee

            # buy signal
            if s == 1 and invest > 0:
                f = premium*invest
                a += (invest-f)/p
                invest = 0

            # sell signal
            elif s == -1 and a > 0:
                invest += a*p
                a = 0
                f = premium*invest
                invest -= f

            # update state
            asset[idx] = a
            value[idx] = invest+a*p
            fee[idx] = f
        return {'asset': asset, 'value': value, 'fee': fee}

    def run(self, df, buy_at='close', invest=1000, report=False):
        """
        Compute backtest
        Args:
            df (pd.DataFrame): stock information (open, high, low, close, signal)
            buy_at (str): buy at price (open or close)
            invest (float): investment valuation
            report (bool): get report or not
        Return (report == True):
            df (pd.DataFrame): stock information + state valutaion
        """
        # Compute and add state valutaion
        ass_val = self.compute_state_asset(df[buy_at], df['signal'], invest)
        df = df.join(pd.DataFrame(ass_val))

        # Compute net profit and profit and loss
        net = round(df['value'].values[-1], 2)
        pnl = round(df['value'].values[-1]-invest, 2)
        ppnl = round((pnl/invest)*100, 3)
        def add_plus(t):
            return '+'+str(t) if t > 0 else str(t)
        pnl_str = add_plus(pnl)
        ppnl_str = add_plus(ppnl)
        try:
            se_word = f"From {df.loc[0, 'Datetime']} to {df.loc[df.shape[0]-1, 'Datetime']}"
        except:
            se_word = ''
        print(f"Cryptopher's backtest: \n{se_word}\n\nInvest: $ {invest}\nCurrent Value: $ {net}\nProfit & Loss: $ {pnl_str} ( {ppnl_str} % )")

        if report:
            return df
