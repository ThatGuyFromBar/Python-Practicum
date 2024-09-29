def main():
    n = int(input())
    s = ""
    x = 2
    while x <= n:
        if n % x == 0:
            s += str(x) + " * "
            n = n / x
        else:
            x += 1
    print(s[:-3])


if __name__ == "__main__":
    main()
