def quickSort1(arr):

    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quickSort1(less) + [pivot] + quickSort1(greater)

def quickSort2(arr, low, high):

    if low >= high:
        return

    i = low
    j = high
    pivot = arr[i]

    while i < j:

        while arr[j] >= pivot and i < j:
            j -= 1

        while arr[i] <= pivot and i < j:
            i += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]

    quickSort2(arr, low, i-1)
    quickSort2(arr, i+1, high)

if __name__ == '__main__':
    print(quickSort1([20, 345, 0, -1, 8]))
    arr = [20, 345, 0, -1, 8]
    quickSort2(arr, 0, len(arr)-1)
    print(arr)