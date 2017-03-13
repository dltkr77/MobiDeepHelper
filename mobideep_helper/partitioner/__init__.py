# -*- coding: utf-8 -*-


# 파티셔너 인터페이스
class Partitioner:
    def __init__(self, config):
        self.config = config

    # 파티션 정보를 리스트로 리턴해야 함
    def get_partitions(self):
        raise NotImplementedError

    # 데이터가 전달되면 적절히 파티셔닝하여 리턴
    def partition(self, data):
        raise NotImplementedError

    def set(self, key, value):
        self.config[key] = value

    def get(self, key):
        return self.config[key]