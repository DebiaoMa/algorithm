def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(smallest_index, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selextionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))

    return newArr

if __name__ == '__main__':
    arr = [3, 5, 1, 5, 0]
    arr = selextionSort(arr)
    print(arr)