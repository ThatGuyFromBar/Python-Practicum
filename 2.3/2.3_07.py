def main():
    a = int(input())
    b = int(input())
    n = a * b
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(n // (a + b))


if __name__ == "__main__":
    main()
