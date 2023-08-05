from odps import ODPS
from odps.df import DataFrame
from odps.df import Delay
from irlabpy.data_model.metrics import TimeSeriesMetric
from irlabpy.data_model.monitoring_item import AnomalyDetectionMonitoringItem
from irlabpy.data_model.feature import MonitorData
from irlabpy.config import FeatureStoreConfig
from irlabpy.dev.data_sync import DataSync
import datetime
import logging
# from deprecated.sphinx import deprecated
from typing import Dict
from typing import List
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


class BaseDataReader:
    def __init__(self):
        pass

    @staticmethod
    def is_valid_time_interval(start_timestamp: int, end_timestamp: int):
        """ 判断输入的时间戳范围是否合法
        Args:
            start_timestamp: 开始时间戳
            end_timestamp: 结束时间戳
        """
        if start_timestamp < 0 or end_timestamp < 0:
            return False
        if start_timestamp >= end_timestamp:
            return False
        return True

    @staticmethod
    def convert_timestamp_to_datetime(timestamp: int):
        """
        将时间戳转化为datetime对象
        """
        return datetime.datetime.fromtimestamp(int(timestamp) // 1000)

    @staticmethod
    def standard_output(data, data_type="Unknown Type", monitor_key=None):
        return MonitorData(data=data, data_type=data_type, monitor_key=monitor_key)

    def process(self, *args, **kwargs):
        pass


class BaseODPSTSDataReader(BaseDataReader):
    """
    ODPS数据读取基类
    """
    __PARTITION_FORMAT = {
        'dt': 'dt=%Y%m%d',
        'dt_hh': 'dt=%Y%m%d,hh=%H'
    }

    def __init__(self, project_name: str, odps_table_name: str):
        super(BaseODPSTSDataReader, self).__init__()
        self.__FEATURE_STORE_CONFIG = FeatureStoreConfig()
        self.odps = ODPS(
            access_id=self.__FEATURE_STORE_CONFIG.odps_access_id,
            secret_access_key=self.__FEATURE_STORE_CONFIG.odps_secret_access_key,
            project=project_name,
            endpoint=self.__FEATURE_STORE_CONFIG.odps_endpoint
        )
        self.table_name = odps_table_name  # 表名
        self.table = self.odps.get_table(self.table_name)
        self.schema = self.table.schema
        self.partitions = self.schema.partitions  # 分区名称

    def get_partition_names(self, start_timestamp: int, end_timestamp: int):
        """ 根据开始和结束时间戳获取所有的分区名
        Args:
            start_timestamp: 开始时间戳
            end_timestamp: 结束时间戳
        Returns:
            分区名的list
        """
        all_partitions = []
        if self.partitions is None or len(self.partitions) == 0:
            return all_partitions
        if self.partitions[0].name != 'dt':
            return all_partitions

        start_datetime = self.convert_timestamp_to_datetime(start_timestamp)
        end_datetime = self.convert_timestamp_to_datetime(end_timestamp)
        tmp_date = start_datetime
        if len(self.partitions) == 1 or self.partitions[1].name != 'hh':
            delta = datetime.timedelta(days=1)
            while tmp_date <= end_datetime:
                time_str = tmp_date.strftime(self.__PARTITION_FORMAT['dt'])
                all_partitions.append(time_str)
                tmp_date += delta
            all_partitions.append(tmp_date.strftime(self.__PARTITION_FORMAT['dt']))
        else:
            delta = datetime.timedelta(hours=1)
            while tmp_date <= end_datetime:
                time_str = tmp_date.strftime(self.__PARTITION_FORMAT['dt_hh'])
                all_partitions.append(time_str)
                tmp_date += delta
            all_partitions.append(tmp_date.strftime(self.__PARTITION_FORMAT['dt_hh']))
        return all_partitions

    def get_partition_dataframes(self, partition_names: List) -> List:
        """ 根据partition name的list获取partition的dataframe的list
        Args:
            partition_names: 分区名称的list
        Returns:
            DataFrame对象的list
        """
        partition_dfs = []
        for partition_name in partition_names:
            logging.info("Number of partitions is %d. Processing %s." % (len(partition_names), partition_name))
            partition = self.table.get_partition(partition_name)
            df = DataFrame(partition)
            partition_dfs.append(df)
        return partition_dfs

    def process(self, start_timestamp: int = 0, end_timestamp: int = 0, *args, **kwargs):
        """ 时序数据获取的接口。
        Args:
            start_timestamp: 需要获取时序数据的开始时间戳
            end_timestamp: 需要获取时序数据的结束时间戳
        Returns:
        """
        pass


class StandardODPSTSDataReader(BaseODPSTSDataReader):
    """
    标准ODPS时序数据获取类
    """
    TIME_STAMP_NAME = 'period'

    def __init__(self, odps_table_name: str):
        """
        Args:
            odps_table_name: odps表名称
        """
        super().__init__(project_name=FeatureStoreConfig().odps_project, odps_table_name=odps_table_name)
        self.__data_sync = DataSync()
        self.__valid_ds_ids = set()

    def __check_sync_table(self, ds_id: str):
        if ds_id in self.__valid_ds_ids:
            return True
        sync_table_name = self.__data_sync.search_odps_table_with_ds_id(ds_id)
        if sync_table_name == self.table_name:
            self.__valid_ds_ids.add(ds_id)
            return True
        else:
            return False

    def get_time_series_data(self, df_tsm: DataFrame, ts_metric: TimeSeriesMetric):
        """ 返回一条线的时序数据
        Args:
            df_tsm:
            ts_metric: 一个TimeSeriesMetric对象
        Returns:
            时序数据, Dict[int, float], <时间戳，该点的指标数值>
        """
        # 判断离线数据同步是否为当前表
        if not self.__check_sync_table(ts_metric.ds_id):
            return None

        lower_case_metric_name = ts_metric.metric_name.lower()

        # 判断是否存在该指标项
        if lower_case_metric_name not in self.schema:
            return None

        # 根据tags进行判断
        for key in ts_metric.tags:
            lower_case_key = key.lower()
            if lower_case_key not in self.schema:
                return None
            df_tsm = df_tsm[df_tsm[lower_case_key] == ts_metric.tags[key]]

        df_tsm = df_tsm[self.TIME_STAMP_NAME, lower_case_metric_name]
        pd_df_tsm = df_tsm.to_pandas()
        if pd_df_tsm.shape[0] == 0:
            return None
        pd_df_tsm = pd_df_tsm.astype({
            self.TIME_STAMP_NAME: 'int',
            lower_case_metric_name: 'float',
        })
        ts_data = pd_df_tsm.set_index([self.TIME_STAMP_NAME])[lower_case_metric_name].to_dict()
        return ts_data

    def process(self, start_timestamp: int = 0, end_timestamp: int = 0, monitor_items=None, *args, **kwargs):
        if monitor_items is None:
            logging.error("monitor items cannot be none.")
            return None

        start_time_int = int(start_timestamp)
        end_time_int = int(end_timestamp)
        if not self.is_valid_time_interval(start_time_int, end_time_int):
            logging.error("not a valid time interval")
            return None
        partition_names = self.get_partition_names(start_time_int, end_time_int)
        partition_dfs = self.get_partition_dataframes(partition_names=partition_names)
        if len(partition_dfs) == 0:
            partition_dfs = [DataFrame(self.table)]
        for i in range(len(partition_dfs)):
            partition_dfs[i] = partition_dfs[i][partition_dfs[i][self.TIME_STAMP_NAME].between(start_timestamp,
                                                                                               end_timestamp)]

        if type(monitor_items) == AnomalyDetectionMonitoringItem:  # 单个监控项
            return self.__process_mi_list([monitor_items], partition_dfs)
        elif type(monitor_items) == list:  # ds_id相同的一组监控项
            return self.__process_mi_list(monitor_items, partition_dfs)
        else:
            return None

    def __process_mi_list(self, monitor_item_list: List[AnomalyDetectionMonitoringItem],
                          partition_dfs: List[DataFrame]) -> Dict[AnomalyDetectionMonitoringItem, MonitorData]:
        """ 一组监控项的时序数据获取
        Args:
            monitor_item_list: 监控项的list
            partition_dfs: dataframe的列表
        Returns:
            字典，key为监控项的hash值，value为MonitorData对象，存储该监控项的时序数据
        """
        with ThreadPoolExecutor(max_workers=len(monitor_item_list)) as thread_item:
            all_item_ts_data = {}
            task_list = []
            for monitor_item in monitor_item_list:
                task = thread_item.submit(self.__monitor_item_task, monitor_item, partition_dfs)
                task_list.append(task)

            for future in as_completed(task_list):
                result = future.result()
                if result is not None:
                    all_item_ts_data.update(result)
        return all_item_ts_data

    def __monitor_item_task(self, monitor_item: AnomalyDetectionMonitoringItem, partition_dfs: List[DataFrame]) -> Dict:
        try:
            ts_metrics = monitor_item.time_series_metrics
        except Exception as e:
            logging.error("cannot load time series metrics from monitor item.")
            return None

        with ThreadPoolExecutor(max_workers=len(partition_dfs) * len(ts_metrics)) as thread_partition:
            all_partition_ts_data = {}
            task_list = {}
            for key in ts_metrics.keys():
                ts_metric: TimeSeriesMetric = ts_metrics[key]
                for partition_df in partition_dfs:
                    task = thread_partition.submit(self.get_time_series_data, partition_df, ts_metric)
                    task_list[task] = ts_metric.unique_name

            for future in as_completed(task_list):
                ts_data = future.result()
                unique_name = task_list[future]
                if ts_data is not None:
                    if unique_name not in all_partition_ts_data:
                        all_partition_ts_data[unique_name] = ts_data
                    else:
                        all_partition_ts_data[unique_name].update(ts_data)
        if len(all_partition_ts_data) == 0:
            return {hash(monitor_item): None}
        return {
            hash(monitor_item): self.standard_output(data=all_partition_ts_data,
                                                     data_type=MonitorData.DataType.TSM_UNIQUE_NAME_MAP,
                                                     monitor_key=hash(monitor_item))
        }


if __name__ == '__main__':
    pass
