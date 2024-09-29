def main():
    a = int(input())
    if a == 0:
        print(1)
    else:
        s = 1
        for i in range(a):
            s *= i + 1
        print(s)


if __name__ == "__main__":
    main()
