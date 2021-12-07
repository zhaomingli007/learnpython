
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

input = [3,1,2,5,9,8,4,10,7]
bubbleSort(input)                
print(input)
