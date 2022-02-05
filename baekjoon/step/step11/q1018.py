# 체스판 다시 칠하기
import sys

# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

def getCount(board):
    startB = 0; startW = 0
    for i in range(8):
        for j in range(8):
            isEven = (i + j) % 2 == 0
            if isEven:
                if board[i][j] == 'W':
                    startB += 1
                elif board[i][j] == 'B':
                    startW += 1
            else:
                if board[i][j] == 'W':
                    startW += 1
                elif board[i][j] == 'B':
                    startB += 1
    return min(startB, startW)

N, M = map(int, sys.stdin.readline().strip().split())
origin = []
for i in range(N):
    origin.append(list(sys.stdin.readline().strip()))
# f = open("step\\step11\\1018Test.txt", "r")
# N, M = map(int, f.readline().strip().split())
# origin = []
# for i in range(N):
#     origin.append(list(f.readline().strip()))
# f.close()

N -= 7; M -= 7
counts = []
for n in range(N):
    for m in range(M):
        board = origin[n : n + 8]
        for i in range(8):
            board[i] = board[i][m : m + 8]
        counts.append(getCount(board))

print(min(counts))