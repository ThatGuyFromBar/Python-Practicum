def recursive_digit_sum(num):
    if num > 0:
        return num % 10 + recursive_digit_sum(num // 10)
    return 0
