def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        if s.find("зайка") >= 0:
            a.append(s.find("зайка") + 1)
        else:
            a.append("Заек нет =(")
    for x in a:
        print(x)


if __name__ == "__main__":
    main()
