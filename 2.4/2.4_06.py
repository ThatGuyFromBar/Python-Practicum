def main():
    n = int(input())
    m1 = 0
    m2 = 0
    for i in range(n):
        s = int(input())
        if i == 0:
            m1 = s
        else:
            m2 = s
            while m1 != 0 and m2 != 0:
                if m1 > m2:
                    m1 = m1 % m2
                else:
                    m2 = m2 % m1
            m1 = m1 + m2
    print(m1)


if __name__ == "__main__":
    main()
