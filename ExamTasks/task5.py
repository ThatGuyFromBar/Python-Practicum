def main():
    n = int(input())
    msr = 10000000
    for i in range(n):
        s = ""
        sr = 0
        k = 0
        while s != "end":
            s = input()
            if s != "end":
                s = int(s)
                k += 1
                sr += s
        sr = sr / k
        if sr < msr:
            msr = sr
    print("{:.2f}".format(msr))


if __name__ == "__main__":
    main()
