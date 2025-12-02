def findSmallest(arr):
    smallest = arr[0]
    smallest_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr) 

    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr 


print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([7, 4, 3, 18, 5]))