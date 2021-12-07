# import module1
# a = 5 + '10'
# print(a)

# f = open('somefile.txt')

x = -5
# if x<0:
#     raise Exception('x should be >0')

# assert(x>=0), 'x is not possitive'

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

try: 
    x  = 5 /1
    b = x + ''
except ZeroDivisionError as e:
    print('an error happened', e)
except TypeError as e:
    print('type error', e)
else:
    print('everything is good')
finally:
    print('cleaning')


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)

def test_value2(x):
    if x<2:
        raise ValueTooSmallError('value is to small', x)

try:
    test_value2(1)
except ValueTooSmallError as e:
    print(e.message, e.value)