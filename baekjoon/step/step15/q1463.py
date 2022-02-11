# 1로 만들기
import sys
input = sys.stdin.readline

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1을 뺀다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

N = int(input().strip()); 
if N == 1: 
    print(0); exit()
elif N == 2 or N == 3:
    print(1); exit()
    
count = [31 for _ in range(10**6 + 1)] # sys.maxsize
count[0] = 0; count[1] = 0; count[2] = 1; count[3] = 1

for i in range(4, N + 1):
    if i % 3 == 0:
        count[i] = min(count[i//3], count[i-1]) + 1
    if i % 2 == 0:
        count[i] = min(min(count[i//2], count[i-1]) + 1, count[i])
    count[i] = min(count[i], count[i-1] + 1)

print(count[N])
