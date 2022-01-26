def q9498():
    jumsu = int(input())
    if jumsu >= 90:
        print("A")
    elif jumsu < 90 and jumsu >= 80:
        print("B")
    elif jumsu < 80 and jumsu >= 70:
        print("C")
    elif jumsu < 70 and jumsu >= 60:
        print("D")
    else:
        print("F")

q9498()