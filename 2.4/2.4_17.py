def main():
    n = int(input())
    k = 0
    for i in range(n):
        s = input()
        if s == s[::-1]:
            k += 1
    print(k)


if __name__ == "__main__":
    main()
