# 수 정렬하기 3
import sys

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 카운팅 정렬
N = int(sys.stdin.readline().strip())
array = [0] * 10001; maxNum = 0
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    array[num] += 1
    if maxNum < num:
        maxNum = num
        
for i in range(0, maxNum + 1):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
