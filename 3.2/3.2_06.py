def main():
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    for i in range(n + m):
        s = input()
        if not (a.__contains__(s)):
            a.add(s)
        elif not (b.__contains__(s)):
            a.remove(s)
            b.add(s)
    if len(a) == 0:
        print("Таких нет")
    else:
        a = list(a)
        a.sort()
        for x in a:
            print(x)


if __name__ == "__main__":
    main()
