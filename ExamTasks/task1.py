def main():
    a = int(input())
    b = int(input())
    c = int(input())
    r = (a ** b) % (a + c)
    print(f"({a} ^ {b}) mod ({a} + {c}) = {r}")


if __name__ == "__main__":
    main()
