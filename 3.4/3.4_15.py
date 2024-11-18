from itertools import permutations


def main():
    s = []
    for i in range(int(input())):
        t = input().split(", ")
        for x in t:
            s.append(x)
    s.sort()
    s = list(permutations(s, 3))
    for i in range(len(s)):
        print(" ".join(s[i]))


if __name__ == "__main__":
    main()
