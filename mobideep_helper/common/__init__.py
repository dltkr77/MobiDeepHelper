# -*- coding: utf-8 -*-

import yaml

# 설정파일을 전달하지 않았을 경우 기본으로 사용되는 설정
DEFAULT_CONF = {
    'mobideep_helper': {
        'reader': {
            'cls': 'mobideep_helper.reader.file.FileReader',
            'header': True
        },
        'writer': {
            'cls': 'mobideep_helper.writer.file.FileWriter',
            'destination': '/tmp',
            'prefix': 'mobideep_helper',
            'option': 'a'
        },
        'partitioner': {
            'cls': 'mobideep_helper.partitioner.test.RawPartitioner'
        },
        'transformer': {
            'cls': 'mobideep_helper.transformer.Transformer'
        }
    }
}


# 클래스를 동적으로 생성하기 위해, 클래스 정보를 얻는 함수
def getclass(classpath):
    components = classpath.split('.')
    modulepath = '.'.join(components[:-1])
    classname = components[-1]
    module = __import__(modulepath, fromlist=[classname])
    return getattr(module, classname)


# YAML 파일로부터 설정을 읽어들이는 함수
def get_config(config_path):
    if config_path is None:
        conf = DEFAULT_CONF
    else:
        conf = yaml.load(open(config_path, 'r'))
    if 'mobideep_helper' not in conf:
        raise AttributeError

    return conf['mobideep_helper']
