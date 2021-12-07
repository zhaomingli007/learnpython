def binsearch(data, start, end, find):
    if start>end:
        return -1
    mid = (start + end) // 2
    if data[mid] == find:
        return mid
    elif find > data[mid]:
        return binsearch(data, mid + 1, end, find)
    else:
        return binsearch(data, start, mid - 1, find)

print(binsearch([1,2,3,4,5,6,7,8,9,10], 0, 9, 5))
