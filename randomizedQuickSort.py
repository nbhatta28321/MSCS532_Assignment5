import time
import random
import tracemalloc

def quick_sort(arr):

    if len(arr) < 2:
        return arr
    
    pivot = random.choice(arr) # used the pivot as middle  element

    left = []
    right = []
    middle = []

    for i in arr: #partioned to left right and middle array and recurively call quick sort and merge when traverse through all the elements.
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)

    return quick_sort(left) + middle + quick_sort(right)  #recursively call quicksort until 1 element is remaining      
    
num=500

   
# function to do the merge sort for random variables
tracemalloc.start()
start = time.time()
a =quick_sort([random.randint(1, 500) for _ in range(num)])
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
print(f"Execution time for random numbers is {end-start} for {num} elments with memory {peak_memory / (1024 * 1024)}")

tracemalloc.start()
start = time.time()
quick_sort(list(range(num)))
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
print(f"Execution time for sorted numbers is {end-start} for {num} elments with memory {peak_memory / (1024 * 1024)}")

tracemalloc.start()
start = time.time()
quick_sort(list(range(num, 0, -1)))
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
print(f"Execution time for reverse sorted numbers is {end-start} for {num} elments with memory {peak_memory / (1024 * 1024)}")

