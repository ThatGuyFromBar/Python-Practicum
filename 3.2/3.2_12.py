def main():
    n = int(input())
    names = {}
    for i in range(n):
        s = input()
        if not (names.__contains__(s)):
            names[s] = 1
        else:
            names[s] += 1
    a = []
    for x in names:
        if names[x] > 1:
            a.append(x)
    if len(a) == 0:
        print("Однофамильцев нет")
    else:
        a.sort()
        for i in range(len(a)):
            print(a[i], "-", names[a[i]])


if __name__ == "__main__":
    main()
