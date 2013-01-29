#The first prime number is 2 but im following the outcome of sieve-fn.py and starting by 3
import sieve

def test1():
    print "--<<test 1>>--"
    print "should get to one value above 29 and stop"
    x = 0
    for i in sieve.adder():
        x = i
        if i > 29:
            break
    assert x == 31
    print "=>Success"
            
def test2():
    print "--<<test 2>>--"
    print "Should get us the first two (3,5)"
    x = sieve.adder()
    y = x.next()
    assert y == 3
    y = x.next()
    assert y == 5
    print "=>Success"

    
def test3():
    print "--<<test 3>>--"
    print "will loop to one prime above 6, then one more manually by next()"
    x = sieve.adder()
    for i in x:
        if i > 6:
            break
    y = x.next()
    assert y == 11
    print "=>Success"
    
test1()
test2()
test3()