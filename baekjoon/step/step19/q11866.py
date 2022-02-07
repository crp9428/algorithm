# 요세푸스 문제 0
from sys import stdin
input = stdin.readline
from collections import deque

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

N, K = map(int, input().strip().split())
deq = deque([str(i) for i in range(1, N + 1)])
result = []

while(len(deq) > 0):
    deq.rotate(-K + 1)
    result.append(deq.popleft())
    
print("<" + ", ".join(result).rstrip() + ">")