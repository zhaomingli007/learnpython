from typing import MutableMapping
from random import randrange


def count_words(filename):
    freq = {}
    for piece in open(filename).read().lower().split():
        word = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1+freq.get(word, 0)

    max_word = ''
    max_count = 0
    for(w, c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c

    print('the most frequent word is', max_word)
    print('Its number of occurrences is ', max_count)


# count_words('algorithms/quicksort.py')

class MapBase(MutableMapping):
    """customized mapping base"""
    class _Item:
        __slot__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return self._key != other._key

        def __lt__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('key Error: '+repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = k
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):

        for j in range(len(self._table)):
            if self._table[j]._key == k:
                self._table.pop(j)
                return
        raise KeyError('Key Error: '+repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key


class HashMapBase(MapBase):

    def __init__(self, cap=11, p=109345121):
        """create empty hash-table, p is prime number"""
        self._table = cap * [None]
        self._n = 0  # Number of entries
        self._prime = p  # Prime for MAD compression
        self._scale = 1+randrange(p-1)  # Scale from 1 to p-1 for MAD
        self._shift = randrange(p)  # shift from 1 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2: #Load factor <=0.5
            self._resize(2*len(self._table)-1) #2^x prime is often prime
    
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n-=1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n=0
        for (k, v) in old:
            self[k] = v

class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key error'+repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if(len(self._table[j])> oldsize): # New key
            self._n +=1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for k in bucket:
                    yield k


class ProbeHashMap(HashMapBase):
    _AVAIL = object() # marks locations of previous deletions

    def _is_avaiable(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self,j,k):
        firstAvail = None
        while True:
            if self._is_avaiable(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j+1) % len(self._table)
            
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error'+repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n +=1
        else:
            self._table[s] = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error'+repr(k))
        self._table[s] = ProbeHashMap._AVAIL
    
    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_avaiable(j):
                yield self._table[j]._key
