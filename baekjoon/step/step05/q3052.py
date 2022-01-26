import sys

def q3052():
    rem = set()
    for _ in range(10):
        n = int(input())
        rem.add(int(n % 42))
    
    print(len(rem))
    
q3052()