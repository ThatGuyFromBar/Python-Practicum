def main():
    n = int(input())
    porridges = {}
    for i in range(n):
        a = input().split()
        for j in range(1, len(a)):
            if not (porridges.__contains__(a[j])):
                porridges[a[j]] = []
            porridges[a[j]].append(a[0])
    s = input()
    if porridges.__contains__(s):
        if len(porridges[s]) > 0:
            porridges[s].sort()
            for i in range(len(porridges[s])):
                print(porridges[s][i])
        else:
            print("Таких нет")
    else:
        print("Таких нет")


if __name__ == "__main__":
    main()
