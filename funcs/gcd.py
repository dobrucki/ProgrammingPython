def gcd(a, b):
    """Calculates greatest common divisor of two integers.

    a -- first integer
    b -- second integer
    """
    while(b != 0):
        c = a % b
        a = b
        b = c
    return a