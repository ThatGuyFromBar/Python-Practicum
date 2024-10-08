def main():
    s = "qwe"
    a = []
    while s != "":
        s = input()
        if s != "":
            if s[0] != "#":
                k = s.find("#")
                if k != -1:
                    a.append(s[:k])
                else:
                    a.append(s)
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
