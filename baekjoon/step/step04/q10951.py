import sys

def q10951():
    while(True):
        try:
            a, b = map(int, sys.stdin.readline().strip().split())
            print(a + b)
        except ValueError as e:
            break

q10951()