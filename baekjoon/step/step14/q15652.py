# N과 M (4)
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
visit = [[False] * N for _ in range(M)]
arr = [0] * M

def dfs(n, depth):
    if depth == M:
        print(" ".join(str(v) for v in arr))
        return
    
    for i in range(n, N + 1):
        if visit[depth][i - 1]: continue
        visit[depth][i - 1] = True
        arr[depth] = i
        dfs(i, depth + 1)
        visit[depth][i - 1] = False

dfs(1, 0)