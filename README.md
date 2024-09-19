# How to Run
> python3 ./quickSort.py
> python3 ./randomizedQuickSort.py

# Quick Sort and Randomized quick sort

Quick Sort is one of the most used sorting algorithms for its various advantages. It has better time complexity and space complexity when the pivot element is chosen for a certain dataset of elements. The best and average time complexity of quick sort is O(nlog n). For the data set of random elements, the pivot is used to divide the smaller and larger elements. The process is recursively called until all the elements in the data set are sorted. The time complexity becomes average or best time when it does not have to move all the elements from right to left. When we are trying to sort in decreasing or increasing order, and the pivot is the middle element, then one half has to shift completely. This will be worse when all the elements towards the right are smaller since it has to go through all the elements, and time complexity becomes O(n^2). The space complexity will be O(n) since it uses n elements to sort, and no extra space is occupied.

For QuickSort
```
Execution time for random numbers is 0.0027341842651367188 for 500 elments with memory 0.0320892333984375
Execution time for sorted numbers is 0.024461030960083008 for 500 elments with memory 1.1366424560546875
Execution time for reverse sorted numbers is 0.024287939071655273 for 500 elments with memory 1.1678085327148438
```

For randomized Quicksort
```
Execution time for random numbers is 0.002813100814819336 for 500 elments with memory 0.0317840576171875
Execution time for sorted numbers is 0.002273082733154297 for 500 elments with memory 0.04517364501953125
Execution time for reverse sorted numbers is 0.0022957324981689453 for 500 elments with memory 0.04517364501953125
```

The quicksort can be modified to use a pivot as a randomly selected element from the array to have an average case for all kinds of data sets. This can also be known as randomized quicksort. This can be done by choosing a random pivot when partitioning numbers. In that case, when a certain number is randomly chosen from a dataset, which can result in O(n^2), there is less chance the pivot is the first or last element in each iteration. In that case, the time complexity is reduced by a greater value when it does not have to swap all the elements on the left and right sides from the pivot. This will prevent Quicksort from going into the worst-case scenario. From the above demonstration, it is clear that when a pivot is selected from random elements, it performs better than the last element as a pivot. It does much better in sorted and reverse-sorted arrays. Hence, randomizing pivot reduces the time complexity to O(nlogn)