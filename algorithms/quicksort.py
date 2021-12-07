# Two pointers, 1 is dividen point, 1 is scan
def partition(array, low, high):
    pivot = array[high]
    pointer = low
    for i in range(low, high):
        if array[i] < pivot:
            array[pointer], array[i] = array[i], array[pointer]
            pointer+=1
        
    # Swap pivot and current point
    array[pointer], array[high] = array[high], array[pointer]

    return pointer # which is current pivot index


#Quick sort
def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot -1)
        quicksort(array, pivot+1, high)

#Sort array
def sort(array):
    quicksort(array, 0, len(array)-1)


a = [2,1,9,10,5,8,3,7,15,6,22]
sort(a)
print(a)

