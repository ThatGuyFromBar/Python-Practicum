def main():
    n = int(input())
    m = int(input())
    xl = int(input())
    xm = xl - 1000000
    for i in range(n - 1):
        x = int(input())
        if abs(x - xl) < m and x > xm:
            xm = x
        xl = x
    print(xm)


if __name__ == "__main__":
    main()
