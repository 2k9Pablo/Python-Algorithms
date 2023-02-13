Este algoritmo nos ayuda a realizar la potencia de un número

#### CONSIDERACIONES
- Si la potencia es 0, devolvemos 1
- Si la potencia es 1, devolvemos n
- Si la potencia es par, devolvemos temp * temp
- Si la potencia es impar, devolvemos temp * temp * n
- Si la potencia es menor que 0, deberemos dividir la multiplicación de temporales

#### PSEUDO

```pseudo
# x ^ y
func pow(x, y):
	if y == 0 then:
		return 1
	else if y == 1 then:
		return x
	else:
		temp = pow(x, int(y/2))
		
		if y % 2 == 0:
			return temp * temp
		else:
			if y > 0:
				return x * temp * temp
			else:
				return temp * temp / x
```

#### ILLUSTRATION

![[calculate-power-function-recursiveexample-e29fc0db85efa756.png]]

#### IMPLEMENTATION

```python3
def powDAC(x, y):  
    if y == 0:  
        return 1  
    elif y == 1:  
        return x  
    else:  
        temp = powDAC(x, int(y / 2))  
        if y % 2 == 0:  
            return temp * temp  
        else:  
            if y > 0:  
                return x * temp * temp  
            else:  
                return temp * temp / x  
  
  
if __name__ == "__main__":  
   x, y = 2, -4  
  
   # Function call  
   print('%.6f' % (powDAC(x, y)))
```

#### IMPLEMENTATION GIVEN (NOT - )

```python3
def potDyV(x, a):  
    if a == 0:  
        result = 1  
    else:  
        if a == 1:  
            result = x  
        else:  
            if a % 2 == 0:  
                aux = potDyV(x, a // 2)  
                result = aux * aux  
            else:  
                result = x * potDyV(x, a - 1)  
    return result
```