import sys

def q5622():
    ss = sys.stdin.readline().strip()
    time = 0
    for s in ss:
        if s == "A" or s == "B" or s == "C":
            time += 3
        elif s == "D" or s == "E" or s == "F":
            time += 4
        elif s == "G" or s == "H" or s == "I":
            time += 5
        elif s == "J" or s == "K" or s == "L":
            time += 6
        elif s == "M" or s == "N" or s == "O":
            time += 7
        elif s == "P" or s == "Q" or s == "R" or s == "S":
            time += 8
        elif s == "T" or s == "U" or s == "V":
            time += 9
        elif s == "W" or s == "X" or s == "Y" or s == "Z":
            time += 10
    print(time)
    
q5622()