# 셀프 넘버
import sys

def d(n):
    result = n
    while(n > 0):
        result += (n % 10)
        n = n // 10
    return result
        

length = 10001
arr = [True for _ in range(length)]
arr[0] = False

for i in range(length):
    if i is False:
        continue
    num = d(i)
    if num < length and arr[num] is True:
        arr[num] = False

for i, v in enumerate(arr):
    if v is True:
        print(i)