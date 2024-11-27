

def main():
    import json
    from sys import stdin
    jfile = input()
    with open(jfile, encoding="UTF-8") as file:
        data1 = json.load(file)
    jfile2 = input()
    with open(jfile2, encoding="UTF-8") as file:
        data2 = json.load(file)
    fresh = {}
    for info in data1:
        name = info.pop('name')
        fresh[name] = info
    for info in data2:
        name = info.pop('name')
        if name not in fresh:
            fresh[name] = {}
        for key in info.keys():
            if fresh[name].get(key, '') < info[key]:
                fresh[name][key] = info[key]
    with open(jfile, 'w') as file:
        json.dump(fresh, file, sort_keys=False, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
