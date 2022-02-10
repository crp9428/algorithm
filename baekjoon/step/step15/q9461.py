# 파도반 수열
from sys import stdin
input = stdin.readline

arr = [None for _ in range(100)]
arr[0], arr[1], arr[2] = 1, 1, 1
def setArr(n):
    if n <= 2:
        return 1
    elif arr[n] != None:
        return arr[n]
    else:
        arr[n] = setArr(n - 3) + setArr(n - 2)
        return arr[n]

T = int(input().strip())
for _ in range(T):
    n = int(input().strip()) - 1
    if arr[n] == None:
        setArr(n)
    print(arr[n])
    