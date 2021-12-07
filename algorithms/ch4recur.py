def sum(data, n):
    if n == 0:
        return 0
    else:
        return sum(data, n-1)+data[n-1]


def sum2(data, start, stop):
    """Binary recursion"""
    if start > stop:  # Slice start > stop
        return 0
    if start == stop:
        return data[start]
    mid = (stop + start) // 2
    return sum2(data, start, mid) + sum2(data, mid+1, stop)


l = [1, 2, 3, 4, 5, 6]
# s = sum2(l, 0, 5)
# print(s)


def reverse(data, n):
    if n >= len(data)//2:
        return
    idx_ops = len(data)-n - 1
    data[n], data[idx_ops] = data[idx_ops], data[n]
    reverse(data, n+1)


# input = [1,2,3,4,5,6,7,8,9,10]
# reverse(input,0)
# print(input)

def power(x, n):
    """Compute 2^n in O(log(n))"""
    if n == 0:
        return 1
    r = power(x, n//2)
    if n % 2 == 0:
        return r*r
    else:
        return x*r*r

# print(power(2,1))


def find_min_max(data, start, end):

    if start >= end:
        return data[start], data[start]
    mid = (start+end)//2
    min1, max1 = find_min_max(data, start, mid)
    min2, max2 = find_min_max(data, mid+1, end)
    return (min1 if min1 < min2 else min2, max1 if max1 > max2 else max2)


ls2 = [4, 2, 3, 19, 2, 56, 8, 2, 7]
# print(find_min_max(ls2, 0, len(ls2)-1))


def uniq_elem(data, start, end):
    if end - start <= 1:
        return True
    elif not uniq_elem(data, start, end - 1):
        return False
    elif not uniq_elem(data, start+1, end):
        return False
    else:
        return data[start] != data[end-1]


def contains(data, ele, idx):
    if idx >= len(data):
        return False
    elif data[idx] == ele:
        return True
    else:
        return contains(data, ele, idx+1)


def uniq_elem2(data, start):
    if start >= len(data):
        return True
    if contains(data, data[start], start+1):
        return False
    else:
        return uniq_elem2(data, start+1)


# print(uniq_elem2([1,2,3,4,5,6,7],0))

def product_add_sub(m, n):
    if m == 0:
        return 0
    else:
        return n + product_add_sub(m-1, n)

# print(product_add_sub(21,5))

def hanio(n, src, dest, aug):
    if n == 1:
        print("move 1 from {0} to {1}".format(src, dest))
        return
    hanio(n-1, src, aug, dest)
    print('Move {0} from {1} to {2}'.format(n, src, dest))
    hanio(n-1,aug, dest, src)

# print(hanio(4,'SRC', 'DEST', 'AUG'))

def subset(setA):
    if len(setA) == 0:
        return [{}]
    e = setA.pop()
    print('pop ',e)
    ss = subset(setA)
    return [ {e,*x} for x in ss ] + ss


# l = subset({1, 2, 3, 4, })
# for x in l:
#     print(x)

def subset2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0:
        return [[]]
    ss = subset2(nums[1:])
    return [[nums[0], *x] for x in ss] + ss


# print(subset2([1,2,3,4]))

def reverse(s):
    if len(s) == 0:
        return ''
    e = s[-1]
    return e+reverse(s[:-1])

# print(reverse(''))

def is_palindrome(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# print(is_palindrome('abbabba'))
from collections import deque
def rearrange_even_odd(l):
    if len(l) <=1:
        return l
    left = l.popleft()
    sub = rearrange_even_odd(l)
    if left % 2 == 0:
        sub.appendleft(left)
    else:
        sub.append(left)
    return sub


# l3 = deque([1, 2, 5, 10, 23, 4, 6])
# r1 = rearrange_even_odd(l3)
# print(r1)

def rearrage_k(s, k):
    if len(s) <= 1:
        return s
    l, r = s.popleft(),s.pop()
    subr = rearrage_k(s, k)
    if l<=k:
        subr.appendleft(l)
    else:
        subr.append(l)
    if r>k:
        subr.append(r)
    else:
        subr.appendleft(r)
    return subr
    

# l4 = deque([3,49,8,55,12,9,0,7,5,2])
# rearrage_k(l4,100)
# print(l4)

# def sum_2_int(data,i, k):
#     # include i element
#     bs(data[i:], k-data[i-1])
#     # dont include i
#     sum_2_int(data[i:], k)

