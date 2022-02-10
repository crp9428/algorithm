# 스타트와 링크
import sys
input = sys.stdin.readline

# f = open("input.txt", "r")
N = int(input().strip())
# N = int(f.readline().strip())
status = list(list(map(int, input().strip().split())) for _ in range(N))
# status = list(list(map(int, f.readline().strip().split())) for _ in range(N))
cases = []; visit = [False for _ in range(N)]

def dfs1(n, depth):
    if depth == N // 2:
        team1 = []; team2 = []
        for i, v in enumerate(visit):
            if v is True: team1.append(i)
            else: team2.append(i)
        cases.append([team1, team2])
        return
    
    for i in range(n, N):
        if visit[i]: continue
        visit[i] = True
        dfs1(i, depth + 1)
        visit[i] = False
dfs1(0, 0)

statusCase = []; visit = [False for _ in range(N // 2)]
def dfs2(n, depth):
    if depth == 2:
        statusCase.append(visit.copy())
        return
    
    for i in range(n, N // 2):
        if visit[i]: continue
        visit[i] = True
        dfs2(i, depth + 1)
        visit[i] = False
dfs2(0, 0)

minstatus = sys.maxsize
for case in cases:
    team1 = case[0]; team2 = case[1]
    team1Status = 0; team2Status = 0
    for case in statusCase:
        idx1 = -1; idx2 = -1
        for i, b in enumerate(case):
            if b is False: continue
            if idx1 == -1: 
                idx1 = i
            else: 
                idx2 = i
                break
        team1Status += status[team1[idx1]][team1[idx2]] + status[team1[idx2]][team1[idx1]]
        team2Status += status[team2[idx1]][team2[idx2]] + status[team2[idx2]][team2[idx1]]
    
    if minstatus > abs(team1Status - team2Status):
        minstatus = abs(team1Status - team2Status)

print(minstatus)
# f.close()