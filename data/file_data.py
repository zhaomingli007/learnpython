
text = open('data/data1.txt', 'r')

d = {}

for l in text:
    words = l.strip().lower().split(' ')
    for w in words:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1


print(d)
