grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

num = 0
for r in grid:
    for c in r:
        if c < 0:
            num+=1

print(num)

rln = len(grid[0])
cnt = 0
for row in grid:
    low, high = 0, rln -1
    while low <= high: #Find the leftmost value less than 0
        mid = low + (high - low)//2
        if row[mid]>-1:
            low = mid + 1
        else:
            high = mid -1
    if low <= rln:
        cnt += rln - low

print(cnt)

