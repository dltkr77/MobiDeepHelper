# -*- coding: utf-8 -*-

from . import Partitioner


# 피모나치 수열로 파티셔닝을 하기 위한 클래스
class FibonacciPartitioner(Partitioner):
    def __init__(self, config):
        Partitioner.__init__(self, config)

        # 피보나치 숫자를 뽑을 개수
        self.length = self.config['fibonacci_length']

        # 피모나치 수열
        self.fibo = self._fibonacci(self.length)

        # 과거 데이터와 조인을 하기 위한 피보나치 수열(각 요소마다 +1한 값)
        self.len_fibo = map(lambda x: x + 1, self.fibo)

    # 파티션 정보를 반환. 피보나치 수열을 그대로 반환한다.
    def get_partitions(self):
        return self.fibo

    # 피보나치 수열을 연산해주는 메소드
    # 단, [1, 2, 3]과 같이 중복되는 값이 없어야 한다.
    def _fibonacci(self, x):
        result = [1, 2]
        for i in xrange(2, x):
            result.append(result[i-1] + result[i-2])
        return result

    def partition(self, data):
        index = self._needs_count(len(data))

        # (파티션, "현재 데이터;과거 데이터") 형태로 반환
        return map(lambda x: (x, '%s;%s' % (data[-1].strip(), data[-(x+1)])), self.fibo[:index])

    # 데이터가 피보나치 수열보다 적은 경우를 위해 계산
    def _needs_count(self, data_length):
        # 인덱스를 찾아낸다.
        i = 0
        for i in xrange(self.length):
            if data_length < self.len_fibo[i]:
                break

        # 마지막 배열까지 접근하기 위함
        if data_length >= self.len_fibo[-1]:
            i += 1

        return i