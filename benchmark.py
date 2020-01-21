#crea una lista
from timeit import time
from random import randrange
from selection_sort import selection_sort
#...
lylist = [randrange(1000) for idx in range(10000)]
#calcola i tempi del selection

#calcola i tempi del bubble

selection_sort_time = selection_sort(mytime.copy())


bubble_sort_time = bubble_sort(mytime.copy())