import os
import configparser
import base64
import ast


class FeatureStoreConfig:
    """
    特征中心的配置
    """

    def __init__(self, cfg_file="prod_config.ini"):
        dir_path = os.path.join(*list(os.path.split(os.path.dirname(__file__))))
        config = configparser.ConfigParser()
        config.read(os.path.join(dir_path, cfg_file), encoding='UTF-8')
        self.domain = config.get('feature_store', 'domain')
        self.open_api_prefix = config.get('feature_store', 'open_api_prefix')
        self.odps_project = config.get('feature_store', 'odps_project')
        self.odps_endpoint = config.get('feature_store', 'odps_endpoint')
        self.odps_feature_data_table = config.get('feature_store', 'odps_feature_data_table')

        b64_id = config.get('feature_store', 'odps_access_id')
        b64_key = config.get('feature_store', 'odps_secret_access_key')
        self.odps_access_id = str(base64.b64decode(b64_id), 'utf8')
        self.odps_secret_access_key = str(base64.b64decode(b64_key), 'utf8')


class MonitorItemServiceConfig:
    """
    监控项存取的配置
    """

    def __init__(self, cfg_file="prod_config.ini"):
        dir_path = os.path.join(*list(os.path.split(os.path.dirname(__file__))))
        config = configparser.ConfigParser()
        config.read(os.path.join(dir_path, cfg_file), encoding='UTF-8')
        self.domain = config.get('monitor_item_service', 'domain')
        self.open_api_prefix = config.get('monitor_item_service', 'open_api_prefix')


class DataSyncJobServiceConfig:
    """
    数据同步的配置
    """

    def __init__(self, cfg_file="prod_config.ini"):
        dir_path = os.path.join(*list(os.path.split(os.path.dirname(__file__))))
        config = configparser.ConfigParser()
        config.read(os.path.join(dir_path, cfg_file), encoding='UTF-8')
        self.domain = config.get('data_sync_job_service', 'domain')
        self.api_prefix = config.get('data_sync_job_service', 'api_prefix')
        try:
            self.headers = ast.literal_eval(config.get('data_sync_job_service', 'headers'))
        except Exception as e:
            self.headers = {}


class Pontus2ClientConfig:
    def __init__(self, cfg_file="prod_config.ini"):
        dir_path = os.path.join(*list(os.path.split(os.path.dirname(__file__))))
        config = configparser.ConfigParser()
        config.read(os.path.join(dir_path, cfg_file), encoding='UTF-8')
        self.domain = config.get('pontus_2_client', 'domain')
        self.test_domain = config.get('pontus_2_client', 'test_domain')
        self.query_tags_pages = config.get('pontus_2_client', 'query_tags_pages')
        self.query_tags_by_page = config.get('pontus_2_client', 'query_tags_by_page')
        self.query_trends_by_tags = config.get('pontus_2_client', 'query_trends_by_tags')


if __name__ == '__main__':
    f = FeatureStoreConfig()
    print(f.odps_access_id)
    print(f.odps_secret_access_key)

    m = MonitorItemServiceConfig()
    print(m.domain)
    print(m.open_api_prefix)

    d = DataSyncJobServiceConfig()
    print(d.domain)
    print(d.api_prefix)
    print(d.headers)
