# N과 M (3)
import sys
input = sys.stdin.readline

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

N, M = map(int, input().strip().split())
visit = [[False] * N for _ in range(M)]
arr = [0] * M

def dfs(depth):
    if depth == M:
        print(" ".join(str(v) for v in arr))
        return

    for i in range(N):
        if visit[depth][i]: continue
        visit[depth][i] = True
        arr[depth] = i + 1
        dfs(depth + 1)
        visit[depth][i] = False

dfs(0)
