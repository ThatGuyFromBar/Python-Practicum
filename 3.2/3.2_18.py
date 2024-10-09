def main():
    n = int(input())
    dots = {}
    for i in range(n):
        a = input().split()
        s = a[0][:-1] + "." + a[1][:-1]
        if not (dots.__contains__(s)):
            dots[s] = []
        dots[s].append([a[0][-1], a[1][-1]])
    maxk = 0
    for x in dots:
        if len(dots[x]) > maxk:
            maxk = len(dots[x])
    print(maxk)


if __name__ == "__main__":
    main()
