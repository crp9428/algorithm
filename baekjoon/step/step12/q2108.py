# 통계학
import sys
from collections import Counter

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 
# 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값, 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값, 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
numbers.sort()

print(round((sum(numbers) / N))) # 산술평균

print(numbers[N // 2]) # 중앙값

count = Counter(numbers).most_common(2)
# 최빈값
if N > 1:
    if count[0][1] == count[1][1]: print(count[1][0])
    else: print(count[0][0])
else: print(count[0][0])

print(numbers[N - 1] - numbers[0]) # 범위