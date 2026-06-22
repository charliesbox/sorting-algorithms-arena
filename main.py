import random
data = random.sample(range(1, int(input('max list value: ')) + 1), int(input('amount of samples: ')))

from algorithms.bubble import bubblesort
from algorithms.insert import insertionsort
from algorithms.brokeninsert import brokeninsert
from algorithms.selection import selectionsort


print(data)
bubblesort(data)
brokeninsert(data)
insertionsort(data)
selectionsort(data)