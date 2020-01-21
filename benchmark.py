from timeit import time
from random import randrange
from selection_sort import selection_sort

#crea una lista

lylist = [randrange(1000) for idx in range(10000)]

#calcola i tempi del selection

selection_sort_time = selection_sort(mytime.copy())

#calcola i tempi del bubble

bubble_sort_time = bubble_sort(mytime.copy())


copy_list = mylist.copy()
default_sort_time = copy_list.sort()