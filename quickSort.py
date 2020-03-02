
def quickSort(arr):

    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i < pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quickSort(left) + [pivot] + quickSort(right)


arr = [123,23,3,2,3,4,123,12,3]

print(quickSort(arr))