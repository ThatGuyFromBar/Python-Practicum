def main():
    n = int(input())
    m = int(input())
    sp = len(str(n * m))
    k = 0
    for i in range(n):
        k = i + 1 - n
        for j in range(m):
            k += n
            s = str(k)
            while len(s) != sp:
                s = " " + s
            print(s, end=" ")
        print()


if __name__ == "__main__":
    main()
