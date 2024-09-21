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
