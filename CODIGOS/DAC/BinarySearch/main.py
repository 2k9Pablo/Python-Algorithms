'''
BINARY SEARCH IMPLEMENTATION 22/12/22
'''
def binarySearch(array, ini, fin, x):

    if fin >= ini:

        mid = ini + (fin - 1) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            return binarySearch(array, ini, mid - 1, x)

        else:
            return binarySearch(array, mid + 1, fin, x)
    else:
        return -1
