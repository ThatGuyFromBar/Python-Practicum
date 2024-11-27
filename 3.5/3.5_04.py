from sys import stdin


def main():
    a = []
    s = stdin.readlines()
    a += [line.rstrip('\n') for line in s if (line.lower().count(s[len(s) - 1].lower().rstrip('\n')) > 0
                                              and line != s[len(s) - 1])]
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
