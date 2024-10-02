def main():
    n = int(input())
    m = 1
    peak = 0
    sp = len(str((n + 1) // 2))
    for i in range(n):
        if i <= ((n + 1) // 2) - 1:
            peak += 1
        else:
            peak -= 1
        s = ""
        sk = ""
        m = 1
        for j in range(n):
            if m > peak:
                sk = str(peak)
            else:
                sk = str(m)
            while len(sk) != sp:
                sk = " " + sk
            s += sk + " "
            if j < ((n + 1) // 2) - 1:
                m += 1
            else:
                m -= 1
        print(s[:-1])


if __name__ == "__main__":
    main()
