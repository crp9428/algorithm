# 소수
import sys
import math

# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

def isPrime(n):
    if n == 1:
        return False
    ii = math.ceil(n / 2) + 1
    for i in range(2, ii):
        if n % i == 0:
            return False
    return True
    
M = int(sys.stdin.readline().strip()); N = int(sys.stdin.readline().strip())
arr = []
for i in range(M, N + 1):
    if isPrime(i) is True:
        arr.append(i)
        
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))