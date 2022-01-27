# ACM 호텔
import sys

t = int(sys.stdin.readline().strip())
for i in range(t): 
    h, w, n = map(int, sys.stdin.readline().strip().split()) # h = 전체 층 수, w = 각 층당 방 수, n = n 번째 손님
    yy = h if n % h == 0 else n % h
    xx = n // h if n % h == 0 else n // h + 1
    result = str(yy) + str(xx).zfill(2)
    print(result)