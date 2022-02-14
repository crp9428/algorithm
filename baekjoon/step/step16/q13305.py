# 주유소
from sys import stdin
input = stdin.readline

N = int(input().strip())
roads = list(map(int, input().strip().split()))
cost = list(map(int, input().strip().split()))

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# roads = list(map(int, f.readline().strip().split()))
# cost = list(map(int, f.readline().strip().split()))
cost.pop()

result = 0; minCost = cost[0]; d = roads[0]
for n in range(1, N - 1):
    if minCost > cost[n]:
        result += (minCost * d)
        minCost = cost[n]
        d = roads[n]
    else:
        d += roads[n]
        
result += (minCost * d)

print(result)