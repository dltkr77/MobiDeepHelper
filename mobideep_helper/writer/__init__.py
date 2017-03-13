# -*- coding: utf-8 -*-


# 데이터를 쓰기 위한 인터페이스
class Writer:
    def __init__(self, config):
        self.config = config

    # 커넥션 등 연결
    def open(self, destination):
        raise NotImplementedError

    # 데이터를 쓴다
    def write(self, data):
        raise NotImplementedError

    # 커넥션 등 해제
    def close(self):
        raise NotImplementedError

    def set(self, key, value):
        self.config[key] = value

    def get(self, key):
        return self.config[key]