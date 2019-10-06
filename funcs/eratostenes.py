from math import sqrt


def eratostenes(a, n):
    if n > 1 and n-a >= 1:
        n = n + 1
        A = [True for i in range(n)]
        A[0:2] = [False, False]
        for i in range(2, int(sqrt(n))):
            if A[i]:
                for j in range(2*i, n, i):
                    A[j] = False
        result = [i for i, val in enumerate(A) if val]
        return [i for i in result if i >= a]
    else:
        return []