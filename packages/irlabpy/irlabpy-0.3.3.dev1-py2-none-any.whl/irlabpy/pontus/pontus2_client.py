import json
import logging
import time
from typing import Dict, List

import requests

from irlabpy.config import Pontus2ClientConfig
from irlabpy.pontus.event_tracking_proxy import EventTrackingProxy
from irlabpy.pontus.trend import Trend


class Pontus2Client:
    # env 可填：test、prod
    def __init__(self, env, token):
        self.env = env
        self.token = token
        self.config = Pontus2ClientConfig();
        if env == 'test':
            self.config.domain = self.config.test_domain

    def query_tags(self, ds_id, conditions) -> List[Dict[str, str]]:
        end = round(time.time() * 1000)
        start = end - 1000 * 60 * 60 * 24 * 7
        pages = self.__query_tags_pages(ds_id, start, end)
        totalTags = []
        for page in pages:
            pageTags = self.__query_tags_by_page(page, ds_id, start, end, conditions)
            totalTags.extend(pageTags)
        return totalTags

    def __query_tags_pages(self, ds_id, start, end) -> List[int]:
        data = {'table': ds_id, 'start': start, 'end': end}
        dataJson = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=self.config.domain + self.config.query_tags_pages, data=dataJson, headers=headers)
        jsonResponse = json.loads(response.text)
        return jsonResponse

    def __query_tags_by_page(self, page, ds_id, start, end, conditions) -> List[Dict[str, str]]:
        result = []
        data = {'table': ds_id, 'start': start, 'end': end, 'partition': page, 'conditions': conditions}
        dataJson = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=self.config.domain + self.config.query_tags_by_page, data=dataJson,
                                 headers=headers)
        jsonResponse = json.loads(response.text)
        if response.status_code != 200:
            logging.error(jsonResponse)
            return result
        tagHeaders = jsonResponse.get('tags').get('headers')
        tagDatas = jsonResponse.get('tags').get('datas')
        for tagsData in tagDatas:
            tags = {}
            for index in range(0, len(tagsData)):
                tags[tagHeaders[index]] = tagsData[index]
            result.append(tags)
        return result

    # List[Dict[str, str], Dict[int, any]]
    #        tags        ,   timestamp metricsName:value
    def query_trends(self, ds_id, start, end, metrics_names, tags_list) -> List[Trend]:
        trackingResult = EventTrackingProxy.upload(self.token, ds_id, self.env, len(tags_list), start, end)
        if not trackingResult:
            logging.error(f'token={self.token}被限流，请检查 token 限流阈值')
        data = {'table': ds_id, 'start': start, 'end': end, 'tagList': tags_list, 'metrics': metrics_names}
        dataJson = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=self.config.domain + self.config.query_trends_by_tags, data=dataJson,
                                 headers=headers)
        jsonResponse = json.loads(response.text)
        result = []
        if response.status_code != 200:
            logging.error(jsonResponse)
            return result
        for i in range(0, len(jsonResponse)):
            trend = Trend(jsonResponse[i])
            result.append(trend)
        return result


if __name__ == "__main__":
    # env 可填 test、prod，分别为线下测试环境和线上环境，线上环境在本地无法调通
    pontus2Client = Pontus2Client(env='test', token=None)
    dsId = 'Awatch@@awatch_monitor_rt_v2@@app_zone_module_sig_rt@@DEFAULT@@1@@DEFAULT'
    start = 1629703810000
    end = 1629707410000
    # conditions 是查询 tags 的查询条件，例如填 app=tradecore ，则查询出来的 tags 全部包含 app=tradecore
    # conditions 为空时查询整表全部 tags
    conditions = None
    tagsList = pontus2Client.query_tags(dsId, conditions)
    batchSize = 50
    totalTrends = []
    for i in range(0, len(tagsList), batchSize):
        tagsBatchList = tagsList[i:i + batchSize]
        # 使用 tags 查询对应的时序数据，在查询时建议对 tags 做个分批处理。避免一次性查询大量 tags 时序数据
        # 当查询数据量过大时会报错，查不到时序数据
        # metrics_name 为要查询的 metrics，如果不需要使用此 tags 下的所有 metrics ，可以指定 metrics_name 降低查询量
        trends = pontus2Client.query_trends(dsId, start, end, None, tagsBatchList)
        totalTrends.extend(trends)
    # TODO: process pontus data
