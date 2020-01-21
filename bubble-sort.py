from timeit import time
from random import randrange

def bubble_sort(list):
    for idx in range(len(list)):
        for bubble in range(idx, len(list)):
            if (list[idx] > list[bubble]):
                list[idx], list[bubble] = list[bubble], list[idx]


# not ordered list
mylist = [randrange(1000) for _ in range(30)]

print("unordered list:")
print(mylist)
start_time = time.time()

#...

bubble_sort(mylist)

stop_time = time.time()
print(f"{(stop_time-start_time):.7f}")

# printing ordered list
print("ordered list:")
print(mylist)
