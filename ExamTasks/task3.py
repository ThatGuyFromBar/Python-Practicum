def main():
    n = int(input())
    m = int(input())
    d = int(input())
    s = ""
    for i in range(n, m + 1, d):
        s += f"{i} - "
    for i in range(m, n - 1, -d):
        s += f"{i} - "
    print(s[:-3])


if __name__ == "__main__":
    main()
