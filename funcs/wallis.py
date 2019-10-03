
"""
Function used to calculate pi using wallis equation. 
"""
def wallis(n):
    sum = 1.0
    for i in range(1, 2 * n, 2):
        x = i * i
        x = x / (i * i)
        sum = sum * x
    sum = sum * 2
    return sum
        