def main():
    s = input()
    a = s.split()
    b = []
    for i in range(len(a)):
        a[i] = bin(int(a[i]))[2:]
        b.append({"digits": len(a[i]), "units": a[i].count("1"), "zeros": a[i].count("0")})
    print(b)


if __name__ == "__main__":
    main()
