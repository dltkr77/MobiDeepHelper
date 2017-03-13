# -*- coding: utf-8 -*-

from .file import FileReader


# 특정 윈도우를 갖고 반환하는 Reader
class SlidingFileReader(FileReader):
    def __init__(self, config):
        FileReader.__init__(self, config)

        # window_size는 tic의 배수여야 한다.
        self.window_size = self.config['window_size'] \
            if 'window_size' in self.config else 130

        self.window = []
        self.started = False

    def read(self):
        # 처음 시작할 경우에는 윈도우를 가득 채운다.
        if not self.started and self.config['header']:
            self.started = True
            self.fd.readline()

        # 윈도우에 라인을 하나 추가
        data = self.fd.readline()
        if not data:
            return data
        self.window.append(data)

        # 윈도우 사이즈가 가득 찬 경우 Shift
        if len(self.window) > self.window_size:
            self.window = self.window[1:]

        return self.window

    def close(self):
        self.fd.close()
        self.started = False