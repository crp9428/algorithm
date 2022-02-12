# 수 정렬하기 2
import sys

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

N = int(sys.stdin.readline().strip())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 병합 정렬 - 시간초과!
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     list = []
#     while len(left) > 0 and len(right) > 0:
#         if left[0] < right[0]:
#             list.append(left.pop(0))
#         else:
#             list.append(right.pop(0))
#     if len(left) > 0:
#         list += left
#     if len(right) > 0:
#         list += right
#     return list

# print(mergeSort(array))

# 병합정렬 - 심화버전, 메모리 231584KB, 시간 1316ms
def mergeSort(list, p, q):
    if p >= q: return
    mid = (p + q) // 2
    mergeSort(list, p, mid)
    mergeSort(list, mid + 1, q)
    merge(list, p, mid + 1, q)

def merge(list, left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if list[l] <= list[r]:
            merged.append(list[l])
            l +=1
        else:
            merged.append(list[r])
            r +=1
    while l < right:
        merged.append(list[l])
        l +=1
    while r <= end:
        merged.append(list[r])
        r+=1

    l = left
    for n in merged:
        list[l] = n	
        l +=1

mergeSort(array, 0, len(array) - 1)
for v in array:
    print(v)

# 퀵 정렬 - 메모리 초과
# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     low, equal, high = [], [], []
#     for v in arr:
#         if v < pivot:
#             low.append(v)
#         elif pivot < v:
#             high.append(v)
#         else:
#             equal.append(v)
#     return quick(low) + equal + quick(high)
# array = quick(array)
# for v in array:
#     print(v)

# 힙 정렬 ??? 시간초과
# n = len(array)
# array = [0] + array
# result = []

# def heapSort(arr, n):
#     for i in range(n, 0, -1):
#         p, c1, c2 = i, i * 2, i * 2 + 1
#         if c1 > n:
#             continue
#         elif c2 > n:
#             if arr[p] > arr[c1]:
#                 arr[p], arr[c1] = arr[c1], arr[p]
#             continue
#         if arr[p] > arr[c1]:
#             arr[p], arr[c1] = arr[c1], arr[p]
#         if arr[p] > arr[c2]:
#             arr[p], arr[c2] = arr[c2], arr[p]
#         if arr[c1] > arr[c2]:
#             arr[c1], arr[c2] = arr[c2], arr[c1]
#     return array

# for i in range(n, 0, -1):
#     result.append(heapSort(array, i).pop(1))

# for v in result:
#     print(v)