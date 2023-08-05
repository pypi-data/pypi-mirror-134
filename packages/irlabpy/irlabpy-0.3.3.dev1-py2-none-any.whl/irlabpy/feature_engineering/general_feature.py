"""
存放一些通用特征算子
"""

import numpy as np
from prophet import Prophet
from sklearn.linear_model import LinearRegression
import pandas as pd
import datetime
import tsfresh as tsf


def to_prophet_df(ts: dict):
    """
    将时序数据转化为prophet的输入的dataframe
    """
    ds = []
    y = []
    for ms_timestamp in ts.keys():
        val = ts[ms_timestamp]
        if val is None:
            continue
        s_timestamp = ms_timestamp / 1000
        ds.append(datetime.datetime.fromtimestamp(s_timestamp))
        y.append(val)
    return pd.DataFrame({"ds": ds, "y": y})


def get_ts_sparsity(ts: dict, threshold=0.25, sparse_values=[None, 0], interval=60000):
    """
    评估时序数据的稀疏度
    :param ts: 时序数据，key为单位为毫秒的timestamp
    :param threshold: 稀疏度>threshold 会被判定为稀疏
    :param sparse_values: sparse_values中的值被判定为稀疏点
    :return: 返回dict对象，score表示稀疏度，ret为是否稀疏判定结果，判定稀疏为True
    """
    timestamp_arr = [t for t in ts.keys()]
    start = min(timestamp_arr)
    end = max(timestamp_arr)
    timestamp = start
    sparse_count = 0
    nonsparse_count = 0
    while timestamp <= end:
        value = ts.get(timestamp)
        if value in sparse_values:
            sparse_count += 1
        else:
            nonsparse_count += 1
        timestamp += interval
    score = sparse_count / (sparse_count + nonsparse_count)
    ret = score > threshold
    return {"score": score, "ret": ret}


def get_ts_stationarity(ts: dict, threshold=0.05):
    """
    评估时序数据的平稳性
    :param ts: 时序数据，key为单位为毫秒的timestamp
    :param threshold: 平稳分>threshold 会被判定为平稳
    :return: 返回dict对象，score表示平稳性分数，ret为是否平稳判定结果，判定平稳为True
    """
    values = []
    for t in sorted(ts.keys()):
        value = ts[t]
        if value is not None:
            values.append(value)

    data = pd.Series(values)
    param = [{'attr': 'pvalue'}]
    ae = tsf.feature_extraction.feature_calculators.augmented_dickey_fuller(
        data, param)
    p_value = ae[0][1]
    score = p_value
    ret = score > threshold
    return {"score": score, "ret": ret}


def get_ts_daily_seasonality(ts: dict, threshold=0.8):
    """
    评估日周期性，返回值越接近1说明，日周期性越明显，小于0.5说明基本无日周期性
    使用了prophet做时序分解，fit速度较慢
    :param ts: 时序数据，key为单位为毫秒的timestamp
    :param threshold: 平稳分>threshold 会被判定为有日周期
    :return: 返回dict对象，score表示周期性分数，ret为是否有日周期判定结果，判定有日周期为True
    """
    df = to_prophet_df(ts)
    model = Prophet(yearly_seasonality=False,
                    daily_seasonality=True)
    model.add_country_holidays(country_name='China')
    model.fit(df)

    # making prediction of trend and seasonality features
    trend_component = model.predict_trend(model.history)
    seasonal_components = model.predict_seasonal_components(model.history)
    y_trend = trend_component.values
    y_daily = seasonal_components['daily'].values

    lr = LinearRegression()
    x = [[i] for i in range(len(y_trend))]
    lr.fit(x, y_trend)
    # TODO 移动平均会更好
    y_linear_trend = [i[0] * lr.coef_[0] + lr.intercept_ for i in x]
    y_trend_residuals = y_trend - y_linear_trend
    weight_t = np.mean(np.abs(y_trend_residuals - np.mean(y_trend_residuals)))
    weight_d = np.mean(np.abs(y_daily - np.mean(y_daily)))
    daily_ratio = weight_d / (weight_d + weight_t)
    score = daily_ratio
    ret = score > threshold
    return {"score": score, "ret": ret}
