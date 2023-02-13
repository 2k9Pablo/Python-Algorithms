'''
QUICK SORT IMPLEMENTATION 23/12/22
'''
def partition(array, low, high):

    pivot = array[low]
    i = low - 1
    j = high + 1

    while(True):

        i += 1
        while(array[i] < pivot):

            i += 1

        j -= 1
        while (array[j] > pivot):
            j -= 1

        if(i >= j):
            return j

        array[i], array[j] = array[j], array[i]


def quickSort(array, low, high):

    if(low < high):

        pi = partition(array, low, high)

        quickSort(array, low, pi)
        quickSort(array, pi - 1, high)