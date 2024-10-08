def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        a.append(s)
    s = input()
    for i in range(n):
        if a[i].casefold().count(s.casefold()) > 0:
            print(a[i])


if __name__ == "__main__":
    main()
