# 카드 2
from sys import stdin
input = stdin.readline

# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

N = int(input().strip())
def main():
    cards = [i for i in range(1, N + 1)]
    idx = 0; size = len(cards)
    while(size > 1):
        # 1. 제일 위에 있는 카드를 바닥에 버린다.
        idx += 1
        size -= 1
        # 2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
        cards.append(cards[idx])
        idx += 1
    print(cards[idx])

main()
