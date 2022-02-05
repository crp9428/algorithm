# 최대공약수와 최소공배수
import sys
import math
input = sys.stdin.readline

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
nums = list(map(int, input().strip().split()))

# 2. 파이썬에 최대공약수 최소공배수 구하는 함수 있음...
gcd = math.gcd(nums[0], nums[1]); lcm = math.lcm(nums[0], nums[1])
print(f"{gcd}\n{lcm}")

# 1. 유클리드 호제법 사용
# def getGcd(a, b):
#     while(b != 0):
#         r = a % b; a = b; b = r
#     return a

# gcd = getGcd(max(nums), min(nums)); lcm = int(nums[0] * nums[1] / gcd)
# print(f"{gcd}\n{lcm}")