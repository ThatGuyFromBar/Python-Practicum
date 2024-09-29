def main():
    s = input()
    k = 0
    while s != "Приехали!":
        if s.count("зайка") > 0:
            k += 1
        s = input()
    print(k)


if __name__ == "__main__":
    main()
