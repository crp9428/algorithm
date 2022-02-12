# 쉬운 계단 수
import sys
input = sys.stdin.readline

# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
# 0으로 시작하는 수는 계단수가 아니다.
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

N = int(input().strip())
stairs = [[0 for _ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    stairs[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            stairs[i][0] = stairs[i - 1][1]
        elif j == 9:
            stairs[i][9] = stairs[i - 1][8]
        else:
            stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]

print(sum(stairs[N]) % 1000000000)