# !/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from odps import ODPS
import logging
from irlabpy.config import FeatureStoreConfig
from typing import List


class BaseFeatureStore:
    # 特征中心配置
    __FEATURE_STORE_CONFIG = None

    def __init__(self):
        if self.__FEATURE_STORE_CONFIG is None:
            self.__FEATURE_STORE_CONFIG = FeatureStoreConfig()
        odps_instance = ODPS(self.__FEATURE_STORE_CONFIG.odps_access_id,
                             self.__FEATURE_STORE_CONFIG.odps_secret_access_key,
                             self.__FEATURE_STORE_CONFIG.odps_project,
                             endpoint=self.__FEATURE_STORE_CONFIG.odps_endpoint)
        self.feature_table = odps_instance.get_table(self.__FEATURE_STORE_CONFIG.odps_feature_data_table)
        self.domain = self.__FEATURE_STORE_CONFIG.domain
        self.open_api_prefix = self.__FEATURE_STORE_CONFIG.open_api_prefix


class StandardFeatureStore(BaseFeatureStore):
    """
    irlab特征中心，提供特征存储/查询能力的标准接口
    """

    def __init__(self):
        super(StandardFeatureStore, self).__init__()

    def store(self, app_name, instance_name, solution_name, monitoring_item_index, feature_name, data, tags=None):
        """
        存储特征数据
        :param app_name: 算法工程名称
        :param instance_name: instance name
        :param solution_name: solution name
        :param feature_name: 特征名称
        :param monitoring_item_index: 监控项索引
        :param data: 特征数据
        :param tags: 存放业务标签
        :return:
        """
        logging.info("begin to store feature data")
        record = self.feature_table.new_record(
            [app_name, instance_name, solution_name, feature_name, monitoring_item_index, tags, data])

        # TODO: 确认partition设置
        partition_format = 'dt={}'
        partition = partition_format.format('default')

        with self.feature_table.open_writer(partition=partition, create_partition=True) as writer:
            records = [record]
            writer.write(records)
        logging.info("finish storing feature data")

    def store_data(self, app_name, instance_name, solution_name, monitoring_item_index, feature_name, data, tags=None):
        """
        存储特征数据到在线存储
        :param app_name: 算法工程名称
        :param instance_name: instance name
        :param solution_name: solution name
        :param feature_name: 特征名称
        :param monitoring_item_index: 监控项索引
        :param data: 特征数据
        :param tags: 存放业务标签
        :return:
        """
        logging.info("begin to store feature data")
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                  'featureName': feature_name, 'monitorKey': monitoring_item_index, 'datas': data}
        request_data = {
            "models": [params]
        }
        resp = requests.post(url=self.domain + self.open_api_prefix + '/data', json=request_data)
        print(resp.text)

    def store_period_data(self, timestamp, app_name, instance_name, solution_name, monitoring_item_index, feature_name, data, tags=None):
        """
        存储特征数据到在线存储
        :param timestamp: 时间戳
        :param app_name: 算法工程名称
        :param instance_name: instance name
        :param solution_name: solution name
        :param feature_name: 特征名称
        :param monitoring_item_index: 监控项索引
        :param data: 特征数据
        :param tags: 存放业务标签
        :return:
        """
        logging.info("begin to store period feature data")
        params = {'timestamp': timestamp, 'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                  'featureName': feature_name, 'monitorKey': monitoring_item_index, 'datas': data}
        request_data = {
            "models": [params]
        }
        resp = requests.post(url=self.domain + self.open_api_prefix + '/data', json=request_data)
        print(resp.text)

    def batch_store_data(self, data: List):
        """
        批量存储特征数据到在线存储
        :param data: dic的list，每个dic包含appName、instanceName、solutionName、featureName、monitorKey、datas和tags
        :return:
        """
        logging.info("begin to batch store feature data")
        request_data = {
            "models": data
        }
        try:
            resp = requests.post(url=self.domain + self.open_api_prefix + '/data', json=request_data)
            print(resp.text)
        except Exception as e:
            logging.error(e)

    def query(self, app_name, instance_name, solution_name, feature_name=None, monitoring_item_index=None, tags=None):
        """
        查询特征数据
        :param app_name: 算法工程名称
        :param instance_name: instance name
        :param solution_name: solution name
        :param feature_name: 特征名称
        :param monitoring_item_index: 监控项索引
        :param tags: 存放业务标签
        :return:
        """
        logging.info("begin to query feature data")
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                  'featureName': feature_name, 'monitorKey': monitoring_item_index}
        resp = requests.get(url=self.domain + self.open_api_prefix + '/data', params=params)
        resp_json = resp.json()
        logging.info("finish querying feature data")
        return resp_json['data']


class CustomFeatureStore(BaseFeatureStore):
    """
    irlab特征中心，提供特征存储/查询能力的自定义接口
    """

    def __init__(self):
        super(StandardFeatureStore, self).__init__()

    def store(self, system_index, config, user_index, data):
        context = {'systemIndex': system_index}
        models = {'config': config, 'userIndex': user_index, 'data': data}
        url = self.domain + self.open_api_prefix + '/storeData'
        feature_store_req = {'context': context, 'models': models}
        r = requests.post(url, json=feature_store_req)
        print(r.text)

    def query(self, config, system_index, user_index):
        url = self.domain + self.open_api_prefix + '/queryData'
        feature_data_query_req = {"context": {'systemIndex': system_index}, "config": config, "userIndex": user_index}
        r = requests.post(url, json=feature_data_query_req)
        j = r.json()
        if len(j['data']) == 0:
            return ''
        return j['data'][0]['data']


if __name__ == '__main__':
    data = [
        {
            "appName": "irlabpy",
            "instanceName": "wnx_test_1",
            "solutionName": "test_solution",
            "featureName": "trend_base_line",
            "monitorKey": 2120778306744932734,
            "datas": 123
        },
        {
            "appName": "irlabpy",
            "instanceName": "wnx_test_1",
            "solutionName": "test_solution",
            "featureName": "trend_base_line_1",
            "monitorKey": 2120778306744932734,
            "datas": "test"
        }
    ]
    fe = StandardFeatureStore()
    fe.batch_store_data(data=data)
    fe.store_data(app_name="irlabpy", instance_name="wnx_test_1", solution_name="test_solution",
                  feature_name="trend_base_line_1", monitoring_item_index=2120778306744932734, data="test")
