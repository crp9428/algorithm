# 직사각형에서 탈출
import sys 

# 한수는 지금 (x, y)에 있다. 
# 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
# 입력 : x(x는 1 이상 w-1 이하), y(y는 1 이상 h-1 이하), w(w는 1 이상 1000 이하), h(h는 1 이상 1000 이하), x, y, w, h는 모두 정수

x, y, w, h = map(int, sys.stdin.readline().strip().split())
arr = [x, w - x, y, h - y] # x to 0, x to w, y to 0, w to h
print(min(arr))