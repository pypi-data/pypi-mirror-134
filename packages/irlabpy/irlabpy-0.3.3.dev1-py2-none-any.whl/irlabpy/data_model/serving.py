"""
定义服务接口相关数据模型
"""
import json
from typing import Dict, List

from irlabpy.utils import sort_dict_by_key


class AnomalyDetectionServingOutput:
    """
    定义异常检测服务接口的输出对象
    """
    ATTR_NAME_RESULT = "result"  # 异常检测结果
    ATTR_NAME_ANOMALY_DURATION = "anomalyDuration"  # 异常持续时长
    ATTR_NAME_MSG = "msg"  # 异常描述文案
    ATTR_NAME_SCORE = "score"  # 异常分数
    ATTR_NAME_ANOMALY_FEATURE_MAP = "anomalyFeatureMap"  # 异常特征
    ATTR_NAME_EXT_INFO = "extInfo"  # 附加信息

    def __init__(self):
        self.__data = {}

    def to_json(self) -> str:
        """
        异常检测输出对象json格式化
        :return:
        """
        return json.dumps(self.__data)

    def set_result(self, ret: bool):
        """
        设置异常检测结果
        :param ret: True表示发现异常, False表示未发现异常
        """
        self.__data[AnomalyDetectionServingOutput.ATTR_NAME_RESULT] = ret

    def get_result(self) -> bool:
        """
        获取异常检测结果
        :return:
        """
        return self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_RESULT)

    def set_anomaly_duration(self, anomaly_duration: int):
        """
        设置异常持续时长
        :param anomaly_duration: 异常持续时长
        """
        self.__data[AnomalyDetectionServingOutput.ATTR_NAME_ANOMALY_DURATION] = anomaly_duration

    def get_anomaly_duration(self) -> int:
        """
        获取异常持续时长
        :return:
        """
        return self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_ANOMALY_DURATION)

    def set_msg(self, msg: str) -> str:
        """
        设置异常描述文案
        :param msg: 异常描述文案
        """
        self.__data[AnomalyDetectionServingOutput.ATTR_NAME_MSG] = msg

    def get_msg(self):
        """
        获取异常描述文案
        :return:
        """
        return self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_MSG)

    def set_score(self, score: float):
        """
        设置异常分数
        :param score: 异常分数
        """
        self.__data[AnomalyDetectionServingOutput.ATTR_NAME_SCORE] = score

    def get_score(self) -> float:
        """
        获取异常分数
        :return:
        """
        return self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_SCORE)

    def set_anomaly_feature(self, feature_name: str, feature_value: str):
        """
        设置异常现象的特征
        :param feature_name: 特征名称
        :param feature_value: 特征值字符串
        """
        anomaly_features = self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_ANOMALY_FEATURE_MAP)
        if anomaly_features is None:
            anomaly_features = {}
            self.__data[AnomalyDetectionServingOutput.ATTR_NAME_ANOMALY_FEATURE_MAP] = anomaly_features
        anomaly_features[feature_name] = feature_value

    def get_anomaly_feature(self, feature_name: str) -> str:
        """
        获取异常现象的特征
        :param feature_name: 特征名称
        """
        anomaly_features = self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_ANOMALY_FEATURE_MAP)
        if anomaly_features is None:
            return None
        return anomaly_features.get(feature_name)

    def set_ext_info(self, key: str, value: str):
        """
        设置用户附带信息
        :param key: 附带信息索引
        :param value: 附带信息
        :return:
        """
        ext_info = self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_EXT_INFO)
        if ext_info is None:
            ext_info = {}
            self.__data[AnomalyDetectionServingOutput.ATTR_NAME_EXT_INFO] = ext_info
        ext_info[key] = value

    def get_ext_info(self, key: str) -> str:
        """
        获取用户附带信息
        :param key: 附带信息索引
        :return:
        """
        ext_info = self.__data.get(AnomalyDetectionServingOutput.ATTR_NAME_EXT_INFO)
        if ext_info is None:
            return None
        return ext_info.get(key)


class AnomalyDetectionServingInput:
    """
    定义异常检测服务接口的输入对象
    """
    PARAM_NAME_TIME_SERIES_DATA = "timeSeriesData"
    PARAM_NAME_DETECTED_METRICS = "detectedMetrics"
    PARAM_NAME_DETECTED_TIMESTAMP = "detectedTimestamp"
    PARAM_NAME_USER_DEFINED_PARAMS = "userDefinedParams"
    PARAM_NAME_FEATURE_MAP = "featureMap"
    PARAM_NAME_PRE_STATUS = "preStatus"
    PARAM_NAME_TAGS = "tags"

    def __init__(self):
        self.time_series_data = None  # 异常检测算法输入时序
        self.detected_metrics: List[str] = None  # 异常检测算法依赖的指标范围
        self.detected_timestamp: int = None  # 检测时间点
        self.user_defined_params: Dict[str, str] = None  # 用户自定义参数
        self.feature_map: Dict[str, str] = None  # 特征数据
        self.pre_status: str = None  # 上一个检测时间点的状态数据的格式化字串
        self.tags: Dict[str, str] = None  # 业务标签信息
        self.monitored_target_index = None  # 监控项索引, 用户如果接入非平台管理的监控项，需要传入监控项索引信息

    @staticmethod
    def load_from_post_req(post_params):
        """
        从post请求中加载参数
        :param post_params: post请求参数dict
        :return: AnomalyDetectionInput
        """
        query_params: dict = eval(post_params.get('body', None))
        if query_params is None:
            return None
        data_model = AnomalyDetectionServingInput()

        data_model.__set_time_series_data(
            query_params.get(AnomalyDetectionServingInput.PARAM_NAME_TIME_SERIES_DATA))
        data_model.detected_metrics = query_params.get(AnomalyDetectionServingInput.PARAM_NAME_DETECTED_METRICS)
        data_model.detected_timestamp = query_params.get(AnomalyDetectionServingInput.PARAM_NAME_DETECTED_TIMESTAMP)
        data_model.user_defined_params = query_params.get(AnomalyDetectionServingInput.PARAM_NAME_USER_DEFINED_PARAMS)
        data_model.feature_map = query_params.get(AnomalyDetectionServingInput.PARAM_NAME_FEATURE_MAP)
        data_model.pre_status = query_params.get(AnomalyDetectionServingInput.PARAM_NAME_PRE_STATUS)
        data_model.tags = query_params.get(AnomalyDetectionServingInput.PARAM_NAME_TAGS)
        return data_model

    def __set_time_series_data(self, time_series_data: Dict[str, Dict]):
        """
        设置异常检测算法输入时序
        :param time_series_data: 类型为Dict[str: Dict], key为指标名称, value为指标对应的时序数据
        """
        if time_series_data is None:
            return
        self.time_series_data = {}

        for metric_name in time_series_data.keys():
            time_series = time_series_data.get(metric_name)
            new_time_series = {}
            for t in time_series.keys():
                # 时间戳原始格式可能是str需转为int
                new_time_series[int(t)] = time_series[t]
            # 按时间戳升序排序
            new_time_series = sort_dict_by_key(new_time_series)
            self.time_series_data[metric_name] = new_time_series
