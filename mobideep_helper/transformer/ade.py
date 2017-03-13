# -*- coding: utf-8 -*-

import struct

from . import Transformer


class TextToBinaryTransformer(Transformer):
    def __init__(self, config):
        Transformer.__init__(self, config)
        self.semcode_size = config['semcode_size'] + 1
        self.vector_max_size = config['vector_max_size'] + 1
        self.hdr_schema = '2i%dfB2I' % (self.semcode_size)
        self.data_schema = ('%df%dbfBi' % (self.vector_max_size, self.vector_max_size)) * 2
        self.schema = self.hdr_schema + self.data_schema

        self.sem = [0 for i in xrange(self.semcode_size + 3)]
        self.attr = [0 for i in xrange(self.vector_max_size + 2)]

    def transform(self, data, delimiter=','):
        data = data.split(';')  # 현재 데이터 ; 과거 데이터 형태의 데이터
        in_data = map(lambda x: float(x), data[0].split(delimiter)[2:])   # 과거 데이터
        out_data = map(lambda x: float(x), data[1].split(delimiter)[2:])  # 현재 데이터

        in_len = len(in_data)
        out_len = len(out_data)
        hdr = [in_len, out_len]

        final_data = hdr + self.sem + \
                     in_data + [0.0] + self.attr + [in_len] + \
                     out_data + [0.0] + self.attr + [out_len]
        return struct.pack(self.schema, *final_data)