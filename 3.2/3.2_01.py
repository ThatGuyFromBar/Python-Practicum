def main():
    s = input()
    a = set()
    for x in s:
        a.add(x)
    s = ""
    for x in a:
        s += x
    print(s)


if __name__ == "__main__":
    main()
