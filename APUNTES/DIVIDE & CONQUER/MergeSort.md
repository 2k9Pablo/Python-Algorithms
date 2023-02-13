Este algoritmo se utiliza para la ordenación de vectores, partiendolos a la mitad siempre que sea posible.
Una vez el array sea indivisible, juntaremos las divisiones reordenandolas.

```ad-important
El tamaño del array para fin de la recursión es 1 
```

*Esto sería un caso teórico aplicable a los ejercicios de la asignatura, realmente, se utilizan tamaños de array mayores para combinarlos posteriormente con otros métodos iterativos como el **bubbleSort***

#### CONSIDERACIONES
- Guardaremos, *en caso de que la longitud del array > 2*, la mitad del array en una variable
- Reordenaremos la parte izquierda
- Reordenaremos la parte derecha
- Mezclaremos las dos partes

#### PSEUDOCODE

```pseudocode
step 1: start

step 2: declare array and left, right, mid variable

step 3: perform merge function.  
    if left > right  
        return  
    mid= (left+right)/2  
    mergesort(array, left, mid)  
    mergesort(array, mid+1, right)  
    merge(array, left, mid, right)

step 4: Stop
```

#### ILLUSTRATION

![[merge_sort-what-img1.webp]]

#### IMPLEMENTATION

```python3
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
```