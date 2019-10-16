from funcs.eratostenes import eratostenes
import collections
from functools import reduce


def count_prime_divisors(n):
    """Calculates prime divisors of number n.
    """
    divisors = []
    for i in eratostenes(2, n):
        while n != 1:
            if n % i == 0:
                divisors.append(i)
                n /= i
            else:
                break
    return divisors


def lcm(a, b):
    """Calculates lowest common multiplier of two integers.

    a -- first integer
    b -- second integer
    """

    divisors_a = count_prime_divisors(a)
    divisors_b = count_prime_divisors(b)

    divisors_a_counter = collections.Counter(divisors_a)
    divisors_b_counter = collections.Counter(divisors_b)

    result_counter = divisors_a_counter | divisors_b_counter
    result_list = list(result_counter.elements())

    return reduce(lambda x, y: x*y, result_list)





