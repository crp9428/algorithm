# 한수
import sys

# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

def isAP(n):
    a = n // 100; b = (n - a * 100) // 10; c = (n - a * 100 - b * 10)
    return (c - b == b - a) or (a - b == b - c)

N = int(sys.stdin.readline().strip())
count = 99 if N > 99 else N
for i in range(100, N + 1):
    if isAP(i) is True:
        count += 1
        
print(count)