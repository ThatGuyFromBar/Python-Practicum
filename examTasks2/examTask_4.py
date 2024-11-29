def main():
    from itertools import product
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(input().split(", "))
    s = numbers[0]
    for i in range(n - 1):
        s = list(product(s, numbers[i + 1]))
        for j in range(len(s)):
            s[j] = ''.join(s[j])
    s = sorted(list(set(s)))
    for a in s:
        print(f"{''.join(a)}")


if __name__ == "__main__":
    main()
