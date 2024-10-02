def main():
    n = int(input())
    s = 0
    for i in range(n):
        m = input()
        for i in range(len(m)):
            s += int(m[i])
    print(s)


if __name__ == "__main__":
    main()
