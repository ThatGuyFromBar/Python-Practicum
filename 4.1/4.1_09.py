def is_prime(num):
    prime = num != 1
    if num != 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
    return prime
