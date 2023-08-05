"""
定义各种指标类型
"""
from irlabpy.utils import sort_dict_by_key, hash_by_murmur, get_public_attrs
from typing import Dict


class TimeSeriesMetric:
    """
    定义时序指标
    """

    def __init__(self, ds_id: str = None, tags: Dict[str, str] = None, metric_name: str = None,
                 unique_name: str = None):
        """

        :param ds_id: 数据源id
        :param tags: 在数据库中索引tag组合条件，e.g: {"app":"minitrans","ldc":"RZ42B"}
        :param metric_name: 指标名称，e.g: "fail"
        :param unique_name: 用户定义的指标别名，用于和其他指标进行区分，为None的使用metric_name赋值
        """
        self.ds_id = ds_id
        # 对tags中内容按key升序排序
        self.tags = sort_dict_by_key(tags)
        self.metric_name = metric_name
        if unique_name is None:
            self.unique_name = metric_name
        else:
            self.unique_name = unique_name


    def __hash__(self):
        attrs = sort_dict_by_key(get_public_attrs(self))
        return hash_by_murmur(str(attrs))


if __name__ == "__main__":
    tsm = TimeSeriesMetric("xxxx", tags={"t1": "3"}, metric_name="fail")
    tsm1 = TimeSeriesMetric("xxxx", tags={"t1": "3"}, metric_name="fail")
    print(hash(tsm))
    a = {}
    a[tsm] = 1
    a[tsm1] = 1
    print(len(a))
