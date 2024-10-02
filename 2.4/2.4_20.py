def main():
    n = int(input())
    ms = 0
    msi = 0
    for i in range(2, 11):
        m = n
        s = 0
        while m > 0:
            s += m % i
            m = m // i
        if s > ms:
            ms = s
            msi = i
    print(msi)


if __name__ == "__main__":
    main()
