Este algoritmo sirve para devolver el elemento central de un array ordenado

En caso de que el array se encuentre desordenador, deberemos ordenarlo primero.

Este algoritmo utiliza KthSmallestElement para devolver el elemento

#### CONSIDERACIONES
- Tenemos dos formas de abordar este problema:
	- Sin ordenar el array
	- Preordenandolo

#### PSEUDOCODE

```pseudocode
func KthSmallest(array):
	n = len(array) // 2
	array.sort
	return array[n]
```

#### ILLUSTRATION

![[Ejemplo-de-cómo-calcular-la-mediana.png]]

#### IMPLEMENTATION SIN ORDENAR

```python3
def median(elements):  
    med = len(elements) // 2  
    return kthSmallestElement(med, elements)  
  
def kthSmallestElement(k, elements):  
    
    mid = len(elements) // 2  
    pivot = elements[mid]   
    low = [x for x in elements if x < pivot]  
    
    if k < len(low):  
        return kthSmallestElement(k, low)  
    
    k -= len(low)  
    equal = [x for x in elements if x == pivot]  
    
    if k < len(equal):  
        return pivot  
    
    k -= len(equal)  
    high = [x for x in elements if x > pivot]  
    return kthSmallestElement(k, high)
```

#### IMPLEMENTATION ORDENANDO

```python3
def KthSmallest(array):
	n = len(array) // 2
	array.sort
	return array[n]
```

