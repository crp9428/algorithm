import sys

def q1546():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    m = max(arr)
    newJumsu = list(map(lambda x: x / m * 100 , arr))
    print(sum(newJumsu)/len(newJumsu))
    
q1546()