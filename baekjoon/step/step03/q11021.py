import sys

def q11021():
    T = int(sys.stdin.readline().strip())
    for i in range(1, T + 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        print("Case #{0}: {1}".format(i, a + b))

q11021()