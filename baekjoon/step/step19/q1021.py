# 회전하는 큐
from sys import stdin
input = stdin.readline
from collections import deque

# N개의 원소를 포함하고 있는 양방향 순환 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
# 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. 
# N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 
# 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

# f = open("input.txt", "r")
def main():
    N, M = map(int, input().strip().split())
    # N, M = map(int, f.readline().strip().split())
    elements = list(map(lambda x: int(x) - 1, input().strip().split()))
    # elements = list(map(lambda x: int(x) - 1, f.readline().strip().split()))
    deq = deque([i for i in range(0, N)])
    count = 0
    
    while(len(elements) > 0):
        move = -deq.index(elements[0]) if deq.index(elements[0]) < (len(deq) / 2) else (len(deq) - deq.index(elements[0]))
        deq.rotate(move)
        count += abs(move)
        deq.popleft()
        elements = elements[1:]
    print(count)

main()
# f.close()