

def adder(n=10):
    s = 0
    for i in range(n+1):
        s = s + i
    return s

def adder2(n):
    s = 0
    for i in xrange(n+1):
        s = s + i
        print i, s
    return s

def adder3(n):
    s = (n / 2.0) * (n+1)
    return int(s)

#def adder2(n):
#    return sum( range(n+1) )

print adder(20)

# n = 3
# s = 0
# for i in [0,1,2,3]:
#     i=0 => print 0
#     i=1 => print 1
#     i=2 => print 2
#     i=3 => print 3
