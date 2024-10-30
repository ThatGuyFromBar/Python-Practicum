def main():
    a, b, c = [int(input()) for i in range(3)]
    print(f"({a} ^ {b}) mod ({a} + {c}) = {(a ** b) % (a + c)}")


if __name__ == "__main__":
    main()
