import sys

def q2439():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        for j in range(n - (i + 1)):
            print(" ", end='')
        for k in range(i + 1):
            print("*", end='')
        print()

q2439()