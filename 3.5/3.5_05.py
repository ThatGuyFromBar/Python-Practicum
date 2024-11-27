from sys import stdin


def main():
    a = []
    s = stdin.readlines()
    for x in s:
        for m in x.split():
            if m.upper() == m[::-1].upper():
                a.append(m)
    for x in sorted(set(a)):
        print(x)


if __name__ == "__main__":
    main()
