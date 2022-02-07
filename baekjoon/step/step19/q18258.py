# 큐 2
from sys import stdin
input = stdin.readline
from collections import deque

# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

N = int(input().strip())
# f = open("input.txt", "r")
# N = int(f.readline().strip())

# 2. deque 사용하지 않고 구현(메모리 92256, 시간 2120)
def main2():
    deq = []; fIdx = 0;
    for _ in range(N):
        cmd = list(input().strip().split())
        # cmd = list(f.readline().strip().split())
        dlen = len(deq) - fIdx
        if cmd[0] == 'push':
            x = int(cmd[1])
            deq.append(x)
        elif cmd[0] == 'pop':
            if dlen > 0:
                print(deq[fIdx])
                fIdx += 1
            else:
                print(-1)
        elif cmd[0] == 'size':
            print(dlen)
        elif cmd[0] == 'empty':
            print(1) if dlen == 0 else print(0)
        elif cmd[0] == 'front':
            print(deq[fIdx]) if dlen > 0 else print(-1)
        elif cmd[0] == 'back':
            print(deq[-1]) if dlen > 0 else print(-1)

main2()
# f.close()

# 1. deque 사용 실습(메모리 92452, 시간 2132)
def main1():
    deq = deque()
    for _ in range(N):
        cmd = list(input().strip().split())
        # cmd = list(f.readline().strip().split())
        dlen = len(deq)
        if cmd[0] == 'push':
            x = int(cmd[1])
            deq.append(x)
        elif cmd[0] == 'pop':
            print(deq.popleft()) if dlen > 0 else print(-1)
        elif cmd[0] == 'size':
            print(dlen)
        elif cmd[0] == 'empty':
            print(1) if dlen == 0 else print(0)
        elif cmd[0] == 'front':
            print(deq[0]) if dlen > 0 else print(-1)
        elif cmd[0] == 'back':
            print(deq[-1]) if dlen > 0 else print(-1)
