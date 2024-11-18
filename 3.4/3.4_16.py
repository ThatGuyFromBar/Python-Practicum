from itertools import product
from itertools import combinations
from itertools import chain


def main():
    a1 = input()
    b1 = input()
    a = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
    b = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
    b.remove(b1)
    cs = product(b, a.values())
    threes = combinations(cs, 3)
    threes = [comb for comb in threes if a[a1] in chain.from_iterable(comb)]
    for i in range(10):
        print(f"{threes[i][0][0]} {threes[i][0][1]}, "
              f"{threes[i][1][0]} {threes[i][1][1]}, "
              f"{threes[i][2][0]} {threes[i][2][1]}")


if __name__ == "__main__":
    main()
