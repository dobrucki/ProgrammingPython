from funcs.gcd import gcd

def lcm(a, b):
    result = a * b
    result /= gcd(a, b)
    return int(result)