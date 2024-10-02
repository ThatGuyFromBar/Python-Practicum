def main():
    n = int(input())
    m = int(input())
    sp = len(str(n * m))
    fwd = False
    add = n * 2 + 1
    up = -1
    k = 0
    for i in range(n):
        k = i + 1
        add -= 2
        up += 2
        fwd = False
        for j in range(m):
            fwd = not fwd
            s = str(k)
            while len(s) != sp:
                s = " " + s
            print(s, end=" ")
            if fwd:
                k += add
            else:
                k += up
        print()


if __name__ == "__main__":
    main()
