### v0.0.3

 * `ChainTransfomer` 추가. functions에 정의된 함수들을 연속적으로 호출하도록 설정할 수 있음
 * 파티셔닝시 기존 source의 이름과 파티션 정보를 Write 파일명으로 사용하도록 변경
 * `mobideep_run` 실행시 인자로 `--multi`를 줄 경우, Transform -> Write 과정이 병렬화 되도록 변경

### v0.0.2

 * FileWriter에서 특정 파티션명의 디렉토리로 파일을 모을 수 있는 `partition_dir` 옵션 추가
 * 파티셔닝이 완료된 데이터를 가공하는 `Transformer` 개념 추가
 * ADE 데이터를 파티셔닝하기 위한 `TextToBinaryTransformer` 추가

### v0.0.1

 * Reader, Writer, Partitioner 인터페이스 개발
 * 일반적인 텍스트 파일을 읽고 쓸 수 있도록 FileReader, FileWriter 개발
 * 테스트를 위한 RawPartitioner 개발
 * 피보나치 데이터를 만들기 위한 FibonacciPartitioner 개발
