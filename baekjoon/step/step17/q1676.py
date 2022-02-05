# 팩토리얼 0의 개수
import sys
input = sys.stdin.readline

# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
# 첫째 줄에 구한 0의 개수를 출력한다.
# 소인수분해의 성질을 활용하여 N!의 끝에 0이 얼마나 많이 오는지 구하는 문제

N = int(input().strip())
count = N // 5 + N // 25 + N // 125
print(count)