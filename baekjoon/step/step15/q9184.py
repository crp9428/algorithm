# 신나는 함수 실행
from sys import stdin
input = stdin.readline

# f = open("input.txt", "r")

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif memory[a][b][c] is not None: 
        return memory[a][b][c]
    elif a < b and b < c:
        memory[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memory[a][b][c]
    else:
        memory[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memory[a][b][c]

while(True):
    a, b, c = map(int, input().strip().split())
    # a, b, c = map(int, f.readline().strip().split())
    a1, b1, c1 = a, b, c
    result = 0
    if a == -1 and b == -1 and c == -1: 
        break
    elif a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
        continue
    elif a > 20 or b > 20 or c > 20:
        a1, b1, c1 = 20, 20, 20
        
    memory = list(list([None for _ in range(c1 + 1)] for _ in range(b1 + 1)) for _ in range(a1 + 1))
    w(a1, b1, c1)
    print(f"w({a}, {b}, {c}) = {memory[a1][b1][c1]}")
    
# f.close()