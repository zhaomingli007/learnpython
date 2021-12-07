d = dict(c='c',a="a",b="b")
a = {"a":"a"}
del d['b']
d.pop('a')
d.popitem()
print(d)

mydict = {"k":"v", "k2":'v2'}
if "k" in mydict:
    print(mydict["k"])
for k in mydict:
    print(mydict[k])

for v in mydict.values():
    print(v)

for k, v in mydict.items():
    print(k,v)

cdict = mydict.copy()
c2dict = dict(mydict)
print(cdict)
print(c2dict)

#merge 
d1 = {"a":"a","b":"b"}
d2 = {"a":"a1","c":"c"}
d1.update(d2)
print(d1)

t = (1,2)
d3 = {t:3}
print(d3)