import requests
from irlabpy.config import MonitorItemServiceConfig
from irlabpy.data_model.monitoring_item import AnomalyDetectionMonitoringItem
from irlabpy.data_model.metrics import TimeSeriesMetric
import ast
import logging
from typing import List
from typing import Dict
import json


class MonitorItemService:
    """
    监控项数据管理
    """
    def __init__(self):
        self.__FEATURE_STORE_CONFIG = MonitorItemServiceConfig()
        self.domain = self.__FEATURE_STORE_CONFIG.domain
        self.open_api_prefix = self.__FEATURE_STORE_CONFIG.open_api_prefix

    @staticmethod
    def __build_monitor_item_from_response(records):
        monitor_items = {}
        for element in records:
            try:
                tags = json.loads(element['tags'])
            except Exception as e:
                logging.error("%s: invalid parameter tags: %s." % (e, element['tags']))
                continue
            monitor_item = AnomalyDetectionMonitoringItem()
            monitor_item.add_time_series_metric(TimeSeriesMetric(
                ds_id=element['dsId'],
                tags=tags,
                metric_name=element['metricName'],
            ))
            if element['dsId'] in monitor_items:
                monitor_items[element['dsId']].append(monitor_item)
            else:
                monitor_items[element['dsId']] = [monitor_item]
        return monitor_items

    def query_page_by_solution(self, app_name, instance_name, solution_name, page_size=0x7fffffff) -> \
            Dict[str, List[AnomalyDetectionMonitoringItem]]:
        """ 根据solution name分页查询监控项记录
        Args:
            app_name:
            instance_name:
            solution_name:
            page_size: 分页读取时的页大小
        Returns:
            dict, key为ds_id, value为ds_id相同的一组AnomalyDetectionMonitoringItem对象的列表
        """
        page_number = 1
        while True:
            params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                      "pageSize": page_size, "pageNumber": page_number}
            response = requests.get(url=self.domain + self.open_api_prefix + '/pageQuery', params=params)
            resp_json = response.json()
            try:
                ts_metric_data = resp_json['data']["rows"]
                if not ts_metric_data:
                    return None
                page_number += 1
                yield MonitorItemService.__build_monitor_item_from_response(ts_metric_data)
            except Exception as e:
                return None

    def query_by_solution(self, app_name, instance_name, solution_name) -> \
            Dict[str, List[AnomalyDetectionMonitoringItem]]:
        """ 根据solution name查询监控项记录
        Args:
            app_name:
            instance_name:
            solution_name:
        Returns:
            dict, key为ds_id, value为ds_id相同的一组AnomalyDetectionMonitoringItem对象的列表
        """
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name}
        response = requests.get(url=self.domain + self.open_api_prefix + '/query', params=params)
        resp_json = response.json()
        ts_metric_data = resp_json['data']
        if not ts_metric_data:
            return None

        monitor_item_dic = {}
        for element in ts_metric_data:
            try:
                tags = ast.literal_eval(element['tags'])
            except Exception as e:
                logging.error("%s: invalid parameter tags: %s." % (e, element['tags']))
                continue
            monitor_item = AnomalyDetectionMonitoringItem()
            monitor_item.add_time_series_metric(TimeSeriesMetric(
                ds_id=element['dsId'],
                tags=tags,
                metric_name=element['metricName'],
            ))
            if element['dsId'] in monitor_item_dic:
                monitor_item_dic[element['dsId']].append(monitor_item)
            else:
                monitor_item_dic[element['dsId']] = [monitor_item]
        return monitor_item_dic

    def query_by_instance(self, app_name, instance_name) -> Dict[str, List[AnomalyDetectionMonitoringItem]]:
        """ 根据instance name查询监控项记录
        Args:
            app_name:
            instance_name:
        Returns:
            dict, key为ds_id, value为ds_id相同的一组AnomalyDetectionMonitoringItem对象的列表
        """
        params = {'appName': app_name, 'instanceName': instance_name}
        response = requests.get(url=self.domain + self.open_api_prefix + '/queryByInstance', params=params)
        resp_json = response.json()
        ts_metric_data = resp_json['data']
        if not ts_metric_data:
            return None

        monitor_item_dic = {}
        for element in ts_metric_data:
            try:
                tags = ast.literal_eval(element['tags'])
            except Exception as e:
                logging.error("%s: invalid parameter tags: %s." % (e, element['tags']))
                continue
            monitor_item = AnomalyDetectionMonitoringItem()
            monitor_item.add_time_series_metric(TimeSeriesMetric(
                ds_id=element['dsId'],
                tags=tags,
                metric_name=element['metricName'],
            ))
            if element['dsId'] in monitor_item_dic:
                monitor_item_dic[element['dsId']].append(monitor_item)
            else:
                monitor_item_dic[element['dsId']] = [monitor_item]
        return monitor_item_dic

    def query_specific_record(self, app_name: str, instance_name: str, solution_name: str, ds_id: str, tags: str,
                              metric_name: str) -> AnomalyDetectionMonitoringItem:
        """ 根据具体信息查询特定的监控项记录
        Args:
            app_name:
            instance_name:
            solution_name:
            ds_id:
            tags:
            metric_name:
        Returns:
            AnomalyDetectionMonitoringItem对象
        """
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name, 'dsId': ds_id,
                  'tags': tags, 'metricName': metric_name}
        response = requests.get(url=self.domain + self.open_api_prefix + '/querySpecific', params=params)
        resp_json = response.json()
        ts_metric_data = resp_json['data']
        if not ts_metric_data:
            return None

        monitor_item = AnomalyDetectionMonitoringItem()
        for element in ts_metric_data:
            try:
                tags = ast.literal_eval(element['tags'])
            except Exception as e:
                logging.error("%s: invalid parameter tags: %s." % (e, element['tags']))
                continue
            monitor_item.add_time_series_metric(TimeSeriesMetric(
                ds_id=element['dsId'],
                tags=tags,
                metric_name=element['metricName'],
            ))
        if monitor_item.time_series_metrics == {}:
            return None
        return monitor_item

    def add_record(self, app_name, instance_name, solution_name, ds_id, tags, metric_name, extra=None):
        """ 添加记录
        Args:
            app_name:
            instance_name:
            solution_name:
            ds_id:
            tags:
            metric_name:
            extra: 额外的信息，可为空
        Returns:
        """
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                  'dsId': ds_id, 'tags': tags, 'metricName': metric_name, 'extra': extra}
        resp = requests.post(url=self.domain + self.open_api_prefix + '/add', json=params)
        logging.info("finish inserting monitor item.")

    def delete_record(self, app_name, instance_name, solution_name, ds_id, tags, metric_name):
        """ 删除记录
        Args:
            app_name:
            instance_name:
            solution_name:
            ds_id:
            tags:
            metric_name:
        Returns:
        """
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                  'dsId': ds_id, 'tags': tags, 'metricName': metric_name}
        resp = requests.post(url=self.domain + self.open_api_prefix + '/delete', json=params)
        logging.info("finish deleting record.")

    def update_record(self, app_name, instance_name, solution_name, ds_id, tags, metric_name, extra):
        """ 更新记录的extra信息
        Args:
            app_name:
            instance_name:
            solution_name:
            ds_id:
            tags:
            metric_name:
            extra:
        Returns:
        """
        params = {'appName': app_name, 'instanceName': instance_name, 'solutionName': solution_name,
                  'dsId': ds_id, 'tags': tags, 'metricName': metric_name, 'extra': extra}
        resp = requests.post(url=self.domain + self.open_api_prefix + '/update', json=params)
        logging.info("finish updating record.")


if __name__ == '__main__':
    monitor_item_service = MonitorItemService()

    data = monitor_item_service.query_by_instance(app_name='irlabpy', instance_name='wnx_demo_test')
    print(data)
