# 블랙잭
import sys

# 블랙잭: 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임

# 첫째 줄에 카드의 개수 N(N은 3 이상 100 이하)과 M(M은 10 이상 30만 이하)이 주어진다.
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000 이하의 양의 정수이다.
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

n, m = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

maxSum = 0
for i in range(n - 2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
            case = cards[i] + cards[j] + cards[k]
            maxSum = case if case <= m and case > maxSum else maxSum
print(maxSum)