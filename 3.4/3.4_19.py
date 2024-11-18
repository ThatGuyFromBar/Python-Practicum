from itertools import product
from itertools import combinations
from itertools import chain


def main():
    s = input()
    vars = [item for item in sorted(set(s.split())) if item.isupper()]
    length = len(vars)
    print(*[v for v in vars], "F")
    for values in product([False, True], repeat=length):
        gs = {key: value for key, value in zip(vars, values)}
        print(*[int(v) for v in values], int(eval(s, gs)))


if __name__ == "__main__":
    main()
