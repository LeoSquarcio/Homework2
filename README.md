# Homework2
Based on the "divide and conquer" method, QuickSort and MergeSort are 2 sorting techniques in which the set of elements is "splitted" into smaller lists, and then recombined and analyzed after rearrangement. The quick sort usually requires more comparisons than merge sort for sorting a large set of elements.

Using Quick sort, the set of the elements is divided into parts repeatedly until it is not possible to divide it further. Also known as "partition exchange sort", it uses a key element (known as the pivot) to "isolate" the elements.
Unlike MergeSort, the splitting of a list of elements is not necessarily divided into halfs every time, and for this reason QuickSort is faster
But it is also inefficient in some situations and also performs a lot of comparisons as compared to merge sort.

In MergeSort, the elements are split into sub-arrays (n/2) again and again until only one element is left in any of the creatd sub-arrays. An array with just 1 element is ALWAYS sorted. This is a feature which significantly decreases the sorting time, but it requires additional storage for storing the auxiliary array.
  At last, the subarrays are merged to make it n element size of the array. The list always divided into just half (n/2) dissimilar to quick sort.
Mergesort is a stable sort, unlike quicksort and heapsort, and can be easily adapted to operate on linked lists and very large lists
The merge sort algorithm performs in the exact same and precise manner regardless of the number of elements involved in the sorting. It works fine even with the large data set. However, it consumes larger part of memory.
