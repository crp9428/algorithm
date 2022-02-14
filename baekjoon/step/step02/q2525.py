# 오븐 시계
from sys import stdin
input = stdin.readline

A, B = map(int, input().strip().split())
C = int(input().strip())

result = [A, B]
result[1] += C
if result[1] > 59:
    result[0] += result[1] // 60
    result[1] = result[1] % 60
if result[0] >= 24:
    result[0] -= 24
    
print(f"{result[0]} {result[1]}")