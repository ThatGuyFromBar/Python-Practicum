def main():
    n = int(input())
    msr = 1000000000
    for i in range(int(input())):
        ns = []
        while (s := input()) != "end":
            ns.append(int(s))
        msr = min(msr, sum(ns) / len(ns))
    print("{:.2f}".format(msr))


if __name__ == "__main__":
    main()
