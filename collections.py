from collections import  Counter, namedtuple, OrderedDict, defaultdict, deque

a = 'aabaabbbbbbccc'
cnt = Counter(a)
print(cnt)
print(cnt.items())
print(cnt.most_common(2))
print(list(cnt.elements()))

Point = namedtuple('Point', 'x, y')
pt = Point(10,12)
print(pt)
print(pt.x, pt.y)
ordered_dict = OrderedDict()
ordered_dict['a'] = 3
ordered_dict['b'] = 4
ordered_dict['c'] = 2
ordered_dict['d'] = 1
print(ordered_dict)

ddict = defaultdict(int)
ddict['a'] = 1
ddict['b'] = 4
print(ddict)
print(ddict['c'])

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q)
q.appendleft(4)
print(q)
print(q.pop())
print(q)
q.popleft()
q.extend([4,5,6])
print(q)

q.rotate(2)
print(q)