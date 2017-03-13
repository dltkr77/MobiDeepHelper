# -*- coding: utf-8 -*-

import os
import sys

from . import Writer


# 파일로 데이터를 쓰기위한 클래스
class FileWriter(Writer):
    def __init__(self, config):
        Writer.__init__(self, config)

    def open(self, destination):
        # destination 설정이 되어 있어야 한다. (파일을 쓰기 위한 디렉토리명)
        # 인자로 전달된 Destination은 파티션 결과
        if 'destination' not in self.config:
            print >> sys.stderr, \
                'FileWriter: destination attribute is not found'
            raise AttributeError

        # prefix 설정이 있을 경우, '_'로 연결한다.
        if 'prefix' in self.config:
            destination = '_'.join(os.path.join(self.config['prefix'],
                                                str(destination)).split('/'))

        # 최종 저장할 destination을 정한다.
        destination = os.path.join(self.config['destination'], destination)
        self.fd = open(destination, self.config['option'])

    def write(self, data):
        # 리스트일 경우 스트링으로 변환하여 쓴다.
        if isinstance(data, list):
            data = ''.join(data)

        self.fd.write(data)

    def close(self):
        self.fd.close()