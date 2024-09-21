import functions as fn
import pandas as pd
import calculatings as cal
import info

for c in info.coin:
    for i in info.intervals_2:
        df = fn.get(c, i, 499)
        df = fn.clean(df)
        sma7 = cal.sma(df, 7)
        sma20 = cal.sma(df, 20)
        ema20 = cal.ema(df, 20)
        k, d, j = cal.kdj(df)
        upper, lower = cal.bb(df)
        macd = cal.macd(df)

        if (
            sma7.iloc[-1] > ema20.iloc[-1] > sma20.iloc[-1]
            and macd.iloc[-1] > 0
            and k.iloc[-1] < d.iloc[-1]
            and j.iloc[-2] < j.iloc[-1]
            and upper.iloc[-1] > upper.iloc[-2]
            and lower.iloc[-1] > lower.iloc[-2]
        ):
            print(c, i, "buy")
        elif (
            sma7.iloc[-1] < ema20.iloc[-1] < sma20.iloc[-1]
            and macd.iloc[-1] < 0
            and k.iloc[-1] > d.iloc[-1]
            and j.iloc[-2] > j.iloc[-1]
            and upper.iloc[-1] < upper.iloc[-2]
            and lower.iloc[-1] < lower.iloc[-2]
        ):
            print(c, i, "sell")
