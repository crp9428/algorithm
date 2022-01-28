# 설탕 배달
import sys

# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

N = int(sys.stdin.readline().strip())
bagArr = []; max5 = N // 5
for i5 in range(0, max5 + 1):
    if (N - i5*5) % 3 == 0:
        bagArr.append((i5 + (N - i5*5) // 3))
        
print(min(bagArr)) if len(bagArr) > 0 else print(-1)