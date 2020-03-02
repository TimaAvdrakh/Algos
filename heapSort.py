def heapify(arr,n,i):
    left = i*2 + 1
    right = i*2 + 2
    most = i

    if left < n and arr[i] < arr[left]:
        most = left

    if right < n and arr[most] < arr[right]:
        most = right

    if most != i:
        arr[most], arr[i] = arr[i], arr[most]
        heapify(arr, n, most)


def heapSort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)

    print(arr)
arr = [11,1,13,131,32]

heapSort(arr)
