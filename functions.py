from binance.um_futures import UMFutures
import pandas as pd
import numpy as np
import time


def get(coin, interval, days):
    um_futures_client = UMFutures()
    get_coin = um_futures_client.continuous_klines(
        coin, "PERPETUAL", interval, limit=days
    )
    time.sleep(0.1)
    return pd.DataFrame(get_coin)


def clean(df):
    df.columns = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "qav",
        "num_trades",
        "taker_base_vol",
        "taker_quote_vol",
        "ignore",
    ]

    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["open_time"] = df["open_time"].dt.tz_localize(
        "UTC", ambiguous="NaT", nonexistent="NaT"
    )
    df["open_time"] = df["open_time"].dt.tz_convert("US/Pacific")

    df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
    df["close_time"] = df["close_time"].dt.tz_localize(
        "UTC", ambiguous="NaT", nonexistent="NaT"
    )
    df["close_time"] = df["close_time"].dt.tz_convert("US/Pacific")

    df.set_index(["open_time"], inplace=True)
    df = df.tz_localize(None)

    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "qav",
        "taker_base_vol",
        "taker_quote_vol",
    ]
    df[numeric_columns] = df[numeric_columns].astype(float)
    df["num_trades"] = df["num_trades"].astype(int)

    return df
