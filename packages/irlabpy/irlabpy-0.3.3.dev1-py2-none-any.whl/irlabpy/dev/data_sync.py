import requests
import re
# from deprecated.sphinx import deprecated
from irlabpy.config import DataSyncJobServiceConfig


class DataSync:
    def __init__(self):
        self.__FEATURE_STORE_CONFIG = DataSyncJobServiceConfig()
        self.domain = self.__FEATURE_STORE_CONFIG.domain
        self.api_prefix = self.__FEATURE_STORE_CONFIG.api_prefix
        self.headers = self.__FEATURE_STORE_CONFIG.headers

    # @deprecated(version="0.1.6", reason="该方法为模糊查询，请使用search_odps_table_with_ds_id")
    # def search_sync_job(self, ds_id):
    #     """ 根据ds_id查询表名, 模糊搜索数据同步任务
    #     Args:
    #         ds_id:
    #     Returns:
    #         odps表名: str，查询成功
    #         None: 查询失败
    #     """
    #     params = {"condition": ds_id}
    #     url = self.domain + self.api_prefix + "/sync/search"
    #     resp = requests.get(url=url, params=params, headers=self.headers)
    #     try:
    #         data = resp.json()
    #         if data['data'] is not None and len(data['data']) > 0:
    #             project_table = data['data'][0]['odps']
    #             return re.split("\.", project_table)[-1]
    #         else:
    #             return None
    #     except ValueError:
    #         return None

    def search_odps_table_with_ds_id(self, ds_id):
        """ 根据dsId表名查询对应的odps表名
        Args:
            ds_id:
        Returns:
            odps表名: str，查询成功
            None: 查询失败
        """
        params = {"dsId": ds_id}
        url = self.domain + self.api_prefix + "/manage/dsid/search"
        resp = requests.get(url=url, params=params, headers=self.headers)
        try:
            data = resp.json()
            if data['data'] is not None and len(data['data']) > 0:
                project_table = data['data'][0]
                return re.split("\.", project_table)[-1]
            else:
                return None
        except ValueError:
            return None

    def submit_sync_job(self, ds_id, odps_table_name="", job_type="HOUR", description="sync job"):
        """ 提交数据同步任务
        Args:
            ds_id:
            odps_table_name: odps表名，默认为空，此时自动根据ds_id自动生成表名
            job_type: 默认为HOUR
            description:
        """
        params = {
            "ceresdbName": ds_id,
            "odpsTable": odps_table_name,
            "jobType": job_type,
            "description": description,
            "creator": ""
        }
        url = self.domain + self.api_prefix + "/apply/submit"
        resp = requests.post(url=url, json=params, headers=self.headers)
        print(resp.text)


if __name__ == '__main__':
    odps_table_name_query = DataSync()
    ds_id = "sofa@@service@@aig@@GRAY@@1@@DEFAULT"
    odps_table_name_query.submit_sync_job(ds_id, description="wnx特征工程test")
    # table = odps_table_name_query.search_odps_table_with_ds_id(ds_id)
    # print(table)
