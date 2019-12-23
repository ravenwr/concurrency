import time
import random

def calculate_prime(n):
    primfac = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

def main():
    print('Crunching numbers now')
    t0 = time.time()

    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime(rand))
    
    t1 = time.time()
    total_time = t1 - t0

    print('Execution Time: {}'.format(total_time))

if __name__ == '__main__':
    main()