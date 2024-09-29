def main():
    n = int(input())
    ans = -1
    a = []
    a.append(0)
    nice = True
    for i in range(n):
        s = int(input())
        h1 = s % 256
        r = (s // 256) % 256
        m = s // (256 ** 2)
        h2 = (37 * (m + r + a[i])) % 256
        if (h2 != h1 or h2 >= 100) and nice:
            ans = i
            nice = False
        a.append(h1)
    print(ans)


if __name__ == "__main__":
    main()
