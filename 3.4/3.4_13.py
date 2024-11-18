from itertools import permutations


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s = list(permutations(s, n))
    for i in range(len(s)):
        print(", ".join(s[i]))


if __name__ == "__main__":
    main()
