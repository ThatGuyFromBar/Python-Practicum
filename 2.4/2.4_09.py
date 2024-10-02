def main():
    n = int(input())
    s = ""
    for i in range(n):
        num = input()
        dm = 0
        for j in range(len(num)):
            if int(num[j]) > dm:
                dm = int(num[j])
        s += str(dm)
    print(s)


if __name__ == "__main__":
    main()
