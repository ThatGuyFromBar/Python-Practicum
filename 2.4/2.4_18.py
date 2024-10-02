def main():
    n = int(input())
    k = 0
    a = []
    m = 0
    while k < n:
        s = ""
        for i in range(m + 1):
            if k < n:
                k += 1
                s += str(k) + " "
        m += 1
        a.append(s[:-1])
    for i in range(len(a)):
        ls = (len(a[len(a) - 1]) - len(a[i])) // 2
        a[i] = " " * ls + a[i]
        print(a[i])


if __name__ == "__main__":
    main()
