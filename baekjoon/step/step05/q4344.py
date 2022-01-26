import sys
from functools import *

def q4344():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, sys.stdin.readline().strip().split()))
        n = arr.pop(0)
        aver = sum(arr) / n
        result = reduce(lambda acc, cur: acc + 1 if cur > aver else acc + 0, arr, 0) / n * 100
        print("{:.3f}%".format(result))
    
q4344()