def main():
    ln = int(input())
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        if len(s) <= ln:
            a.append(s)
        else:
            a.append(s[:ln - 3] + "...")
    for i in range(n):
        print(a[i])


if __name__ == "__main__":
    main()
