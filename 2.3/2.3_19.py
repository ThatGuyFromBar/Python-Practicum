import math


def main():
    n = 500
    x = n
    print(n)
    s = input()
    while s != "Угадал!":
        n = math.ceil(n / 2)
        if s == "Меньше":
            x -= n
        elif s == "Больше":
            x += n
        print(x)
        s = input()


if __name__ == "__main__":
    main()
