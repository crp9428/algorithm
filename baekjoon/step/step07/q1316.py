import sys

def q1316():
    n = int(sys.stdin.readline().strip())
    groupWordCount = 0
    for _ in range(n):
        ss = sys.stdin.readline().strip()
        ssSet = set()
        isGroupWord = True
        for i, s in enumerate(ss):
            if (s in ssSet) and (s == ss[i-1]):
                continue
            elif s in ssSet:
                isGroupWord = False
                break
            else:
                ssSet.add(s)
        if isGroupWord:
            groupWordCount += 1    
    print(groupWordCount)
    
q1316()