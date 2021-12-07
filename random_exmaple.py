import numpy as np
import random

a = random.random()
print(a)

b = random.uniform(1,10)
print(breakpoint)

c = random.randint(1,10)
print(c)
d = random.randrange(1,10)
print(d)

random.seed()

import secrets

a = secrets.randbelow(10)
print(a)

b = secrets.randbits(4)
print(b)


c = np.random.rand(3,3)

print(c)

d = np.random.randint(0,20,(3, 3))
print(d)
