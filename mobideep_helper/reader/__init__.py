# -*- coding: utf-8 -*-


# 데이터소스로부터 읽기 위한 인터페이스
class Reader:
    def __init__(self, config):
        self.config = config

    # 커넥션 등 연결
    def open(self, source):
        raise NotImplementedError

    # 데이터를 읽어들인다. 리스트로 반환할 것.
    def read(self):
        raise NotImplementedError

    # 커넥션 등을 해제
    def close(self):
        raise NotImplementedError

    def set(self, key, value):
        self.config[key] = value

    def get(self, key):
        return self.config[key]