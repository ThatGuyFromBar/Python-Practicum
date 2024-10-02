def main():
    n = int(input())
    m = int(input())
    sp = len(str(n * m))
    k = 0
    for i in range(n):
        for j in range(m):
            k += 1
            s = str(k)
            while len(s) != sp:
                s = " " + s
            print(s, end=" ")
        print()


if __name__ == "__main__":
    main()
