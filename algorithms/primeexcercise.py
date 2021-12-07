def minmax(data):
    min = data[0]
    max = data[0]
    for n in data:
        if n > max:
            max = n
        if n < min:
            min = n
    return min, max

min, max = minmax([4,-1,3,9,80,6])
print(min, max)

# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
def squares(n):
    return sum(x**2 for x in range(n) if x**2 < n)

print(squares(10))

for e in range(50, 90, 10):
    print(e)

for e in range(8, -10, -2):
    print(e)

print([2**i for i in range(9)])

from random import randrange, choice
print(randrange(1, 100,1))
print(choice([1,2,3,4,5,6,7,8,9,10]))

def mychoice(data):
    return data[randrange(0,len(data)-1, 1)]

print(mychoice([1,2,3,4,5,6,7,8,9,10]))


def isdistinct(data):
    distinct_set  = {s for s in data}
    return len(data) == len(distinct_set)

print(isdistinct([1,2,3,4,5]))
print(isdistinct([1,2,3,4,5,3]))


# 1.16
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    return data


l = [1, 2, 3]
print(scale(l, 2))
print(l)

# c1.18
print([i*(i+1) for i in range(10)])

# c1.19
print([chr(c) for c in range(97,97+26)])
print([chr(c) for c in range(65, 65+26)])

#c1.20 shuffle
from random import shuffle, randint
shlst = [1, 2, 3, 4, 5, 6]
shuffle(shlst)
print(shlst)

def myshuffle(data):
    for i in data:
        idx1 = randint(0, len(data)-1)
        idx2 = randint(0, len(data)-1)
        data[idx1], data[idx2] = data[idx2], data[idx1]


shlst1 = [1, 2, 3, 4, 5, 6]
myshuffle(shlst1)
print(shlst1)

#1.21 reverse input from std input
# chars = str(input("Input a array of character \n"))
# print(''.join([chars[i] for i in range(len(chars)-1, -1, -1)]))

#1.23 raise an error
try:
    print([1,2,3][3])
except IndexError as e:
    print('Index out of bound error.')  

#C-1.24
def count_vowels(data):
    vowels = {'a', 'o', 'e', 'i', 'u'}
    return len([c for c in data if c in vowels])
print(count_vowels(['1','a','b','c','o','f','u']))

#C-1.25
def remove_punctuation(data):
    def is_not_punc(c): return ord(c) > ord('a') and ord(
        c) < ord('z') or ord(c) >ord('A') and ord(c) < ord('Z') or c == ' '
    return ''.join([c for c in data if is_not_punc(c)])

print(remove_punctuation('''Let's try, Mike.'''))

#C-1.27
#8=> 1, 2, 4, 8 ; test up to square root, if k is a factor and n % k == 0, then n / k is also a factor
def compute_factors(n):
    k = 1
    store = []
    while k * k < n:
        if n % k == 0:
            yield k
            store.append(n // k)
        k += 1
    if k*k == n: # Perfect square
        yield k
    for i in range(len(store)-1,-1,-1):
        yield store[i]


fctrs = compute_factors(8)
for i in fctrs:
    print(i)

#C-1.29 'catdog', 
def allword(letters, word='', ls = []):
    letters or ls.append(word)
    for l in letters:
        allword(letters - {l}, word + l, ls)

res_list = []
allword({'a','b','c','d','e'}, ls=res_list)
print(res_list)
print(len(res_list))

#C-1.30 number of times repeatedly divide this number.
def divide_times(n): return (0 if n < 2 else  1 + divide_times(n//2))

print(divide_times(1000))


#C-1.31 make change: 100, 50, 10, 5, 2, 1
def make_change(charged, pay):
    change = pay-charged
    if change == 0: print(0)

    def get_change(ch, monetary):
        for m in monetary:
            monetary.remove(m)
            if ch // m >0:
                print(str(ch // m)+ ' ' + str(m))
            if ch % m > 0:
                get_change(ch % m, monetary)
    get_change(change, [100, 50, 20, 5, 2, 1])
        

make_change(27, 100)

#C-1.33 calculators
def calculator():
    ar = list(input('arithmetic expression: \n'))
    stack = []
    ops = {'+','-','x','/'}
    tmp = ''
    op_pre = None
    for c in ar:
        if c in ops:
            stack.append(tmp)
            tmp = ''
            op_pre and stack.append(op_pre)
            op_pre = c
        else:
            tmp+=c
    if tmp != '':
        stack.append(tmp)
        stack.append(op_pre)
    print(stack)
    or1,or2 = 0,0
    for x in stack:
        if x in ops:
            if x=='+':
                or2 = int(or1)+int(or2)
            elif x =='-':
                or2 = int(or1) - int(or2)
            elif x == 'x':
                or2 = int(or1) * int(or2)
            elif x=='/':
                or2 = int(or1) / int(or2)
        else:
            or1, or2 = or2, x
    return or2


# res = calculator()
# print(res)

#C-1.36 count time of word appears in the list 
def count_words():
    words_str = str(input('input a str of words separated by space \n'))
    words_list = words_str.split()
    words_dict  = {}
    for w in words_list:
        if w in words_dict:
            words_dict[w] += 1
        else: 
            words_dict[w] = 1
    print(words_dict)
    return words_dict

count_words()
