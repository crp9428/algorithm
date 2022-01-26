# 큰 수 A+B
import sys

def xySum(x, y, q):
    return (x + y + q)

a, b = map(lambda x: x[::-1], sys.stdin.readline().strip().split())
aLen = len(a); bLen = len(b)
maxLen = aLen if aLen > bLen else bLen
sumAB = ""; q = 0; x = 0; y = 0

for i in range(maxLen):
    x = int(a[i]) if i < aLen else 0
    y = int(b[i]) if i < bLen else 0
    tSum = xySum(x, y, q)
    q = tSum // 10
    sumAB += str(tSum % 10)
    
if q != 0:
    sumAB += str(q)

result = int(sumAB[::-1])
print(result)
