# 균형잡힌 세상
import sys
input = sys.stdin.readline
import re

# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
# 1. 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 2. 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 3. 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 4. 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 5. 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
# f = open("input.txt", "r")

string = ""; stack = []; isSymmetry = True
while(True):
    string = input().rstrip()
    # string += f.readline().rstrip()
    if string.find(".") == 0 and len(string) == 1:
        break
    elif string.find(".") == -1:
        continue

    string = re.sub("[^\(\)\[\]]", "", string); stack = []; isSymmetry = True
    for s in string:
        tmp = ""
        if s == "(":
            stack.append("s")
        elif s == "[":
            stack.append("b")
        elif s == ")":
            if len(stack) == 0 or stack.pop() != "s":
                isSymmetry = False
                break
        elif s == "]":
            if len(stack) == 0 or stack.pop() != "b":
                isSymmetry = False
                break
    isSymmetry = isSymmetry and len(stack) == 0
    print("yes") if isSymmetry else print("no")
    string = ""
# f.close()