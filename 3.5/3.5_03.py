from sys import stdin


def main():
    a = []
    for line in stdin:
        if line[0] != '#':
            if line.count('#') > 0:
                a.append(line.rstrip('\n')[:line.index('#')])
            else:
                a.append(line.rstrip('\n'))
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
