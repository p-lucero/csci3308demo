import itertools

def test(v):
    s = 2
    r = 0
    bs = bin(v)[2:] # convert to binary and remove leading 0b that python tacks on
    while len(bs) != 42:
        bs = "0" + bs # fix size of bitset
    for sb in bs:
        b = int(sb) # convert bit to int
        if (s % 7) == b:
            r = r+(2*b)-1
        s = (6+s*(5+s*s*s*(2+s*(3+s))) + b*(5+s*(5+s*(6+s*s*(3+s*6))))) % 7
    return r

normcap = 2**42 # don't use this
starcap = 2**14 # don't use this
testcap = 2**6
counter = 0
stuff = [2**x for x in range(42)]
for i in xrange(normcap):
    if test(i) != 0:
        counter += 1
    if i in stuff:
        print i
print "Number of non-zero results:", counter
