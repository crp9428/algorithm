# 01타일
from sys import stdin
input = stdin.readline

# 첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.

N = int(input().strip())
def main():
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(2)
        return
    
    a = 1; b = 2; sum = 0
    for i in range(3, N + 1):
        sum = (a + b) % 15746
        a = b
        b = sum
    print(sum)

main()