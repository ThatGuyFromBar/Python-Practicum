def main():
    n = int(input())
    good = True
    for i in range(n):
        s = input()
        if s[0] != 'а' and s[0] != 'б' and s[0] != 'в':
            good = False
    if good:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()