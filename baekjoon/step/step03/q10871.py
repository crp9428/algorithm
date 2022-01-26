import sys

def q10871():
    n, x = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    for i, v in enumerate(arr):
        if v < x:
            print(v, end=' ')

q10871()