# -*- coding: utf-8 -*0

from .common import get_config
from .common import getclass


# 기본적인 Runner
class Runner:
    def __init__(self, config):
        # 전역 설정
        self.global_config = get_config(config)

        # Reader, Writer, Partitioner 각각의 설정을 가져온다.
        self.r_config = self.global_config['reader']
        self.w_config = self.global_config['writer']
        self.p_config = self.global_config['partitioner']
        self.t_config = self.global_config['transformer']

        # 각각의 클래스 객체를 가져옴
        self.reader_cls = getclass(self.r_config['cls'])
        self.writer_cls = getclass(self.w_config['cls'])
        self.partitioner_cls = getclass(self.p_config['cls'])
        self.transformer_cls = getclass(self.t_config['cls'])

        # 읽고 쓰기 위한 Reader, Partitioner를 생성
        # Writer의 경우 파티션 별로 저장을 하기 위해 run메소드에서 여러개를 생성
        self.reader = self.reader_cls(self.r_config)
        self.partitioner = self.partitioner_cls(self.p_config)
        self.transformer = self.transformer_cls(self.t_config)

    # mobideep_helper를 수행하는 메소드
    def run(self, source):
        self.reader.open(source)

        # Partitioner로부터 파티션 정보를 획득하고 Writer Dictionary를 만든다.
        writer_dict = {}
        partitions = self.partitioner.get_partitions()
        for partition in partitions:
            writer_dict[partition] = self.writer_cls(self.w_config)
            writer_dict[partition].open('%s_%s' % (source, str(partition)))

        while True:
            # Reader로부터 데이터를 읽는다.
            data = self.reader.read()
            if not data:
                break

            # 파티션별로 데이터를 쓴다.
            for part, _data in self.partitioner.partition(data):
                _data = self.transformer.transform(_data)
                writer_dict[part].write(_data)

        # 파티션별로 연결을 끊는다. (fd의 경우 해당 절차가 있어야 파일에 정상적으로 Flush됨)
        for part, _writer in writer_dict.items():
            _writer.close()
            print 'writing success partition: %s' % (str(part))

        print 'success'