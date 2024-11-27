

def main():
    import json
    from sys import stdin
    with open("scoring.json") as file:
        data = json.load(file)
    answers = stdin.readlines()
    score = 0
    while data:
        tests = data.pop(0)
        plus = int(tests['points'] / len(tests['tests']))
        for test in tests['tests']:
            result = test['pattern']
            answer = answers.pop(0).strip('\n')
            if result == answer:
                score += plus
    print(score)


if __name__ == "__main__":
    main()
