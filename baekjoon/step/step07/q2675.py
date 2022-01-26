import sys
from functools import *

def q2675():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        r, s = sys.stdin.readline().strip().split()
        r = int(r)
        result = reduce(lambda acc, cur: acc + cur*r, s, "")
        print(result)
        
q2675()