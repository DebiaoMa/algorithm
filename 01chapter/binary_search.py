import random
import time

import numpy as np

def binary_search(arr, dst):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = arr[mid]

        if guess == dst:
            return mid
        elif guess < dst:
            low = mid + 1
        else:
            high = mid - 1

    return None

if __name__ == '__main__':
    arr = np.arange(1, 1300000000)
    dst = random.randint(1, 1300000000)
    begin = time.perf_counter()
    ret = binary_search(arr, dst)
    end = time.perf_counter()
    print(ret, "  耗时：", end="")
    print(end-begin)
    print("*******************")
    begin = time.perf_counter()
    for i in range(1300000001):
        if i == dst:
            break

    end = time.perf_counter()
    print(end - begin)
