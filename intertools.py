from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

a = [1,2]
b = [3]
prod  = product(a,b)
print(list(prod))

a1 = [1,2,3]
perm = permutations(a1,2)
print(list(perm))

comb = combinations(a1, 2)
print(list(comb))

combwr = combinations_with_replacement(a1, 2)
print(list(combwr))


a3 = [1,4,3,2]
acc = accumulate(a3, func=operator.mul)
print(list(acc))

acc2 = accumulate(a3, func=max)
print(list(acc2))

def l3(x):
    return x<=3

a4 = [1,2,3,4,5,6]
group_obj = groupby(a4, key=lambda x:x<=3)
for k, v in group_obj:
    print(k,list(v))


for i in count(10):
    print(i)
    if i==15:
        break

a5=[1,2,3]
for i in cycle(a5):
    print(i)
    if i == 3:
        break

for i in repeat(1, 5):
    print(i)