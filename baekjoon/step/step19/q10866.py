# 덱
from sys import stdin
input = stdin.readline
from collections import deque

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# N = int(input().strip())
f = open("input.txt", "r")
N = int(f.readline().strip())

# 1. deque 사용(메모리 32428, 시간 96)
def main1():
    deq = deque()
    for _ in range(N):
        cmd = list(input().strip().split())
        # cmd = list(f.readline().strip().split())
        if cmd[0] == "push_front":
            x = int(cmd[1])
            deq.appendleft(x)
        elif cmd[0] == "push_back":
            x = int(cmd[1])
            deq.append(x)
        elif cmd[0] == "pop_front":
            print(deq.popleft()) if len(deq) > 0 else print(-1)
        elif cmd[0] == "pop_back":
            print(deq.pop()) if len(deq) > 0 else print(-1)
        elif cmd[0] == "size":
            print(len(deq))
        elif cmd[0] == "empty":
            print(0) if len(deq) > 0 else print(1)
        elif cmd[0] == "front":
            print(deq[0]) if len(deq) > 0 else print(-1)
        elif cmd[0] == "back":
            print(deq[-1]) if len(deq) > 0 else print(-1)
    
main1()
f.close()

    

