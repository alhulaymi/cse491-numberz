# this is an implementation of the Fibonacci series using
# Python's iterator functionality.  Here, 'fib' is a class that
# obeys the iterator protocol.

class fib(object):
    def __init__(self):
        print "init"
        self.last_1 = 1
        self.last_2 = 1

    def __iter__(self):
        print "iter"
        return self

    def next(self):
        print "next"
        next_fib = self.last_1 + self.last_2
        self.last_1, self.last_2 = self.last_2, next_fib
        return next_fib
