'''
RANDOMICED BINARY SEARCH IMPLEMENTATION 22/12/22

'''
import random


def getRandom(x,y):
    tmp=(x + random.randint(0,100000) % (y-x+1))
    return tmp

def RandomizedBinarySearch(array, ini, fin, x):

    if fin >= ini:

        mid = getRandom(ini, fin)

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            return RandomizedBinarySearch(array, ini, mid - 1, x)

        else:
            return RandomizedBinarySearch(array, mid + 1, fin, x)

    else:
        return -1
