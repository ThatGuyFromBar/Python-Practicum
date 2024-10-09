def main():
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    ans = 0
    for i in range(n + m):
        s = input()
        if not (a.__contains__(s)):
            a.add(s)
        elif not (b.__contains__(s)):
            b.add(s)
            ans -= 1
    ans += len(a)
    if ans == 0:
        print("Таких нет")
    else:
        print(ans)


if __name__ == "__main__":
    main()
