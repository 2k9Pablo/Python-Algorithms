'''
MERGE SORT IMPLEMENTATION 22/12/22
'''

def mergeSort(array):

    if array.size() > 1:

        mid = len(array) // 2

        L = array[mid:]
        R = array[:mid]

        mergeSort(L)
        mergeSort(R)

        i, j, d = 0
        while(i < len(L) and j < len(R)):
            if(L[i] < R[j]):
                array[d] = L[i]
                i += 1

            else:
                array[d] = R[j]
                j += 1
        d += 1
        while(i < len(L)):
            array[d] = L[i]
            i += 1
            d += 1

        while(j < len(R)):
            array[d] = R[j]
            j += 1
            d += 1

    return array