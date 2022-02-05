# 피보나치 함수
import sys
input = sys.stdin.readline

# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

T = int(input().strip())
count = [None for _ in range(41)]
count[0] = [1, 0]
count[1] = [0, 1]
n = 2

for _ in range(T):
    N = int(input().strip())
    if count[N] is not None:
        print(count[N][0], count[N][1])
        continue
    for i in range(n, N + 1):
        count[i] = [count[i - 1][0] + count[i - 2][0], count[i - 1][1] + count[i - 2][1]]
    n = N + 1
    print(count[N][0], count[N][1])

# 1. 피보나치 함수 그대로 사용, 시간초과 :)
# T = int(input().strip())
# count0, count1 = 0, 0

# def fibonacci(num):
#     global count0, count1
#     if num == 0:
#         count0 += 1
#         return 0
#     elif num == 1:
#         count1 += 1
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)

# for _ in range(T):
#     n = int(input().strip())
#     fibonacci(n)
#     print(f"{count0} {count1}")
#     count0, count1 = 0, 0