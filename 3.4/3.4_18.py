from itertools import product
from itertools import combinations
from itertools import chain


def main():
    s = input()
    print('a b c f')
    for a, b, c in product([0, 1], repeat=3):
        print(a, b, c, int(eval(s, {'a': a, 'b': b, 'c': c})))


if __name__ == "__main__":
    main()
