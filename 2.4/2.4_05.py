def main():
    n = int(input())
    s = 0
    for i in range(n):
        ans = ""
        n = ""
        while ans != "ВСЁ":
            ans = input()
            n += ans
        if n.count("зайка") > 0:
            s += 1
    print(s)


if __name__ == "__main__":
    main()
