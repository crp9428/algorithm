# 분수찾기
import sys

# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 -> ...
# X(X는 1 이상 1천만 이하)가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 1. 틀린 것 같진 않긴 한데 시간초과남..
# X = int(sys.stdin.readline().strip())
# n = 1; num = 1; den = 1; isMaxNum = True; isMaxDen = True
# for x in range(1, X):
#     if isMaxNum and isMaxDen:
#         n += 1
#         isMaxNum = False if n % 2 == 0 else True
#         isMaxDen = True if n % 2 == 0 else False
#         num = 1 if n % 2 == 0 else n
#         den = n if n % 2 == 0 else 1
#         continue
        
#     num = num + 1 if n % 2 == 0 else num - 1
#     den = den - 1 if n % 2 == 0 else den + 1
#     if(num == n):
#         isMaxNum = True
#     if(den == n):
#         isMaxDen = True
        
# print(f"{num}/{den}")

X = int(sys.stdin.readline().strip())

num = 0; count = 0
while(X > count):
    num += 1
    count += num

n = 1; d = 1
if(num % 2 == 0):
    n = X - (count - num)
    d = num + 1 - n
else:
    d = X - (count - num)
    n = num + 1 - d

print(f"{n}/{d}")


