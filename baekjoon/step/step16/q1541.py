# 잃어버린 괄호
from sys import stdin
input = stdin.readline
import re

K = input().strip()
num = list(map(int, re.sub("[^0-9]", ",", K).split(",")))
oper = re.sub("[0-9]", "", K)

result = num[0]; isBracket = False; temp = 0
for i in range(1, len(num)):
    if oper[i-1] == "-" and isBracket is True:
        result -= temp
        temp = num[i]
    elif oper[i-1] == "-" and isBracket is False:
        isBracket = True
        temp += num[i]
    elif oper[i-1] == "+" and isBracket is True:
        temp += num[i]
    elif oper[i-1] == "+" and isBracket is False:
        result += num[i]

if isBracket is True:
    result -= temp
else:
    result += temp

print(result)