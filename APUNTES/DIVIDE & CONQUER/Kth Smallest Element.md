Este algoritmo, dado un número *k*, nos devuelve el elemento que se encuentra en esa posición en un "array ordenado"

En caso de que nos proporcionen un array desordenado, en primer lugar lo ordenaremos.

#### CONSIDERACIONES
- Encontramos dos formas diferentes de abordar este problema
	- Sin preordenar el array
	- Preordenando el array

#### PSEUDOCODE

```pseudocode
func KthSmallest(k, array):
	array.sort
	return array[k]
```

#### ILLUSTRATION

![[inorder.png]]

#### IMPLEMENTATION SIN ORDENAR

```python3
def KthSmallest(array, k):
	pivote = array[k]
	
	low = [x for x in array if x < pivote]
	if k < len(low):
		return KthSmallest(k, low)
	
	k -= len(low)
	equal = [x for x in array if x == pivote]
	elif k < len(equal):
		return pivote
	
	k -= len(equals)
	high = [x for x in array if x > pivote]
	return KthSmallest(k, high)
```

#### IMPLEMENTATION ORDENADO

```python3
def KthSmallest(k, array):
	array.sort()
	return array[k]
```

