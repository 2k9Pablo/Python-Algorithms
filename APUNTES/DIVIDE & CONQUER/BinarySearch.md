Este algoritmo sirve para, dado un array *ordenado* de **n** elementos, buscar un elemento *x* y devolver su posición

```ad-tip
En este algoritmo, normalmente se empieza por el centro del array, pero se puede empezar desde cualquier posición
```

#### CONSIDERACIONES

- Comparamos el *elemento a buscar* con el *elemento central* 
- En caso de ser menor, buscaremos en la mitad izquierda y repetiremos el proceso
- En caso de ser mayor, buscaremos en la mitad derecha y repetiremos el proceso

#### PSEUDOCODE

```pseudo
func binarySearch(array, x):
	
	if size(array) > 1 then:
		
		mid = size(array) // 2
		if array[mid] == x then:
			return x
		
		else if array[mid] < x then:
			return binarySearch(array[mid ->], x)
		
		else:
			return binarySearch(array[-> mid], x)
	
	else:
		return -1
```

#### ILLUSTRATION

![Imagen Binary Search](binary-and-linear-search-animations.gif)

#### IMPLEMENTATION BINARY SEARCH

```python3
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
```

#### IMPLEMENTATION RANDOMIZED BINARY SEARCH

```python3
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
```
