# 统计与限流
import json

import requests


class EventTrackingProxy:

    # 根据返回值决定是否限流
    # True 通行
    # False 限流
    @classmethod
    def upload(cls, token, ds_id, env, tags_list_size, start, end):
        params = {'token': token, 'dsId': ds_id, 'env': env, 'tagListSize': tags_list_size, 'start': start, 'end': end}
        dataJson = json.dumps(params)
        headers = {'Content-Type': 'application/json'}
        url = 'https://irlabprod-pre.alipay.com/openapi/sdk/eventTracking'
        response = requests.post(url=url, data=dataJson,
                                 headers=headers)
        jsonResponse = json.loads(response.text)
        if response.status_code != 200:
            return True
        if jsonResponse.get('resultCode') == 200:
            data = jsonResponse.get('data')
            return data
        else:
            return True
