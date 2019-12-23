import time
import random
from multiprocessing import Process

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

def execute_process():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime(rand))

def main():
    print("crunching numbers now")
    t0 = time.time()

    procs = []

    for _ in range(10):
        proc = Process(target = execute_process, args=())
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    
    t1 = time.time()
    total_time = t1 - t0

    print('Execution Time: {}'.format(total_time))

if __name__ == '__main__':
    main()