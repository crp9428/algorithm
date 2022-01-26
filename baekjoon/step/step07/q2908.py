import sys

def q2908():
    a, b = sys.stdin.readline().strip().split()
    rA = int(a[::-1])
    rB = int(b[::-1])
    print(rA if rA > rB else rB)
    
q2908()