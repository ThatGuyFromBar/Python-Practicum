def gcd(*args):
    a = args[0]
    for i in range(1, len(args)):
        b = args[i]
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        a = a + b
    return a
