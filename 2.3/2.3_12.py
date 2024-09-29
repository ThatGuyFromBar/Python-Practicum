def main():
    n = int(input())
    m = 0
    while n > 0:
        if n % 10 > m:
            m = n % 10
        n //= 10
    print(m)


if __name__ == "__main__":
    main()
