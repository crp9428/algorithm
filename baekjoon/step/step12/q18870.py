# 좌표 압축
from sys import stdin
input = stdin.readline

# f = open('input.txt', "r")
def main():
    N = int(input().strip())
    # N = int(f.readline().strip())
    origin = list(map(int, input().strip().split()))
    # origin = list(map(int, f.readline().strip().split()))
    numSet = list(set(origin))
    numSet.sort()
    
    dict = {}
    for i, v in enumerate(numSet):
        dict[v] = i
    
    for i, v in enumerate(origin):
        idx = dict[v]
        origin[i] = idx
    
    for v in origin:
        print(v, end=" ")
    
main()
# f.close()