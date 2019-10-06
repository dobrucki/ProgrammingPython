def wallis(n):
    """Calculates approximation of PI using Wallis equation.

    n -- number of n-first approximations
    """
    if n >= 1:
        res = [2.0]
        for i in range(1, n+1):
            x = 4 * i**2
            x /= (x-1)
            res.append(res[-1] * x)
        return res[1:]
    else:
        return []
        