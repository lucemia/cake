import random
from collections import Counter

def rand5():
    return random.randint(0, 4)

def rand25():
    return rand5() * 5 + rand5()

def rand7():
    k = rand25()
    if k < 21:
        return k % 7

c = Counter()

c.update(rand25() for k in xrange(1000000))
c1 = Counter()
c1.update(random.randint(0, 24) for k in xrange(1000000))

for i in c:
    print i, c[i], c1[i]
