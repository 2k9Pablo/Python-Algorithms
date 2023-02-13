Este algoritmo analiza todas las sumas de las subsecuencias de un array, de forma que devuelve la que sea más alta entre todas.


#### CONSIDERACIONES

- Deberemos comprobar si el principio == final, en cuyo caso solo tendríamos un elemento a devolver
- Al iterar las mitades:
	- *La parte **izquierda** se itera desde **mitad -> inicio - 1, restando 1***
	- *La parte **derecha** se itera**de mitad + 1 -> final +1, sumando 1***
- Deberemos establecer como resultado el máximo de todas las sumas posibles

#### PSEUDO

```pseudo
func sumaMaxima(array):
	if array[inicio] == array[final] then:
		return array[inicio]
	
	else:
		mitad = len(array) / 2
		sumaIzquierda = sumaMaxima(array[hasta mitad])
		sumaDerecha = sumaMaxima(array[desde mitad])
		
		suma = 0
		sumaMaxI = 0
		
		for i in (desde mitad hasta inicio -1):
			suma += array[i]
			if suma > sumaMaxI then:
				sumaMaxI = suma
		
		suma = 0
		sumaMaxD = 0
		for i in (desde mitad +1 hasta final + 1):
			suma += array[i]
			if suma > sumaMaxD then:
				sumaMaxD = suma
		
		sumaMaxC = sumaMaxD + sumaMaxI
		result = max(sumaMaxC, sumaIzquierda, sumaDerecha)
	
	return result
```

#### ILUSTRACIÓN

![[kadane-Algorithm.png]]

#### IMPLEMENTACIÓN

```python3
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
```

