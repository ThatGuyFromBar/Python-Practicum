def main():
    s = "qwe"
    friends = {}
    while s != "":
        s = input()
        b = s.split()
        for i in range(len(b)):
            if not (friends.__contains__(b[0])):
                friends[b[0]] = []
            if not (friends.__contains__(b[1])):
                friends[b[1]] = []
            friends[b[0]].append(b[1])
            friends[b[1]].append(b[0])
            friends[b[0]] = set(friends[b[0]])
            friends[b[1]] = set(friends[b[1]])
            friends[b[0]] = list(friends[b[0]])
            friends[b[1]] = list(friends[b[1]])
    a = []
    for x in friends:
        b = set()
        for i in range(len(friends[x])):
            for j in range(len(friends[friends[x][i]])):
                cond = friends[x].count(friends[friends[x][i]][j]) == 0
                if friends[x][i] != x and friends[friends[x][i]][j] != x and cond:
                    b.add(friends[friends[x][i]][j])
        a.append([x])
        b = list(b)
        b.sort()
        for f in b:
            a[len(a) - 1].append(f)
    a.sort()
    for i in range(len(a)):
        s = a[i][0] + ": "
        for j in range(1, len(a[i])):
            s += a[i][j] + ", "
        if s[-2] == ",":
            s = s[:-2]
        print(s)


if __name__ == "__main__":
    main()
