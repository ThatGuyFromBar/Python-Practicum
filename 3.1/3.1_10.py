def main():
    s = "qwe"
    sall = ""
    while s != "ФИНИШ":
        s = input()
        if s != "ФИНИШ":
            sall += s.lower()
    maxl = ''
    k = 0
    for i in range(len(sall)):
        if sall.count(sall[i]) > k and sall[i] != " ":
            k = sall.count(sall[i])
            maxl = sall[i]
    print(maxl)


if __name__ == "__main__":
    main()
