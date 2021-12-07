myset = {1,2,3,1}
print(myset)

s1 = set("hello")
print(s1)

#empty set
s2 = set()
print(set())
s2.add(1)
s2.add(3)
s2.discard(2)
print(s2)

odds = {1,3,5,7}
evens = {1,2,4,6,8}
primes = {2,3,5,7}
u = odds.union(evens)
print(u)
i = odds.intersection(primes)
print(i)
d = odds.difference(primes)
d2 = primes.difference(odds)
print(d)
print(d2)
sd = odds.symmetric_difference(primes)
print(sd)

seta = {1,2,3,4,5,6,7,8,9}
setaa = seta.copy()
setaaa = seta.copy()
setb = {1,2,3,10,11,12}
seta.update(setb)
print(seta)
setaa.intersection_update(setb)
print(setaa)
print(setaaa.difference(setb))
setaaa.difference_update(setb)
print(setaaa)

setc = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setd = {1,2,3}
print(setd.issubset(setc))
print(setc.isdisjoint(setd))

fseta= frozenset([1,2,3,4])
print(fseta)
