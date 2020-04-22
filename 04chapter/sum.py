def sum(arr):

    if len(arr) == 0:
        return 0

    return arr.pop(0) + sum(arr)

def myLen(arr):

    if len(arr) == 0:
        return 0

    else:
        arr.pop(0)
        return 1 + myLen(arr)





if __name__ == '__main__':
    a = [2, 3, 4]
    print(myLen(a))
    s = sum(a)
    print(s)
