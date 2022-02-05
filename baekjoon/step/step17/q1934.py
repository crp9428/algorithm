# 최소공배수
import sys
input = sys.stdin.readline

# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

def getGcd(a, b): # 재귀 방식 사용
    if b == 0:
        return a
    else:
        return getGcd(b, a % b)
        
T = int(input().strip())
for _ in range(T):
    nums = list(map(int, input().strip().split()))
    lcm = nums[0] * nums[1] // getGcd(max(nums), min(nums))
    print(lcm)
    