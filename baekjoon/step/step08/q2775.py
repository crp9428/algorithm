# 부녀회장이 될테야
import sys

# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 주어지는 양의 정수 k(k는 1 이상)와 n(n은 1 이상 14 이하)에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

tt = int(sys.stdin.readline().strip())
for t in range(tt):
    kk = int(sys.stdin.readline().strip()); nn = int(sys.stdin.readline().strip())
    arr = [[0]*nn for k in range(kk + 1)]
    for k in range(kk + 1):
        if k == 0:
            for n in range(nn):
                arr[k][n] = 1 if n == 0 else arr[k][n-1] + 1
        else:
            for n in range(nn):
                arr[k][n] = 1 if n == 0 else arr[k - 1][n] + arr[k][n - 1]
    
    print(arr[kk][nn - 1])