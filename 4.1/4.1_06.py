printed = set()


def modern_print(s):
    if s not in printed:
        printed.add(s)
        print(s)
