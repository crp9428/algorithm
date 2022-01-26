import sys
from functools import *

def q10809():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    s = sys.stdin.readline().strip()
    result = reduce(lambda acc, cur: acc + str(s.find(cur)) + " ", alphabet, "")
    print(result)
    
q10809()