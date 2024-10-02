def main():
    n = int(input())
    m = int(input())
    sp = len(str(n * m))
    fwd = True
    k = 0
    for i in range(n):
        if fwd:
            if i != 0:
                k += m - 1
        else:
            k += m + 1
        for j in range(m):
            if fwd:
                k += 1
            else:
                k -= 1
            s = str(k)
            while len(s) != sp:
                s = " " + s
            print(s, end=" ")
        print()
        fwd = not fwd


if __name__ == "__main__":
    main()
