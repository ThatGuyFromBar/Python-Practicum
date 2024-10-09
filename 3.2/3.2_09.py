def main():
    things = {}
    s = "qwe"
    while s != "":
        s = input()
        if s != "":
            a = s.split()
            for i in range(len(a)):
                if not (things.__contains__(a[i])):
                    things[a[i]] = 0
                things[a[i]] += 1
    for x in things:
        print(x, things[x])


if __name__ == "__main__":
    main()
