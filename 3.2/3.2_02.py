def main():
    a = set()
    s = input()
    for x in s:
        a.add(x)
    s = input()
    ans = ""
    for x in s:
        if a.__contains__(x) == 1 and ans.count(x) == 0:
            ans += x
    print(ans)


if __name__ == "__main__":
    main()
