
def prime_sieve(n):
    primes = [i for i in range(n + 1)]
    primes[1] = 0
    i = 2
    while i <= n:
        if primes[i] != 0:
            j = i + i
            while j <= n:
                primes[j] = 0
                j = j + i
        i += 1
    return [i for i in primes if i != 0]


def main():
    import json
    from sys import stdin
    s = stdin.readlines()
    numbers = [int(x.strip()) for x in s]
    primes = prime_sieve(max(numbers))
    data = {}
    for prime in primes:
        a = []
        for num in numbers:
            if num % prime == 0:
                a.append(num)
        if not (a == []):
            data[str(prime)] = sorted(list(set(a)))
    with open("result.json", 'w') as file:
        json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
