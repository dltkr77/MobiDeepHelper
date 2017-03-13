# -*- coding: utf-8 -*-

from . import Partitioner


# 테스트를 위해 0, 1 두가지로 반환하는 클래스
class RawPartitioner(Partitioner):
    def __init__(self, config):
        Partitioner.__init__(self, config)

    def get_partitions(self):
        return [0, 1]

    def partition(self, data):
        length = len(data)/2
        return [(0, data[0:length]), (1, data[length:])]