
def main():
    with open(input(), encoding="UTF-8") as file:
        lines = [string for string in file.read().split("\n") if string]
    file1 = input()
    file2 = input()
    file3 = input()
    for line in lines:
        chet = []
        nechet = []
        both = []
        for x in line.split():
            s1 = x.count("1") + x.count("3") + x.count("5") + x.count("7") + x.count("9")
            s2 = x.count("0") + x.count("2") + x.count("4") + x.count("6") + x.count("8")
            if s1 < s2:
                chet.append(x)
            elif s2 < s1:
                nechet.append(x)
            else:
                both.append(x)
        with open(file1, "a", encoding="UTF-8") as file:
            file.write(" ".join(chet) + "\n")
        with open(file2, "a", encoding="UTF-8") as file:
            file.write(" ".join(nechet) + "\n")
        with open(file3, "a", encoding="UTF-8") as file:
            file.write(" ".join(both) + "\n")


if __name__ == "__main__":
    main()
