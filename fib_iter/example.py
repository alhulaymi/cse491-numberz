print "will import"
import fib
print "imported"

print "will fib"
a = fib.fib
print "did fib"

b = range(3)
print a
print "will loop"
for n, i in zip(b, a):
    print "one iter "+str(i)
    print i

# additional questions to address:
# - what the heck do 'zip' and 'range' do, and why are they there?
