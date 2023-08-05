from typing import Dict
from irlabpy.data_model.feature import MonitorData
from irlabpy.dev.feature_data_service import StandardFeatureStore
# from deprecated.sphinx import deprecated


class BaseFeatureOperator:
    """
    特征算子基类
    """
    APP_NAME = None
    INSTANCE_NAME = None
    SOLUTION_NAME = None
    FEATURE_NAME = None  # 特征名称
    FEATURE_TAGS = None  # 特征标签
    __STANDARD_FEATURE_STORE = StandardFeatureStore()

    def __init__(self, init_params=None):
        pass

    # @deprecated(version="0.1.8", reason="该方法被废弃，直接使用feature_name")
    # def get_key(self):
    #     """
    #     返回特征算子的标识
    #     """
    #     return self.FEATURE_NAME

    # @deprecated(version="0.1.8", reason="该方法被废弃，直接使用feature_tags")
    # def get_tags(self):
    #     """
    #     返回特征算子的标签
    #     """
    #     return self.FEATURE_TAGS

    @classmethod
    def standard_feature_query(cls, monitoring_item_index):
        return cls.__STANDARD_FEATURE_STORE.query(cls.APP_NAME, cls.INSTANCE_NAME, cls.SOLUTION_NAME, cls.FEATURE_NAME,
                                                  monitoring_item_index)

    def process(self, monitor_data_obj: MonitorData = None) -> str:
        """ 特征算子的实现逻辑
        Args:
            monitor_data_obj: 监控项数据
        Returns:
            特征值
        """
        data = monitor_data_obj.get_monitor_data()


if __name__ == '__main__':
    class FE(BaseFeatureOperator):
        def __init__(self):
            super(FE, self).__init__()
            pass
    FE.APP_NAME = 3
    print(FE.APP_NAME)
    print(BaseFeatureOperator.APP_NAME)
    print(FE().standard_feature_query(34))
