# string are immutable
s = 'this\'s my string'
print(s)
s1=""" abc \
break line"""
print(s1)

s1 = '  hello  '
print(s1.strip())
print(s1.find('l'))
print(s1.count('l'))
print(s1.replace("ll","LL"))
print(s1.split())
print(' '.join(['ab', 'd', 'e']))

my_list = ['a'] * 6
print(my_list)

my_str = ''.join(my_list)
print(my_str)

v1 = 'Tom'
s1 = 'the var is %s' % v1
print(s1)

print('t %.2f' % 3.1415)
print('my string is {}'.format('abc'))
print('my string is {:.2f}'.format(3.14159))
v2 = 3.14
# print(f"the string is {v2}")

tests = not ''
print('tests: {0}'.format(tests))