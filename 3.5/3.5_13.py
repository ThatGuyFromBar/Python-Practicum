from sys import stdin
import json


def main():
    jfile = input()
    with open(jfile) as file:
        data = json.load(file)

    lines = stdin.readlines()

    for line in lines:
        if line:
            key, value = line.split('==')
            data[key.strip()] = value.strip()

    with open(jfile, 'w') as file:
        json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
