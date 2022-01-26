import sys
from functools import *

def q1157():
    s = sys.stdin.readline().strip().upper()
    sSet = set(s)
    maxAlphabet = ""
    maxCount = 0
    for i in sSet:
        count = reduce(lambda acc, cur: acc + 1 if cur == i else acc, s, 0)
        if count > maxCount:
            maxCount = count
            maxAlphabet = i
        elif count == maxCount:
            maxAlphabet = "?"
    print(maxAlphabet)
    
q1157()