Utilizado en problemas del tipo *selección de actividades*
Estas actividades, tendrán *una fecha comienzo / fecha finalización*

```ad-warning
*Todas las actividades reportan un mismo beneficio, no buscamos un ratio*
```

Para ordenar las diferentes actividades, deberemos ordenarlas según su fecha de finalización.

#### PSEUDOCODE

```pseudocode
class activity():
	
	string name
	int start
	int finish

def max_activities(activities):
	
	selected = []
	activities.sort(x.finish)
	last_finish = activities[0].finish
	
	selected.add(activities[0])
	
	for act in activities:
		if last_finish < activities[act].start:
			last_finish = activities[act].finish
			selected.add(activities[act])
	
	return selected
```

#### ILLUSTRATION
![[1Qajl.png]]

#### IMPLEMENTATION

```python3
class Actividad():
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

class OverlappingIntervals():
    def __init__(self):
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
    
    def greedySelect(self):
        self.items.sort(key = lambda x: (x.finish))
        total = 1
        best_finish = self.items[0].finish
        
        for item in self.items:
            if item.start > best_finish:
                total += 1
                best_finish = item.finish
        
        return total
```