# Homework2
Based on the "divide and conquer" method, QuickSort and MergeSort are 2 sorting techniques in which the set of elements is "splitted" into smaller lists, and then recombined and analyzed after rearrangement. The quick sort usually requires more comparisons than merge sort for sorting a large set of elements.


In MergeSort, the elements are split into sub-arrays (n/2) again and again until only one element is left in any of the creatd sub-arrays. An array with just 1 element is ALWAYS sorted. This is a feature which significantly decreases the sorting time, but it requires additional storage for storing the auxiliary array.
  At last, the subarrays are merged to make it n element size of the array. The list always divided into just half (n/2) dissimilar to quick sort: this means that you will have 2 lists during the 1° loop, 4 lists in the 2° loop, and so on. For every n partition, we make 1 comparison, so the total numer of comparison is n log n.
 In the end, the program return 1 single Array, result of the sorting of the new sub-arrays.

Unlike QuickSort, Mergesort is a stable sort and can be easily adapted to operate on linked lists and very large lists.
The merge sort algorithm performs in the exact same and precise manner regardless of the number of elements involved in the sorting. It works fine even with the large data set. However, it consumes larger part of memory adn it is a lot slower.


QuickSort is the faster of the 2 sorting programs.
Using Quick sort, the set of the elements is infact divided into parts repeatedly until it is not possible to divide it further. Also known as "partition exchange sort", it uses a key element (known as the pivot) to "isolate" the elements.
One partition contains those elements that are smaller than the key element. Another partition contains those elements that are greater than the key element. The elements are sorted recursively.
The number of comparisons during the first loop is n-1, during the second loop is n-2... so at the end of the code (n-1)+(n-2)+(n-3)+ . . . +3+2+1 comparisons are required.
Unlike MergeSort, the splitting of a list of elements is not necessarily divided into halfs every time, except in the rare case in which the pivot is also the median of the list of elements.
At the same time, the created sub-arrays don't require extra space in the code, and for this reason QuickSort is faster.
But it is also inefficient in some situations and also performs a lot of comparisons as compared to merge sort.
