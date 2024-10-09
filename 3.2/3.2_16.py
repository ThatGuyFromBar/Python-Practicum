def main():
    s = "qwe"
    a = set()
    while s != "":
        s = input()
        b = s.split()
        for i in range(len(b)):
            if b[i] == "зайка":
                if i > 0:
                    a.add(b[i - 1])
                if i < len(b) - 1:
                    a.add(b[i + 1])
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
