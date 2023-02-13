Los problemas del tipo *fractional knapsack* se resuelven mediante *greedy algorithms* puesto que se nos permite fraccionar los elementos a la hora de guardalos en la mochila.

Por tanto, deberemos ordenar los elementos en base a un *ratio* 

```ad-note
**ratio** = *valor* / *peso*
```

#### CONSIDERACIONES
- Deberemos ordenar los items en función de su ratio **valor / peso**
- Una vez llegado al último item a insertar, deberemos utilizar:
	*total += (freespace * value) / weight

#### PSEUDOCODE

```pseudocode
class Item():
	
	int value
	int weight

class Knapsack(max_weight, items):
	
	items.sort(x.value / x.weight)
	total = 0
	freespace = max_weight
	i = 0
	while freeSpace > 0:
		if freespace - items[i].weight > 0 then:
			total += items[i].value
			freespace -= items[i].weight
			i++
		
		else:
			total += freespace * items[i].value / items[i].weight
			freespace -= items[i].weight
	
	return total
```

#### ILLUSTRATION

![[Fractional-Knapsackexample-min-1024x512.png]]



#### IMPLEMENTATION

```python3
class Item():  
    def __init__(self, value, weight):  
        self.value = value  
        self.weight = weight  
  
class Knapsack():  
    def __init__(self):  
        self.max = 0  
        self.items = []  
    
    def addItem(self, item):  
        self.items.append(item)  
    
    def fractionalKnapsack(self):  
        freespace = self.max  
        self.items.sort(key = lambda x: (x.value / x.weight), reverse = True)  
        
        total = 0  
        for item in self.items:  
            if freespace - item.weight > 0:  
                total += item.value  
                freespace -= item.weight  
            
            elif freespace > 0:  
                total += (freespace * item.value) / item.weight  
                freespace -= item.weight  
        
        return total  
    
    def setMP(self, max):  
        self.max = max
```
