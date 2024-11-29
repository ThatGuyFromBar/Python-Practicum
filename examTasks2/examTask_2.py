def main():
    dicts = {}
    s = input()
    while s != "":
        a = s.lower().split()
        for x in a:
            key = x[len(x) - 1].upper()
            if not (key in dicts):
                dicts[key] = []
            dicts[key].append(x)
        s = input()
    for i in dicts.keys():
        print(f"{i} - {", ".join(sorted(set(dicts[i])))}")


if __name__ == "__main__":
    main()
