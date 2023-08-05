from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from typing import Dict
from typing import List
from irlabpy.feature_engineering.base_feature_operator import BaseFeatureOperator
from irlabpy.data_model.feature import MonitorData


class ClassRegister:
    """
    自动注册所有用户自定义类，并提供统一运行函数的接口。
    """

    def __init__(self):
        self.__registered_map = {}  # 保存注册的类名与类的映射关系

    def register_cls(self, cls):
        """ 作为装饰器的函数
        Args:
            cls: 被装饰的类
        """
        self.__registered_map[cls.__name__] = cls

    def register_solution(self, app_name, instance_name, solution_name):
        """ 装饰器函数，填入应用名、项目名等有关信息
        Args:
            app_name:
            instance_name:
            solution_name:
        Returns:
        """

        def register(cls):
            self.__registered_map[cls.__name__] = cls
            cls.APP_NAME = app_name
            cls.INSTANCE_NAME = instance_name
            cls.SOLUTION_NAME = solution_name
            return cls

        return register

    def call_function_v0(self, init_params, *args, **kwargs) -> Dict[BaseFeatureOperator, Dict]:
        """ 作为统一调用所有注册类对象的process方法的接口。注册类需包含能处理统一输入的process()方法。
        Args:
            init_params: dict, 创建对象时的初始化参数字典。
            *args: tuple, 任意个无名参数。
            **kwargs: dict, 任意个关键字参数。
        Returns:
            key为特征算子类名的字典
        """
        with ThreadPoolExecutor(max_workers=len(self.__registered_map)) as t:
            process_result = {}
            task_list = {}
            for key in self.__registered_map:
                obj = self.__registered_map[key](init_params)
                task = t.submit(obj.process, *args, **kwargs)
                task_list[task] = key
            for future in as_completed(task_list.keys()):
                feature_value = future.result()
                if "monitor_data_obj" in kwargs and type(kwargs["monitor_data_obj"]) == MonitorData:
                    process_result[self.__registered_map[task_list[future]]] = {
                        "feature_data": feature_value,
                        "monitor_index": kwargs["monitor_data_obj"].get_monitor_key()
                    }
                else:
                    process_result[self.__registered_map[task_list[future]]] = {
                        "feature_data": feature_value,
                        "monitor_index": None
                    }
        return process_result

    def call_function(self, init_params, solution_name=None, *args, **kwargs) -> List[Dict]:
        """ 作为统一调用所有注册类对象的process方法的接口。注册类需包含能处理统一输入的process()方法。
        Args:
            init_params: dict, 创建对象时的初始化参数字典。
            solution_name: 只筛选对应solution name的特征算子进行计算
            *args: tuple, 任意个无名参数。
            **kwargs: dict, 任意个关键字参数。
        Returns:
            特征存储dict数据格式的list
        """
        with ThreadPoolExecutor(max_workers=len(self.__registered_map)) as t:
            process_result = []
            task_list = {}
            for key in self.__registered_map:
                if solution_name is None or solution_name == self.__registered_map[key].SOLUTION_NAME:
                    obj = self.__registered_map[key](init_params)
                    task = t.submit(obj.process, *args, **kwargs)
                    task_list[task] = key
            for future in as_completed(task_list.keys()):
                feature_value = future.result()
                cls: BaseFeatureOperator = self.__registered_map[task_list[future]]
                if "monitor_data_obj" in kwargs and type(kwargs["monitor_data_obj"]) == MonitorData:
                    process_result.append({
                        "appName": cls.APP_NAME,
                        "instanceName": cls.INSTANCE_NAME,
                        "solutionName": cls.SOLUTION_NAME,
                        "featureName": cls.FEATURE_NAME,
                        "monitorKey": kwargs["monitor_data_obj"].get_monitor_key(),
                        "datas": feature_value,
                        "tags": cls.FEATURE_TAGS
                    })
                else:
                    process_result.append({
                        "appName": cls.APP_NAME,
                        "instanceName": cls.INSTANCE_NAME,
                        "solutionName": cls.SOLUTION_NAME,
                        "featureName": cls.FEATURE_NAME,
                        "monitorKey": None,
                        "datas": feature_value,
                        "tags": cls.FEATURE_TAGS
                    })
        return process_result


if __name__ == '__main__':
    from irlabpy.feature_engineering.base_feature_operator import BaseFeatureOperator

    register = ClassRegister()


    @register.register_solution(app_name="test_app", instance_name="123", solution_name="sol")
    class Test(BaseFeatureOperator):
        FEATURE_NAME = "name"  # 特征名称
        FEATURE_TAGS = "tags"  # 特征标签

        def __init__(self, init_params):
            super(Test, self).__init__(init_params)

        def process(self, monitor_data_obj=None):
            return "12345"


    @register.register_solution(app_name="test_app1", instance_name="1233", solution_name="sol1")
    class Test1(BaseFeatureOperator):
        FEATURE_NAME = "nam2e"  # 特征名称
        FEATURE_TAGS = "tags4"  # 特征标签

        def __init__(self, init_params):
            super(Test1, self).__init__(init_params)

        def process(self, monitor_data_obj=None):
            return "23456"


    data = MonitorData(data=123, monitor_key=345)
    result = register.call_function(init_params={}, solution_name="sol", monitor_data_obj=data)
    print(result)
