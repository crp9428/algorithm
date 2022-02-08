# 베르트랑 공준
from sys import stdin
input = stdin.readline
import math

# f = open("input.txt", "r")
def main():
    primes = [True for _ in range(123456 * 2 + 1)]
    primes[0] = primes[1] = False
    for i in range(2, math.ceil(math.sqrt(len(primes))) + 1):
        if primes[i] == False: continue
        for j in range(i + i, len(primes), i):
            primes[j] = False
    
    while(True):
        n = int(input().strip())
        # input = int(f.readline().strip())
        if n == 0: break
        case = primes[n + 1 : 2 * n + 1]
        print(case.count(True))
main()
# f.close()