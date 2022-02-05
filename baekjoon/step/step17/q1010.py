# 다리 놓기
import sys
input = sys.stdin.readline

T = int(input().strip())

def getCase(N, K):
    check = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for n in range(N + 1):
        check[n][0] = 1
        if n <= (K): check[n][n] = 1
    
    for n in range(1, N + 1):
        for k in range(1, K + 1):
            check[n][k] = check[n - 1][k] + check[n - 1][k - 1]
            
    return check[N][K]
    
for i in range(T):
    n, m = map(int, input().strip().split())
    print(getCase(m, n))