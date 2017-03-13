# -*- coding: utf-8 -*-

import struct

from . import Transformer


class TextToBinaryTransformer(Transformer):
    def __init__(self, config):
        Transformer.__init__(self, config)

        # Sementic Code와 관련된 설정
        # Transformer의 입장에서는 모든 값을 0으로 채우면 됨.
        # +1인 이유는 마지막 빈 값
        self.semcode_size = config['semcode_size'] + 1

        # 벡터의 최대 크기
        # +1인 이유는 마지막 빈 값
        self.vector_max_size = config['vector_max_size'] + 1

        # 헤더를 쓰기 위한 Struct Format
        # in_cnt, out_cnt, semcodes, type, wisdom, energy
        self.hdr_schema = '2i%dfB2I' % (self.semcode_size)

        # 데이터를 쓰기 위한 Struct Format
        # 벡터의 모든 값, 벡터의 모든 Attributes, entropy, type, sz
        # 과거 데이터와 현재 데이터, 두 가지가 필요하므로 같은 Format이 2회 반복됨.
        self.data_schema = ('%df%dbfBi' % (self.vector_max_size, self.vector_max_size)) * 2

        # 헤더와 데이터를 쓰기 위한 Struct Format을 합친 문자열
        self.schema = self.hdr_schema + self.data_schema

        # 각각 Sementic Code 값과 Attribute 값을 0으로 초기화한다.
        self.sem = [0 for i in xrange(self.semcode_size + 3)]
        self.attr = [0 for i in xrange(self.vector_max_size + 2)]

    def transform(self, data, delimiter=','):
        # <현재 데이터>;<과거 데이터>를 분리한다.
        data = data.split(';')

        # ADE 데이터의 앞의 2개 필드는 사용하지 않는다.
        # in_data = 과거 데이터
        # out_data = 현재 데이터
        in_data = map(lambda x: float(x), data[0].split(delimiter)[2:])
        out_data = map(lambda x: float(x), data[1].split(delimiter)[2:])  # 현재 데이터

        # 헤더를 만들기 위해 각각 사이즈를 잰다.
        in_len = len(in_data)
        out_len = len(out_data)
        hdr = [in_len, out_len]

        # 모든 값을 바이너리로 만들어서 반환
        final_data = hdr + self.sem + \
                     in_data + [0.0] + self.attr + [in_len] + \
                     out_data + [0.0] + self.attr + [out_len]
        return struct.pack(self.schema, *final_data)