MobiDeep Helper
===============

제한된 볼츠만 머신(Restricted Boltzmann Machine)을 기반으로 하는 심층 신뢰 신경망인 `MobiDeep` 엔진의 사용을 돕기 위한 헬퍼 모듈

## 구조
Source --> Reader --> Partitioner --> Transformer --> Writer -> Destination

* Reader
	* 특정 소스로부터 데이터를 읽는 역할 수행
	* 리스트를 반환해야 함	
* Partitioner
	* Reader로부터 데이터를 전달받아 해당 데이터를 적절히 나누어주는 역할
	* 데이터를 특정 기준으로 분리시키기 위함
* Transformer
    * Partitioner가 파티셔닝된 데이터를 전달하면, 적절히 변환하는 역할 수행
    * Text파일을 바이너리로 만들거나, 기타 변환 작업을 수행
* Writer
	* 최종 데이터를 전달하면 저장하는 역할 수행

## Build
```
$ python setup.py sdist
```

## Installation
`dist` 디렉토리 밑의 모듈을 배포 후, 아래와 같이 설치
```
$ pip install mobideep_helper-0.0.2.tar.gz
```

## Uninstallation
```
$ pip uninstall mobideep_helper
```

## Usage
```
$ mobideep_run -h
usage: mobideep_run [-h] [--config CONFIG] source

positional arguments:
  source           data source

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  mobideep_helper config file
```

* source
	* 헬퍼로 전달할 데이터소스
	* 현재는 파일을 지원하나, Connector 및 Reader의 구현을 통해 HDFS, FTP등을 지원 예정
* config
	* Mobideep Helper의 설정파일
	* 기본으로 File로부터 읽고 쓰는 설정이 적용됨
	
## Configuration Example
```
$ cat etc/example.yml
mobideep_helper:
  reader:
    cls: 'mobideep_helper.reader.slide.SlidingFileReader'
    header: true
    window_size: 14
  writer:
    cls: 'mobideep_helper.writer.file.FileWriter'
    option: 'a'
    destination: '/tmp/mobideep/data'
    prefix: 'mobideep_helper'
    partition_dir: true
  partitioner:
    cls: 'mobideep_helper.partitioner.fibo.FibonacciPartitioner'
    fibonacci_length: 6
  transformer:
    cls: 'mobideep_helper.transformer.ade.TextToBinaryTransformer'
    semcode_size: 16
    vector_max_size: 16
```
