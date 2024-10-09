def main():
    n = int(input())
    dishes = {}
    for i in range(n):
        s = input()
        dishes[s] = 0
    m = int(input())
    for i in range(m):
        n = int(input())
        for j in range(n):
            s = input()
            dishes[s] += 1
    a = []
    for x in dishes:
        if dishes[x] == 0:
            a.append(x)
    if len(a) > 0:
        a.sort()
        for x in a:
            print(x)
    else:
        print("Готовить нечего")


if __name__ == "__main__":
    main()
