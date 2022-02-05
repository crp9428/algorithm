# 나이순 정렬
import sys
input = sys.stdin.readline

# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

N = int(input().strip())
array = []
for _ in range(N):
    age, name = input().strip().split()
    age = int(age)
    array.append([age, name])
    
array.sort(key= lambda x: x[0])

for v in array:
    print(f"{v[0]} {v[1]}")


# 삽입정렬? 시간초과
# N = int(input().strip())
# arr = [0]
# age, name = input().strip().split()
# arr[0] = [int(age), name]
# for i in range(N - 1):
#     age, name = input().strip().split()
#     age = int(age)
#     for i, v in enumerate(arr):
#         if age < v[0]:
#             arr.insert(i, [age, name])
#             break
#         if i + 1 == len(arr):
#             arr.append([age, name])
#             break

# for v in arr:
#     print(f"{v[0]} {v[1]}")
