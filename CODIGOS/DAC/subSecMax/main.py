'''
Suma SubSecuencia Máxima
'''

def subSexMax(array, start, end):

    if start == end:
        return array[start]

    else:

        half = (start + end) // 2
        sumMaxL = subSexMax(array, start, half)
        sumMaxR = subSexMax(array, half + 1, end)

        total = 0
        sumAuxL = 0

        for i in range(half, start - 1, -1):
            total += array[i]

            if total > sumAuxL:
                sumAuxL = total

        total = 0
        sumAuxR = 0
        for i in range(half + 1, end + 1):
            total = array[i]

            if total > sumAuxR:
                sumAuxR = total

        sumCentral = sumAuxR + sumAuxL
        return max(sumCentral, sumMaxL, sumMaxR)

if __name__ == "__main__":
    v = [-2, 11, -4, 13, -5, 2]

    print("El vector es: ", v)
    sumaMaxima = subSexMax(v, 0, len(v) - 1)
    print("Resultado ", sumaMaxima)