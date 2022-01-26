import sys

def q11022():
    T = int(sys.stdin.readline().strip())
    for i in range(1, T + 1, 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        sum = a + b
        print(f"Case #{i}: {a} + {b} = {sum}")

q11022()