#The first prime number is 2 but im following the outcome of sieve-fn.py and starting by 3
import sieve

def test1():
    print "--<<test 1>>--"
    print "should get to one value above 29 and stop"
    for i in range(29): #29 here has nothing to do with the value, but since there are less prime numbers than real numbers in a particular range, this will enusre the inclusion with minimal range
        x = sieve.next()
        if x > 29:
            break
    assert sieve.next() == 37
    print "=>Success"

            
def test2():
    print "--<<test 2>>--"
    print "Should manually get us the next two value using next(). Keeping in mind that the values are still restored in the imported module and one was used for the previous test"
    y = sieve.next()
    y = sieve.next()
    assert y == 43
    print "=>Success"

    
def test3():
    print "--<<test 3>>--"
    print "Will attempt to loop to prime values above 6. Next is called before the comparison to 6. Then one more manually by next()"
    for i in range(6):
        x = sieve.next()
        if x > 6:
            break
    y = sieve.next()
    assert y == 53
    print "=>Success"

    
test1()
test2()
test3()