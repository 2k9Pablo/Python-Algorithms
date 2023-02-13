'''
Kth ELEMENT IMPLEMENTATION 22/12/22
'''

def kthElement(a, b, k):

    m = len(a)
    n = len(b)

    sorted = [0] * (n+m)
    i = 0
    j = 0
    d = 0
    while (i < m and j < m):

        if(a[i] < b[j]):
            sorted[d] = a[i]
            i += 1

        else:
            sorted[d] = b[j]
            j += 1

        d += 1

    #Acabamos de vaciar los arrays en caso de que haya alguno que falte
    while (i < m):
        sorted[d] = a[i]
        i += 1
        d += 1
    while(j < n):
        sorted[d] = b[j]
        j += 1
        d += 1

    return sorted[k]
