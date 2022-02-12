# 연속합
import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().strip().split()))

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# nums = list(map(int, f.readline().strip().split()))

dp = [0 for _ in range(N)]
dp[0] = nums[0]

for i in range(1, N):
    if dp[i - 1] + nums[i] < nums[i]:
        dp[i] = nums[i]
    else:
        dp[i] = dp[i - 1] + nums[i]
        
print(max(dp))