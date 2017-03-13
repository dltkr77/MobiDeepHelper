# -*- coding: utf-8 -*-

from . import Reader


# 일반적인 텍스트 파일을 읽는 Reader
class FileReader(Reader):
    def __init__(self, config):
        Reader.__init__(self, config)

        # 한 번에 반환하는 라인 수
        self.max_count = self.config['max_count'] \
            if 'max_count' in self.config else 10000

        # CSV와 같이 헤더가 있을 경우 처리
        self.started = False

    def open(self, source):
        self.fd = open(source, 'r')

    def read(self):
        # 헤더가 있을 경우 한 줄을 그냥 읽기
        if not self.started and self.config['header']:
            self.fd.readline()
        self.started = True

        # 최대치만큼 읽어서 반환
        result = []
        for i in xrange(self.max_count):
            data = self.fd.readline()
            if not data:
                break
            result.append(data)

        return result

    def close(self):
        self.fd.close()
        self.started = False