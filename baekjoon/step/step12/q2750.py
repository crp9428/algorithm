# 수 정렬하기
import sys

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

N = int(sys.stdin.readline().strip())
arr = []

# 1. 삽입 정렬??
# arr.append(int(sys.stdin.readline().strip()))
# for _ in range(N - 1):
#     num = int(sys.stdin.readline().strip())
#     for i, v in enumerate(arr):
#         if num < v:
#             arr.insert(i, num)
#             break
#         if i + 1 == len(arr):
#             arr.append(num)
#             break
# for v in arr:
#     print(v)

# 2. 버블 정렬
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
    
for i in range(len(arr) - 1, -1, -1):
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

for v in arr:
    print(v)