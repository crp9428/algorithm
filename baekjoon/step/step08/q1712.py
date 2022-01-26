# 손익분기점

import sys
import math

# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 21억 이하의 자연수이다.
# 첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 손익분기점이 존재하지 않으면 -1을 출력한다.

# A: 고정비용, B: 가변비용, C: 판매가

a, b, c = map(int, sys.stdin.readline().strip().split())
bep = -1 if c <= b else (int(a / (c - b)) + 1 if a % (c - b) == 0 else int(math.ceil(a / (c - b))))
print(bep)

