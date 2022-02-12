# 포도주 시식
import sys
input = sys.stdin.readline

N = int(input().strip())
wines = [0] + [int(input().strip()) for _ in range(N)]

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# wines = [0] + [int(f.readline().strip()) for _ in range(N)]

result = [0 for _ in range(N + 1)]
result[0] = 0; result[1] = wines[1]
if N >= 2: result[2] = sum(wines[:3])
if N >= 3: result[3] = max(wines[1] + wines[2], wines[1] + wines[3], wines[2] + wines[3])
for i in range(4, N + 1):
    result[i] = max(result[i - 1], result[i - 2] + wines[i], result[i - 3] + wines[i - 1] + wines[i])
    
print(result[N])