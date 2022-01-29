# 소수 찾기
import sys
import math

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 주어진 수들 중 소수의 개수를 출력한다.

def isPrime(n):
    if n == 1:
        return False
    ii = math.floor(math.sqrt(n)) + 1
    for i in range(2, ii):
        if n % i == 0:
            return False
    return True

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
count = 0
for v in numbers:
    if isPrime(v) is True:
        count += 1

print(count)

