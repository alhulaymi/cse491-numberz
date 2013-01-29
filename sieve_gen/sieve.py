def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def adder():
    _primeslist = [2]
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            yield start

        start += 1