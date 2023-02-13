Este algoritmo selecciona un *elemento como pivote* y reordena el array alrededor de este.

Encontramos muchas versiones diferentes del *QuickSort* ya que podemos escoger multiples pivotes

```ad-tip
El mejor pivote es la mediana
```

El elemento *clave* a la hora de realizar *QuickSort* es el particionamiento.
	*Proceso por el que escogido un elemento como pivote, pondremos los elementos mayores a un lado y los menores al otro*

#### PARTICIÓN DE LOMUTO

La *partición de Lomuto* asume como pivote **siempre** el último elemento
- En caso de que se de cualquier otro elemento como pivote, se intercambia primero con el último elemento

Inicializaremos dos variables: *i,  j* ambas como el *low del array*
Incrementamos **j** (en cada iteración siempre)
	- si *array[ j ] < pivote* **->** swap *array[ i ] <-> array[ j ]*

Cuando terminemos, swap  *array[ i ] <-> array[ hi ]*
	- **i contiene el pivote**

#### IMPLEMENTACIÓN

```pseudocode
partition(arr[], lo, hi) 
    pivot = arr[hi]
    i = lo-1     // place for swapping
    for j := lo to hi – 1 do
        if arr[j] <= pivot then
            i = i + 1 
            swap arr[i] with arr[j]
    swap arr[i+1] with arr[hi]
    return i+1
```

#### ILLUSTRACIÓN

![[o3.png]]

#### PARTICIÓN DE HOARE

La partición de Hoare es más complicada que la de Lomuto, pero al mismo tiempo más eficiente.

Esta partición funciona de forma que, se inicializan dos índices los cuales en cada iteración, se irán moviendo hacia el otro.

```ad-note
Elegiremos como pivote el array[low]
```

Cuando encontremos una inversión (que el valor del índice izquierdo sea mayor que el índice derecho), intercambiaremos los valores y repetiremos el proceso

#### IMPLEMENTACIÓN

```pseudocode
partition(arr[], lo, hi)
   pivot = arr[lo]
   i = lo - 1  // Initialize left index
   j = hi + 1  // Initialize right index

   // Find a value in left side greater
   // than pivot
   do
	   i = i + 1
   while arr[i] < pivot

   // Find a value in right side smaller
   // than pivot
   do
      j--;
   while (arr[j] > pivot);

   if i >= j then 
      return j

   swap arr[i] with arr[j
```

#### ILLUSTRACIÓN

![[hoare.png]]

#### IMPLEMETACIÓN QUICKSORT

```python3
  
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
```

