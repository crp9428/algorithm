import sys

def q15552():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(a + b)

q15552()