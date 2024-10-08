def main():
    s = "qwe"
    a = []
    while s != "":
        s = input()
        if s[-3:] != "@@@":
            if s[:2] == "##":
                a.append(s[2:])
            else:
                a.append(s)
    for i in range(len(a)):
        print(a[i])


if __name__ == "__main__":
    main()
