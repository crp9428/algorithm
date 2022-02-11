# 정수 삼각형
from sys import stdin
input = stdin.readline
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

N = int(input().strip())
triangle = list(list(map(int, input().strip().split())) for _ in range(N))

# f = open("input.txt", "r")
# N = int(f.readline().strip())
# triangle = list(list(map(int, f.readline().strip().split())) for _ in range(N))

for i in range(1, N):
    for j, v in enumerate(triangle[i]):
        lastIdx = len(triangle[i]) - 1
        if j == 0:
            triangle[i][j] += triangle[i-1][0]
        elif j == lastIdx:
            triangle[i][j] += triangle[i-1][lastIdx-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            
print(max(triangle[N - 1]))
# f.close()