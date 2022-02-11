# RGB거리
import sys
input = sys.stdin.readline

# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

# N = int(input().strip())
f = open("input.txt", "r")
N = int(f.readline().strip())
case = []
for n in range(N):
    # case.append(list(map(int, input().strip().split())))
    case.append(list(map(int, f.readline().strip().split())))

for i in range(1, len(case)):
    case[i][0] += min(case[i-1][1], case[i-1][2])
    case[i][1] += min(case[i-1][0], case[i-1][2])
    case[i][2] += min(case[i-1][0], case[i-1][1])
    
print(min(case[N-1]))

# 시간초과..
# # f = open("input.txt", "r")
# N = int(input().strip())
# # N = int(f.readline().strip())
# cph = []
# for n in range(N):
#     cph.append(list(map(int, input().strip().split())))
#     # cph.append(list(map(int, f.readline().strip().split())))

# case = []; visit = [[False] * 3 for _ in range(N)]; arr = [0] * N; costs = []

# def dfs(depth):
#     if depth == N:
#         cost = 0
#         for i, v in enumerate(arr):
#             cost += cph[i][v]
#         costs.append(cost)
#         return

#     for i in range(3):
#         if visit[depth][i]: continue
#         visit[depth][i] = True;
#         if depth < N - 1: visit[depth+1][i] = True;
#         arr[depth] = i
#         dfs(depth + 1)
#         visit[depth][i] = False
#         if depth < N - 1: visit[depth+1][i] = False;
# dfs(0)

# print(min(costs))