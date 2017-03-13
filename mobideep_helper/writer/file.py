# -*- coding: utf-8 -*-

import os
import sys

# from . import Writer
from mobideep_helper.writer import Writer


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

        if self.config.get('partition_dir', False):
            dir = str(destination)
        else:
            dir = ''

        # prefix 설정이 있을 경우, '_'로 연결한다.
        if 'prefix' in self.config:
            destination = '_'.join(os.path.join(self.config['prefix'],
                                                str(destination)).split('/'))

        # 최종 저장할 디렉토리가 없을 경우 생성
        dir = os.path.join(self.config['destination'], dir)
        if not os.path.exists(dir):
            os.makedirs(dir)

        # 최종 저장할 destination을 정한다.
        destination = os.path.join(dir, destination)

        # 파일을 쓰는 옵션에 따라서 write 메소드를 변경한다.
        if 'b' in self.config['option']:
            self.write = self._write_binary
        else:
            self.write = self._write_text

        # 쓰기 위해 파일을 오픈
        self.fd = open(destination, self.config['option'])

    def write(self, data):
        raise NotImplementedError('Write method is not defined')

    # 텍스트 파일을 쓰는 메소드
    def _write_text(self, data):
        if isinstance(data, list):
            data = ''.join(data)
        self.fd.write(data)

    # 바이너리 파일을 쓰는 메소드
    def _write_binary(self, data):
        if isinstance(data, list):
            for d in data:
                self.fd.write(d)
        else:
            self.fd.write(data)

    def close(self):
        self.fd.close()