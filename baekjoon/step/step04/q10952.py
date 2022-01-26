import sys

def q10952():
    while(True):
        a, b = map(int, sys.stdin.readline().strip().split())
        if a == 0 and b == 0:
            break
        print(a + b)

q10952()