"""
定义监控项相关数据结构
"""

from irlabpy.data_model.metrics import TimeSeriesMetric
from irlabpy.utils import hash_by_murmur


class AnomalyDetectionMonitoringItem:
    """
    定义异常检测监控项
    """

    def __init__(self):
        self.time_series_metrics = {}

    def add_time_series_metric(self, time_series_metric: TimeSeriesMetric):
        """
        监控项中添加时序指标
        :param time_series_metric:
        :return:
        """
        self.time_series_metrics[hash(time_series_metric)] = time_series_metric

    def __hash__(self):
        time_series_metric_hash_codes = [k for k in self.time_series_metrics.keys()]
        # 对hashcode排序
        time_series_metric_hash_codes = sorted(time_series_metric_hash_codes)
        return hash_by_murmur(str(time_series_metric_hash_codes))
