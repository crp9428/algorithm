# 네 번째 점
import sys 

# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 
# 좌표는 1 이상 1000 이하의 정수이다.
x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())
x3, y3 = map(int, sys.stdin.readline().strip().split())

x = x3 if x1 == x2 else x2 if x1 == x3 else x1
y = y3 if y1 == y2 else y2 if y1 == y3 else y1

print(f"{x} {y}")