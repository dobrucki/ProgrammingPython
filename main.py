from funcs.wallis import wallis
from funcs.gcd import gcd
from funcs.eratostenes import eratostenes

if __name__ == '__main__':
    
    # First task
    print("\n# Podpunkt 1\n")
    n = 10
    print("{0:d} pierwszych przyblizen liczby PI:".format(n))
    print('\n'.join(map(str, wallis(n))) + '\n')

    a = 84
    b = 18
    print("Najwiekszy wspolny dzielnik liczb {} i {} to {}.\n".format(a, b, gcd(a, b)))
    
    # Second task
    print("\n# Podpunkt 2\n")
    a = 2
    b = 100
    print("Liczby pierwsze w przedziale od {0:d} do {1:d}:".format(a, b))
    print(', '.join(map(str, eratostenes(a, b))))
