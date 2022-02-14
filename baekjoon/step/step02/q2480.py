# 주사위 세개
from sys import stdin
input = stdin.readline

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

dice = list(map(int, input().strip().split()))
reward = 0

if dice[0] == dice[1] == dice[2]:
    reward = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[0] == dice[2]:
    reward = 1000 + dice[0] * 100
elif dice[1] == dice[2]:
    reward = 1000 + dice[1] * 100
else:
    reward = max(dice) * 100

print(reward)