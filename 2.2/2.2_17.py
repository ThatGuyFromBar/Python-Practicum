a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0:
    print("No solution")
elif a == 0:
    print(f"{-c / b:.2f}")
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("No solution")
    else:
        s = []
        s.append((-b + d ** 0.5) / (2 * a))
        s.append((-b - d ** 0.5) / (2 * a))
        s.sort()
        if s[0] != s[1]:
            print(f"{s[0]:.2f} {s[1]:.2f}")
        else:
            print(f"{s[0]:.2f}")
