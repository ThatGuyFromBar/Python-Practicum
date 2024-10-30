def main():
    n, m, d = [int(input()) for i in range(3)]
    s = " - ".join([str(i) for i in range(n, m + 1, d)] + [str(i) for i in range(m, n - 1, -d)])
    print(s)


if __name__ == "__main__":
    main()
