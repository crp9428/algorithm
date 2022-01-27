# 택시 기하학
import sys
import math

# 알고리즘 자체보다는 유클리드 기하학과 택시 기하학에 대한 이해가 우선
# 아래 링크 참고하여 학습함
# https://itholic.github.io/kata-taxicab-circle/

R = int(sys.stdin.readline().strip())
print("%.6f" % (math.pi * (R**2)))
print("%.6f" % (2 * (R**2)))