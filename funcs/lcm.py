from funcs.gcd import gcd


def lcm(a, b):
    """Calculates lowest common multiplier of two integers.

    a -- first integer
    b -- second integer
    """
    result = a * b
    result /= gcd(a, b)
    return int(result)