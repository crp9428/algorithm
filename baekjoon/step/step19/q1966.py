# 프린터 큐
from sys import stdin
input = stdin.readline
from collections import deque

# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 
# 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

# f = open("input.txt", "r")
T = int(input().strip())
# T = int(f.readline().strip())

def main():
    for _ in range(T):
        N, M = map(int, input().strip().split())
        # N, M = map(int, f.readline().strip().split())
        docs = deque(map(int, input().strip().split()))
        # docs = deque(map(int, f.readline().strip().split()))
        count = 0
        
        while(M >= 0):
            maxImportance = max(docs); maxIdx = docs.index(maxImportance)
            docs.rotate(-maxIdx)
            M -= maxIdx
            docs.popleft()
            count += 1
            if M == 0:
                break
            else:
                M = M - 1 if M > 0 else M + len(docs)
            
        print(count)

main()
# f.close()