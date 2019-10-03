
def wallis(n):
    sum = 1.0
    for i in range(1, n):
        x = (2 * i) * (2 * i)
        x = x / (2 * i - 1)
        x = x / (2 * i + 1)
        sum = sum * x
    sum = sum * 2
    return sum
        