# 연산자 끼워넣기
import sys
input = sys.stdin.readline

# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 
# 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
# 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
# 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
# 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다.

f = open("input.txt", "r")

# N = int(input().strip())
# nums = list(map(int, input().strip().split()))
# sum, sub, mul, div = map(int, input().strip().split())
N = int(f.readline().strip())
nums = list(map(int, f.readline().strip().split()))
sum, sub, mul, div = map(int, f.readline().strip().split())

ops = ['sum' for _ in range(sum)] + ['sub' for _ in range(sub)] + ['mul' for _ in range(mul)] + ['div' for _ in range(div)]
cases = []; visit = [False for _ in range(len(ops))]; arr = ['' for _ in range(len(ops))]

def dfs(depth):
    if depth == len(ops):
        tmp = []
        for v in arr:
            tmp.append(v)
        cases.append(tmp)
        return
    
    for i in range(len(ops)):
        if visit[i]: continue
        visit[i] = True
        arr[depth] = ops[i]
        dfs(depth + 1)
        visit[i] = False

dfs(0)

results = [nums[0] for _ in range(len(cases))]
for i, case in enumerate(cases):
    for j in range(N - 1):
        if case[j] == 'sum':
            results[i] = results[i] + nums[j + 1]
        elif case[j] == 'sub':
            results[i] = results[i] - nums[j + 1]
        elif case[j] == 'mul':
            results[i] = results[i] * nums[j + 1]
        elif case[j] == 'div':
            if results[i] < 0 and nums[j + 1] > 0:
                results[i] = ((results[i] * -1) // nums[j + 1]) * -1
            else:
                results[i] = results[i] // nums[j + 1]

print(max(results))
print(min(results))
f.close()