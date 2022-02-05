# 괄호
import sys
input = sys.stdin.readline

# 입력은 T개의 테스트 데이터로 주어진다. 
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 
# 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
# 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

T = int(input().strip())
# f = open("input.txt", "r")
# T = int(f.readline().strip())

for t in range(T):
    ps = input().strip()
    # ps = f.readline().strip()
    stack = []
    isVPS = True
    for v in ps:
        if v == "(":
            stack.append(0)
        else:
            if len(stack) == 0:
                isVPS = False
            else:
                stack.pop()
    isVPS = isVPS and len(stack) == 0
    print("YES") if isVPS else print("NO")

# f.close()