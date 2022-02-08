# 골드바흐의 추측
from sys import stdin
input = stdin.readline

def main():
    primes = [True for _ in range(10001)]
    primes[0] = primes[1] = False
    for i in range(2, 101):
        if primes[i] == False: continue
        for j in range(i * 2, 10001, i):
            primes[j] = False
    
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        sIdx = n // 2; bIdx = n // 2
        if primes[sIdx]:
            print(f"{sIdx} {bIdx}")
        else:
            partition = None
            for i in range(sIdx, -1, -1):
                if primes[i] is False: continue
                for j in range(bIdx, n + 1):
                    if primes[j] is False: continue
                    elif i + j > n: break
                    
                    if i + j == n:
                        partition = str(i) + " " + str(j)
                        break
                if partition is not None:
                    break
            print(partition)
        
main()