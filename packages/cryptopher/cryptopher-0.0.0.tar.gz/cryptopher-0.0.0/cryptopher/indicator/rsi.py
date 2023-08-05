#!/usr/bin/env python
# Copyright (c) Cryptopher.

import numpy as np
import pandas as pd

def get_rsi(close, lookback):

    ret = np.array(close.diff()).reshape(-1)

    down = np.array([x if x < 0 else 0 for x in ret])
    up = ret-down
    def np_2_ewm(data):
        return pd.Series(np.abs(data)).ewm(com = lookback-1, adjust = False).mean()

    up_ewm = np_2_ewm(up)
    down_ewm = np_2_ewm(down)

    rs = up_ewm/down_ewm
    rsi = 100-(100/(1 + rs))

    rsi_df = pd.DataFrame(rsi).rename(columns = {0:'rsi'}).set_index(close.index)
    rsi_df = rsi_df.dropna()
    return rsi_df[3:]

def simulate_rsi(rsis, buy=30, sell=70):
    signal = [0 for i in range(len(rsis))]
    tmp = 0
    for idx, rsi in enumerate(rsis):
        if rsi < buy and tmp != 1:
            tmp = 1
            signal[idx] = 1
        elif rsi > sell and tmp != -1:
            tmp = -1
            signal[idx] = -1
    return signal
