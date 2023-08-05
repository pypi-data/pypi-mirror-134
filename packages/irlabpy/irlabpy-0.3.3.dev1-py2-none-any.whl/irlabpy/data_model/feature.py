"""
定义与离线特征工程相关的对象
"""
from enum import Enum
import logging


class MonitorData:
    """
    监控数据封装的类，用于管理不同类型的监控数据
    """

    class DataType(Enum):
        """
        描述监控数据类型，便于用户理解
        """
        METRIC_NAME_MAP = "<metric_name, time_series_data>"  # 监控指标和时序数据的字典
        TSM_OBJECT_MAP = "<TimeSeriesMetric_obj_hash, time_series_data>"  # TimeSeriesMetric对象hash值和时序数据的字典
        TSM_UNIQUE_NAME_MAP = "<TimeSeriesMetric_unique_name, time_series_data_map>"  # TimeSeriesMetric对象unique
        # name和时序数据的字典

    def __init__(self, data, data_type: DataType = "Unknown Type", monitor_key=None):
        """ 用时序数据初始化
        Args:
            data: 时序数据
            data_type: 数据的类型
            monitor_key: 监控项标识
        """
        self.__data = data  # 监控项数据
        self.__data_type = data_type  # 监控项数据类型
        self.__monitor_key = monitor_key  # 监控项标识，将监控项数据与监控项关联

    def get_monitor_data(self):
        return self.__data

    def set_data_type(self, data_type: DataType):
        self.__data_type = data_type

    def get_data_type(self):
        try:
            return self.__data_type.value
        except AttributeError:
            return self.__data_type

    def get_metric_data(self, unique_name=None):
        """ 返回监控项某个metric的数据，如果metric的unique_name为空，返回字典序第一个metric的数据。
            如果数据类型不是以unique_name为key的map，返回所有的数据。
        Args:
            unique_name: 监控项metric的标识
        """
        if self.__data_type != self.DataType.TSM_UNIQUE_NAME_MAP:
            logging.error("data type is not %s" % self.DataType.TSM_UNIQUE_NAME_MAP.value)
            return self.__data
        if unique_name is None:
            try:
                metric_data = list(self.__data.values())[0]
                return metric_data
            except Exception as e:
                logging.error(e, "cannot get time series data for one metric")
                return self.__data
        else:
            if unique_name not in self.__data:
                logging.error("no such key: %s" % unique_name)
                return self.__data
            else:
                return self.__data[unique_name]

    def set_monitor_key(self, monitor_key):
        self.__monitor_key = monitor_key

    def get_monitor_key(self):
        return self.__monitor_key


if __name__ == '__main__':
    data = {'cost': {1626832980000: 69.2, 1626833040000: 69.66666666666667, 1626833100000: 78.0, 1626833160000: 51.625,
                     1626833220000: 44.5, 1626833280000: 61.666666666666664, 1626833340000: 45.25, 1626833400000: 128.0,
                     1626833460000: 140.0, 1626833520000: 88.5, 1626833580000: 72.375, 1626833640000: 124.0,
                     1626833700000: 70.0, 1626833760000: 36.0, 1626833820000: 66.7, 1626833880000: 78.0,
                     1626833940000: 49.333333333333336, 1626834000000: 71.66666666666667, 1626834060000: 54.0,
                     1626834120000: 75.5, 1626834180000: 62.142857142857146, 1626834240000: 62.4, 1626834300000: 70.75,
                     1626834360000: 88.5, 1626834420000: 85.28571428571429, 1626834480000: 77.5, 1626834540000: 103.0,
                     1626834600000: 90.0, 1626834660000: 84.33333333333333, 1626834720000: 80.66666666666667,
                     1626834780000: 76.5, 1626834840000: 67.25, 1626834900000: 72.2, 1626834960000: 62.666666666666664,
                     1626835020000: 64.0, 1626835080000: 72.66666666666667, 1626835140000: 61.714285714285715,
                     1626835200000: 77.0, 1626835260000: 58.857142857142854, 1626835320000: 67.5, 1626835380000: 57.4,
                     1626835440000: 60.0, 1626835500000: 73.16666666666667, 1626835560000: 68.125, 1626835620000: 79.0,
                     1626835680000: 87.85714285714286, 1626835740000: 70.0, 1626835800000: 74.0, 1626835860000: 52.0,
                     1626835920000: 81.6, 1626835980000: 63.666666666666664, 1626836040000: 89.5,
                     1626836100000: 46.333333333333336, 1626836160000: 87.57142857142857, 1626836220000: 78.6,
                     1626836280000: 67.5, 1626836340000: 74.0}}
    monitor_data = MonitorData(data, data_type=MonitorData.DataType.TSM_UNIQUE_NAME_MAP)
    t = monitor_data.get_metric_data(unique_name="cost")
    print(t)
