def main():
    s = float(input())
    n = 0
    while s != 0:
        if s >= 500:
            n += 0.9 * s
        else:
            n += s
        s = float(input())
    print(n)


if __name__ == "__main__":
    main()