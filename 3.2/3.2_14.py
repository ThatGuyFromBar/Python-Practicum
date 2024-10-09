def main():
    n = int(input())
    a = set()
    for i in range(n):
        a.add(input())
    m = int(input())
    b = []
    for i in range(m):
        name = input()
        n = int(input())
        good = True
        for j in range(n):
            s = input()
            if not (a.__contains__(s)):
                good = False
        if good:
            b.append(name)
    if len(b) > 0:
        b.sort()
        for x in b:
            print(x)
    else:
        print("Готовить нечего")


if __name__ == "__main__":
    main()
