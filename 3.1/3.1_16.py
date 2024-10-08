def main():
    ls = int(input()) - 3
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        a.append(s)
    for i in range(n):
        ls -= len(a[i])
        if ls <= 0:
            if ls == 0:
                sf = a[i] + "..."
            else:
                sf = a[i][:ls] + "..."
            print(sf)
            break
        else:
            print(a[i])


if __name__ == "__main__":
    main()
