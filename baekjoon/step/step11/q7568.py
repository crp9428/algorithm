# 덩치
import sys

# 첫 줄에는 전체 사람의 수 N이 주어진다. 
# 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다.

# 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.

N = int(sys.stdin.readline().strip())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr.append({'x': x, 'y': y, 'n': 0})
    
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if arr[i]['x'] > arr[j]['x'] and arr[i]['y'] > arr[j]['y']:
            arr[j]['n'] += 1
        
for v in arr:
    print(v['n'] + 1, end=" ")