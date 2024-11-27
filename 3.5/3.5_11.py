
def main():
    with open(input(), encoding='UTF-8') as base_text:
        numbers = [int(number) for number in base_text.read().split()]
    count = len(numbers)
    pos = [x for x in numbers if x > 0]
    count2 = len(pos)
    mins = min(numbers)
    maxs = max(numbers)
    sums = sum(numbers)
    sred = round(sums / count, 2)
    with open(input(), 'w', encoding='UTF-8') as finished_text:
        print("{", file=finished_text)
        print(f"\t\"count\": {count},", file=finished_text)
        print(f"\t\"positive_count\": {count2},", file=finished_text)
        print(f"\t\"min\": {mins},", file=finished_text)
        print(f"\t\"max\": {maxs},", file=finished_text)
        print(f"\t\"sum\": {sums},", file=finished_text)
        print(f"\t\"average\": {sred}", file=finished_text)
        print("}", file=finished_text)


if __name__ == "__main__":
    main()
