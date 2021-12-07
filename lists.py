import sys
import timeit
t = tuple(['a', 'a','b','c'])
c,*b,d = t
print(type(b))

print(sys.getsizeof(t))
print(timeit.timeit(stmt="(1,2,3,4,5)", number=1000000))
