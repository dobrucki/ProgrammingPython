from funcs.wallis import wallis
from funcs.gcd import gcd
from funcs.eratostenes import eratostenes

if __name__ == '__main__':
    
    # First task
    for num, approx in enumerate(wallis(10)):
        print("Przyblizenie nr {0:d} : {1:.5f}".format(num+1, approx))

    # Second task
    a = 2
    b = 100
    print("Liczby pierwsze w przedziale od {0: d} do {1: d}:".format(a, b))
    print(', '.join(eratostenes(a, b)))
