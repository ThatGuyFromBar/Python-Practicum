v1 = int(input())
v2 = int(input())
v3 = int(input())
s = [v1, v2, v3]
s.sort(reverse=True)
for i in range(3):
    if s[i] == v1:
        print(f"{i + 1}. Петя")
    elif s[i] == v2:
        print(f"{i + 1}. Вася")
    else:
        print(f"{i + 1}. Толя")