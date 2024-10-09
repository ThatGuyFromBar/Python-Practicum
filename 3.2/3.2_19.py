def main():
    n = int(input())
    toys = {}
    for i in range(n):
        s = input().replace(":", "").replace(",", "")
        a = s.split()
        for j in range(1, len(a)):
            if not (toys.__contains__(a[j])):
                toys[a[j]] = set()
            toys[a[j]].add(a[0])
    a = []
    for x in toys:
        if len(toys[x]) == 1:
            a.append(x)
    a.sort()
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
