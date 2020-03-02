
def mergeSort(arr):
    l = len(arr)

    if l == 1:
        return arr

    mid = l // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i = j = k =0
    a = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    print(arr)
arr = [12,3,2,1421,421,123,1,23,31,13,3]


mergeSort(arr)