def main():
    numbers = [1, 2, 3, 4, 5]
    s = [x for x in numbers if (x % 2) == 0] + [x for x in numbers if (x % 2) > 0]
    print(s)


if __name__ == "__main__":
    main()
