def main():
    n = int(input())
    k = 0
    for i in range(n):
        s = int(input())
        good = True
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:
                good = False
                break
        if s == 1:
            good = False
        if good:
            k += 1
    print(k)


if __name__ == "__main__":
    main()
