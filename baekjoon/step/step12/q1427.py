# 소트인사이드
import sys

# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

N = sys.stdin.readline().strip()
arr = [int(n) for n in N]
arr.sort(reverse=True)
for v in arr:
    print(v, end="")