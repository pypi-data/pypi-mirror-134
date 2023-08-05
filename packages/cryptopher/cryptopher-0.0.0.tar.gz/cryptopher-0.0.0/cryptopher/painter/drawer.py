#!/usr/bin/env python
# Copyright (c) Cryptopher.

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.graph_objs.scatter.marker import Line

class Drawer:
    """
    Stock visualization tools
    """
    def __init__(self):
        pass

    @staticmethod
    def _check_mode(df, mode):
        pass

    def visualize(df, mode="Default", buy_at=30, sell_at=70):
        """
        Visualize strategy
        Args:
            mode (string): mode of visualization (eg. rsi, macd)
            buy_at (float): buy ratio for some strategy (eg. rsi)
            sell_at (float): sell ratio for some strategy (eg. rsi)
        """
        if mode == 'Default':
            Drawer._st_volume(df)
        elif mode == 'rsi':
            Drawer._st_rsi(df, buy_at, sell_at)
        elif mode == 'macd':
            pass
        else:
            print(f'Invalid Mode')

    @staticmethod
    def _obj_candle(df):
        return go.Candlestick(x=df["Datetime"], open=df["open"], high=df["high"],
                low=df["low"], close=df["close"], name="Price")

    @staticmethod
    def _obj_buy_sell(df):
        def filter_signal(df, sig):
            df = df[df['signal'] == sig]
            if sig == 1:
                x = go.Scatter(x=df['Datetime'], y=df['close'], mode='markers',
                           marker=dict(color='LightSkyBlue', symbol = 'triangle-up', size=8)
                               , name='buy')
            elif sig == -1:
                x = go.Scatter(x=df['Datetime'], y=df['close'], mode='markers',
                           marker=dict(color='lightsalmon', symbol = 'triangle-down', size=8)
                               , name='sell')
            return x
        return [filter_signal(df, 1), filter_signal(df, -1)]

    @staticmethod
    def _gen_st_candle(df):
        rs = [Drawer._obj_candle(df)]
        rs.extend(Drawer._obj_buy_sell(df))
        return rs

    @staticmethod
    def _vis_st_candle(df, fig):
        rs1 = Drawer._gen_st_candle(df)
        for elem in rs1:
            fig.add_trace(elem, row=1, col=1)
        return fig

    @staticmethod
    def _init_fig(name):
        return make_subplots(rows=2, cols=1, shared_xaxes=True,
               vertical_spacing=0.03, subplot_titles=('Cryptopher', name),
               row_width=[0.2, 0.7])

    @staticmethod
    def _logo(fig):
        fig.update(layout_xaxis_rangeslider_visible=False)
        fig.update_layout( title='www.cryptopher.info')
        fig.layout.template = 'plotly_dark'
        fig.show()

    @staticmethod
    def _st_volume(df):
        fig = Drawer._init_fig('Trading Volume')
        fig = Drawer._vis_st_candle(df, fig)
        fig.add_trace(go.Bar(x=df['Datetime'], y=df['trade_volume'], showlegend=False), row=2, col=1)
        Drawer._logo(fig)

    @staticmethod
    def _st_rsi(df, buy_at=30, sell_at=70):
        fig = Drawer._init_fig('RSI')
        fig = Drawer._vis_st_candle(df, fig)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['rsi'], showlegend=False, mode='lines', line={'color':'sandybrown'}), row=2, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=[buy_at for i in range(df.shape[0])], showlegend=False, mode='lines', line={'dash': 'dash', 'color': 'lightgreen'}), row=2, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=[sell_at for i in range(df.shape[0])], showlegend=False, mode='lines', line={'dash': 'dash', 'color': 'lightskyblue'}), row=2, col=1)
        Drawer._logo(fig)
