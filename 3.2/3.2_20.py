def main():
    s = input()
    a = list(set(int(i) for i in s.split("; ")))
    a.sort()
    for i in range(len(a)):
        primes = []
        for j in range(len(a)):
            n = a[i]
            m = a[j]
            while n != 0 and m != 0:
                if n > m:
                    n = n % m
                else:
                    m = m % n
            if n + m == 1:
                primes.append(a[j])
        if len(primes) > 0:
            s = str(a[i]) + " - "
            for x in primes:
                s += str(x) + ", "
            print(s[:-2])


if __name__ == "__main__":
    main()
