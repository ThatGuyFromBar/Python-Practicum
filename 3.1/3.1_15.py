def main():
    s = input()
    a = s.split()
    for i in range(len(a) - 1):
        a[i] = int(a[i])
        a[i + 1] = int(a[i + 1])
        while a[i] != 0 and a[i + 1] != 0:
            if a[i] > a[i + 1]:
                a[i] = a[i] % a[i + 1]
            else:
                a[i + 1] = a[i + 1] % a[i]
        a[i + 1] = a[i] + a[i + 1]
    print(a[len(a) - 1])


if __name__ == "__main__":
    main()
