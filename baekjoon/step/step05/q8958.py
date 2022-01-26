import sys

def q8958():
    t = int(input())
    for _ in range(t):
        plus = 0
        jumsu = 0
        ox = input()
        for i in ox:
            if i == "X":
                plus = 0
            else:
                plus += 1
            jumsu += plus
        print(jumsu)
    
q8958()