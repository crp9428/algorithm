import sys

def q2562():
    arr = []
    for _ in range(9):
        arr.append(int(sys.stdin.readline().strip()))
    
    maxNum = max(arr)
    print("%d" % maxNum)
    print("%d" % (arr.index(maxNum) + 1))
    
q2562()