# 배수와 약수
import sys

# 입력은 여러 테스트 케이스로 이루어져 있다. 
# 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 
# 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

# 각 테스트 케이스마다 :
# 첫 번째 숫자가 두 번째 숫자의 약수라면 factor 출력
# 첫 번째 숫자가 두 번째 숫자의 배수라면 multiple 출력
# 둘 다 아니라면 neither 출력

# 8 16    factor
# 32 4    multiple
# 17 5    neither

while(True):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")