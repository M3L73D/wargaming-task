from random import randint
from timeit import repeat
from time import process_time

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

ARRAY_LENGTH = 10000

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    
    start = process_time()
    quicksort(array)
    end = process_time()
    print(f"quicksort: {end - start}s")
    
    start = process_time()
    sorted(array)
    end = process_time()
    print(f"sorted: {end - start}s")