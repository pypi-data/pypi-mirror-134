import hashlib

import mmh3
import logging
import datetime
import re


def sort_dict_by_key(data: dict, reverse=False):
    """
    对字典按key排序
    :param data: dict数据
    :param reverse: True表示按key降, 默认False表示按key升序
    :return:
    """
    if data is None:
        return None

    new_dict = {}
    for k in sorted(data.keys(), reverse=reverse):
        new_dict[k] = data[k]
    return new_dict


def hash_by_murmur(content: str):
    """
    使用Murmur算法计算hash值
    :param content:
    :return:
    """
    # return mmh3.hash128(content)
    return mmh3.hash(content, seed=-1)


def get_public_attrs(obj):
    """
    获取对象中用户自定义的属性名称和属性值
    :param obj:
    :return:
    """
    names = dir(obj)
    attr_value_dict = {}
    for name in names:
        # 内置的成员变量和方法排除
        if name.startswith("__"):
            continue
        # 排除方法
        if type(getattr(obj, name)).__name__ == "function":
            continue
        attr_value_dict[name] = getattr(obj, name)
    return attr_value_dict


def get_feature_task_timestamps(zark_solution_params):
    """ 获得特征任务的时间戳
    :param zark_solution_params: zark solution的输入参数
    :return: 本次任务的开始时间戳和结束时间戳
    """
    class ErrorTimeStamps:
        """
        错误输入时的起止时间戳
        """
        def __init__(self):
            pass

        @staticmethod
        def error_start_end_timestamp():
            now_time = datetime.datetime.now()
            now_timestamp = str(int(now_time.timestamp() * 1000))
            return now_timestamp, now_timestamp

    def read_time_clock(time_str: str):
        """
        解析 12:04:32 型的输入数据
        """
        # 不指定结束时间，默认为当前时间
        if time_str == "0":
            return datetime.datetime.now()
        else:
            yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)
            try:
                time = datetime.datetime.strptime(time_str, "%H:%M:%S")
                time = time.replace(microsecond=999999)
                end_time = datetime.datetime.combine(yesterday.date(), time.time())
                return end_time
            except ValueError as e:
                logging.error("%s: invalid end_time." % e)
                return datetime.datetime.now()

    def read_timedelta(timedelta_str: str):
        """
        解析时间区间长度：hh=24或dd=1
        """
        kv = re.split("=", timedelta_str)
        if len(kv) != 2:
            logging.error("invalid time_delta.")
            return None
        try:
            data = int(kv[1])
        except ValueError as e:
            logging.error("%s: invalid value for %s." % (e, kv[0]))
            return None
        if data < 0:
            logging.error("time_delta cannot be negative.")
            return None

        if kv[0] == 'hh':
            delta = datetime.timedelta(hours=data)
            return delta
        elif kv[0] == 'dd':
            delta = datetime.timedelta(days=data)
            return delta
        else:
            logging.error("invalid time interval of %s." % kv[0])
            return None

    try:
        start_timestamp = zark_solution_params['start_timestamp']
        end_timestamp = zark_solution_params['end_timestamp']
        time_delta_str = zark_solution_params['time_delta']
        end_time_str = zark_solution_params['end_time']
    except KeyError as e:
        logging.error("%s: no such key." % e)
        return ErrorTimeStamps.error_start_end_timestamp()

    # 单次特征任务，固定起止时间戳
    if start_timestamp != "0" and end_timestamp != "0":
        return start_timestamp, end_timestamp
    # 非法起止时间戳
    elif start_timestamp != "0" or end_timestamp != "0":
        logging.error("invalid start_timestamp and end_timestamp")
        return ErrorTimeStamps.error_start_end_timestamp()
    # 定时任务，定义时间区间长度和区间右端点
    else:
        end_time = read_time_clock(end_time_str)
        time_delta = read_timedelta(time_delta_str)
        if time_delta is None:
            return ErrorTimeStamps.error_start_end_timestamp()
        start_time = end_time - time_delta
        start_timestamp = str(int(start_time.timestamp() * 1000))
        end_timestamp = str(int(end_time.timestamp() * 1000))
        return start_timestamp, end_timestamp


def _get_md5(s):
    md = hashlib.md5()
    md.update(s.encode('utf-8'))
    return md.hexdigest()


def get_key_by_datasource(table, tags, tenant):
    tags_list = []
    keys = sorted(tags)
    for k in keys:
        tags_list.append('%s=%s' % (k, tags[k]))
    k = ', '.join(tags_list)
    k = '{%s}' % k
    s = table + k + tenant
    return _get_md5(s)


if __name__ == '__main__':
    init_params = {
        'start_timestamp': '0',
        'end_timestamp': '0',
        'time_delta': 'hh=3',
        'end_time': '23:45:34',
    }
    st, et = get_feature_task_timestamps(init_params)
    print(st, et)
