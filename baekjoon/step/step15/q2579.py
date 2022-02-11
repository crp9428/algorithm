# 계단 오르기
from sys import stdin
input = stdin.readline

# 입력의 첫째 줄에 계단의 개수가 주어진다. (계단의 개수는 300이하의 자연수이다.)
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. (계단에 쓰여 있는 점수는 10,000이하의 자연수이다.)
# i번째 계단에 오를 때, 몇 개의 연속한 계단을 올랐는지를 고려하여 부분문제를 정의해봅시다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

N = int(input().strip())
stairs = [0] + [int(input().strip()) for _ in range(N)]

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# stairs = [0] + [int(f.readline().strip()) for _ in range(N)]

result = [0 for _ in range(N + 1)]
result[1] = stairs[1]
if N >= 2: result[2] = max(result[1] + stairs[2], stairs[2])
if N >= 3: result[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N + 1):
    result[i] = max(result[i-2] + stairs[i], result[i-3] + stairs[i-1] + stairs[i])

print(result[N])