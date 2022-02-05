# 링
import sys
import math
input = sys.stdin.readline

N = int(input().strip())
rings = list(map(int, input().strip().split()))

for i in range(1, N):
    gcd = math.gcd(rings[0], rings[i])
    print(f"{int(rings[0] / gcd)}/{int(rings[i] / gcd)}")
    