def main():
    x = 0
    y = 0
    s = input()
    while s != "СТОП":
        n = int(input())
        if s == "СЕВЕР":
            y += n
        elif s == "ЮГ":
            y -= n
        elif s == "ВОСТОК":
            x += n
        elif s == "ЗАПАД":
            x -= n
        s = input()
    print(y)
    print(x)


if __name__ == "__main__":
    main()
