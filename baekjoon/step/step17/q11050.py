# 이항 계수 1
import sys
import math
input = sys.stdin.readline

N, K = map(int, input().strip().split())
result = math.factorial(N) // (math.factorial(N - K) * math.factorial(K))
print(result)