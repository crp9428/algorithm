# 좌표 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] * N
for i in range(N):
    x, y = map(int, input().strip().split())
    arr[i] = [x, y]
arr.sort(key=lambda x: (x[1], x[0]))
for v in arr:
    print(f"{v[0]} {v[1]}")