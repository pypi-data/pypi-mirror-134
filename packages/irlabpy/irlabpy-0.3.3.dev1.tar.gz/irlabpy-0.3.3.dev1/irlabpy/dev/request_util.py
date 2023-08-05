# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

domain = 'http://localhost:8888'

prefix = '/openapi/feature'


def storeFeatureData(context, models):
    print('now execute store feature data!')
    url = domain + prefix + '/storeData'

    feature_store_req = {'context': context, 'models': models}
    r = requests.post(url, json=feature_store_req)
    print(r.text)


def queryFeatureData(contexts, config, user_index):
    print('now execute query feature data!')

    url = domain + prefix + '/queryData'

    feature_data_query_req = {}
    feature_data_query_req["context"] = contexts
    feature_data_query_req["config"] = config
    feature_data_query_req["userIndex"] = user_index

    r = requests.post(url, json=feature_data_query_req)
    print(r.text)
    j = r.json()
    if len(j['data']) == 0:
        return ''
    return j['data'][0]['data']


if __name__ == '__main__':
    contexts = {'systemIndex': 'test-5'}
    config = 'test-config-2'
    user_index = 'test-userIndex-2'
    featureData = '{duration: 1000}'
    data = queryFeatureData(contexts, config, user_index)
    print('data = ', data)

    models = {'config': config, 'userIndex': user_index, 'data': featureData}
    storeFeatureData(contexts, [models])
    data = queryFeatureData(contexts, config, user_index)
    print('data = ', data)
