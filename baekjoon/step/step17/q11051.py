# 이항 계수 2
import sys
input = sys.stdin.readline

# N개중 K개를 뽑는 경우의 가짓수
N, K = map(int, input().strip().split())
check = [[0 for k in range(K + 1)] for n in range(N + 1)]
for n in range(N + 1):
    check[n][0] = 1
    try:
        check[n][n] = 1
    except IndexError:
        continue

for n in range(1, N + 1):
    for k in range(1, K + 1):
        check[n][k] = check[n - 1][k] + check[n - 1][k - 1]

print(check[N][K] % 10007)