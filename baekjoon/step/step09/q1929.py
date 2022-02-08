# 소수 구하기
from sys import stdin
input = stdin.readline
import math

# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def main():
    M, N = map(int, input().strip().split())
    primes = [True for _ in range(0, N + 1)]
    primes[0] = primes[1] = False
    for i in range(2, math.ceil(math.sqrt(N)) + 1):
        if primes[i] == False: continue
        for j in range(i * 2, N + 1, i):
            primes[j] = False
    
    for i in range(M, N + 1):
        if primes[i]: print(i)
main()