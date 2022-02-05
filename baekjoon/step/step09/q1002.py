# 터렛
import sys
import math

# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
# 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. 
# x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, 
# r1, r2는 10,000보다 작거나 같은 자연수이다.

# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 
# 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

T = int(sys.stdin.readline().strip())
result = 0
for tt in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    if distance == 0 and r1 == r2: # 동심원
        result = -1
    elif distance == r1 + r2: # 외접
        result = 1
    elif distance == abs(r1 - r2): # 내접
        result = 1
    elif abs(r1 - r2) < distance < (r1 + r2): # 두 점에서 만나는 경우
        result = 2
    else: # 만나지 않는 경우
        result = 0
    print(result)