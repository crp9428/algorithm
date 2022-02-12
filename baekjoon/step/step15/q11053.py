# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().strip().split()))

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# nums = list(map(int, f.readline().strip().split()))

LIS = [nums[0]]

def lower_bound(arr, n):
    for i, v in enumerate(arr):
        if v == n or v > n:
            return i
    return len(arr) - 1

for i in range(1, N):
    if nums[i] > LIS[-1]:
        LIS.append(nums[i])
    elif nums[i] < LIS[-1]:
        LIS[lower_bound(LIS, nums[i])] = nums[i]
print(len(LIS))