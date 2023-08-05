import json

import requests
import tbase

from irlabpy.cache.cache import Cache
from irlabpy.utils import get_key_by_datasource


class TBaseClient(Cache):

    def __init__(self, token, connection_string):
        self.token = token
        self._client = tbase.Client(connection_string)
        self.url = ''
        self.headers = {'Content-Type': 'application/json'}

    def query_metrics_with_time_window(self, table, tags, start, end, tenant='default'):
        """
        获取时序数据
        TODO: 如果cache未命中考虑从数据源头实时拉取
        :param table: 表名
        :param tags: 维度组合
        :param start: 时间起始
        :param end: 时间截止
        :param tenant: 租户
        :param scores: 是否带时间戳,默认True
        :return:
        """
        r = self._client

        time_to_metrics = {}

        key = get_key_by_datasource(table, tags, tenant)

        count = r.zcount(key, start, end)
        if count == 0:
            self._add_metrics(table, tags, start, end, tenant)

        items = r.zrangebyscore(name=key, min=start, max=end, withscores=True)
        for pair in items:
            time_to_metrics[int(pair[1])] = json.loads(pair[0])[str(int(pair[1]))]
        return time_to_metrics

    def _cache_miss(self):
        pass

    def _expire(self, table, tags, tenant='default', ex_time=25 * 60 * 60):
        pass

    def _add_metrics(self, table, tags, start, end, tenant):
        r = self._client
        key = get_key_by_datasource(table, tags, tenant)
        count = 0
        trends = self._query_remote_metrics(table, tags, start_time=start, end_time=end)
        for trend in trends:
            mapping = {json.dumps({trend['period']: trend['metrics']}): trend['period']}
            if r.zcount(key, trend['period'], trend['period']) < 1:
                if r.zadd(key, mapping) == 1:
                    count += 1
            else:
                continue
        return count

    def _query_remote_metrics(self, table, tags, start_time, end_time):
        payload = {"table": table, "tags": tags, "start": start_time, "end": end_time}
        response = requests.request("POST", self.url, headers=self.headers, data=json.dumps(payload))
        return json.loads(response.text.encode('utf8'))["trends"]

    def remove_metrics_with_time_window(self, table, tags, start, end, tenant='default'):
        r = self._client
        key = get_key_by_datasource(table, tags, tenant)
        return r.zremrangebyscore(key, start, end)


if __name__ == '__main__':
    #  SPM@@727146262@@DEFAULT, tags: {接口=MobileTrusteeOrderAndPaymentHandle} ,result: 0
    connection_string = 'servers=11.166.117.235:6001,11.166.117.235:6002,11.166.32.118:6001,11.166.32.118:6002;cluster=publicsecondgztbase;tenant=antmonitoralarm;connection timeout=3000;redis timeout=2000;'
    client = TBaseClient(token='ai', connection_string=connection_string)
    client.url = "http://pontusconsole.alipay.com:8080/api/1.0.0/metrics/trend"
    # print(
    #     client.remove_metrics_with_time_window('SPM@@727146262@@DEFAULT', {'接口': 'MobileTrusteeOrderAndPaymentHandle'},
    #                                            1638345600000, 1638346200000))
    metrics = client.query_metrics_with_time_window('sofa@@error@@app@@DEFAULT@@1@@DEFAULT',
                                                    {'app': 'promobench'}, 1639039920000,
                                                    1639039920000, tenant='AI')
    print(metrics)
    # print(client.zcount('af8f65d06f087c42b1ee9a13c5bfb865', 0, 1638340992000))
    # print(client.zcard('af8f65d06f087c42b1ee9a13c5bfb865'))
