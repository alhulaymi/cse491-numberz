

class adder(object):
    def __init__(self):
        self._primeslist = [2]

    def __iter__(self):
        return self
        
    def _is_prime(self,primes, n):
        for i in primes:
            if n % i == 0:
                return False
        return True

    def next(self):
        start = self._primeslist[-1] + 1
        while 1:
            if self._is_prime(self._primeslist, start):
                self._primeslist.append(start)
                return start

            start += 1