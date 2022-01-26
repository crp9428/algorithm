import sys

def q10818():
    N = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print("%d %d" % (min(arr), max(arr)))
    
q10818()