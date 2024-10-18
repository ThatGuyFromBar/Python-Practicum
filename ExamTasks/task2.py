def main():
    a = int(input())
    s = input()
    b = int(input())
    ans = 0
    if (len(s) % 2 == 0) and s.count(" ") > 0:
        ans = a + b
    elif (len(s) % 2 == 0) and s.count(" ") == 0:
        ans = a - b
    elif (len(s) % 2 > 0) and s.count(" ") > 0:
        ans = a * b
    else:
        ans = a // b
    print(ans)


if __name__ == "__main__":
    main()
