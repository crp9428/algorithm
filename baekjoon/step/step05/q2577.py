import sys

def q2577():
    a, b, c = map(int, list(input() for _ in range(3)))
    result = a * b * c
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while(result > 1):
        r = int(result % 10)
        arr[r] = arr[r] + 1
        result = result / 10
    for i in arr:
        print(i)
    
q2577()