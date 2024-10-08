def main():
    n = int(input())
    k = 0
    for i in range(n):
        s = input()
        k += s.count("зайка")
    print(k)


if __name__ == "__main__":
    main()
