# 단어 정렬
import sys
input = sys.stdin.readline

# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

N = int(input().strip())
arr = set()
for i in range(N):
    word = input().strip()
    arr.add(word)
# f = open("step\\step12\\test.txt", "r")
# N = int(f.readline().strip())
# arr = set()
# for i in range(N):
#     word = f.readline().strip()
#     arr.add(word)
# f.close()
arr = list(arr)
arr.sort(key=lambda x: (len(x), x))

for v in arr:
    print(v)