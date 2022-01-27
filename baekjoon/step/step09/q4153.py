# 직각삼각형
import sys 

# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 
# 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
# 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

while(True):
    tri = list(map(int, sys.stdin.readline().strip().split()))
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    maxIdx = tri.index(max(tri))
    isRT = False
    if maxIdx == 0:
        isRT = tri[1]**2 + tri[2]**2 == tri[0]**2
    elif maxIdx == 1:
        isRT = tri[0]**2 + tri[2]**2 == tri[1]**2
    elif maxIdx == 2:
        isRT = tri[0]**2 + tri[1]**2 == tri[2]**2
    
    print("right") if isRT else print("wrong")