# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input().strip())
meetings = [list(map(int, input().strip().split())) for _ in range(N)]

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# meetings = [list(map(int, f.readline().strip().split())) for _ in range(N)]

meetings.sort(reverse= True, key= lambda x: (x[0], x[1]))
count = 1; start = meetings[0][0]
print(meetings)
for i in range(1, N):
    if start >= meetings[i][1]:
        count += 1
        start = meetings[i][0]
print(count)

# 시간초과: 완전탐색에 더 가까운 듯
# meetings.sort(key= lambda x: x[0])
# count = [1 for _ in range(N)]

# for i, v in enumerate(meetings):
#     e = v[1]
#     for j in range(i + 1, N):
#         if meetings[j][0] >= e:
#             count[i] += 1
#             e = meetings[][1]

# print(max(count))