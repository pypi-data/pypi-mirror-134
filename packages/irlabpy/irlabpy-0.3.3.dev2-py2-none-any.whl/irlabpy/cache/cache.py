# !/usr/bin/env python
# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Cache(metaclass=ABCMeta):

    @abstractmethod
    def query_metrics_with_time_window(self, table, tags, start, end, tenant='default'):
        pass

    @abstractmethod
    def _expire(self, table, tags, tenant='default', ex_time=25 * 60 * 60):
        pass

