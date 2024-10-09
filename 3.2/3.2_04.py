def main():
    n = int(input())
    m = int(input())
    a1 = set()
    a2 = set()
    for i in range(n):
        s = input()
        a1.add(s)
    for i in range(m):
        s = input()
        a2.add(s)
    ans = len(a1.intersection(a2))
    if ans == 0:
        print("Таких нет")
    else:
        print(ans)


if __name__ == "__main__":
    main()
