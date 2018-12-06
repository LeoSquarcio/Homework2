import matplotlib.pyplot as plt



        
setup="""

import random

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 

def quickSort(arr,low,high):
    if low < high:

        pi = partition(arr,low,high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        

        
def measurethis(size):
    mylist=[]
    for i in range(size):
        mylist.append(random.randint(0,size))
        
"""      
import timeit
TimeQuick = timeit.Timer('measurethis(1000)', setup=setup)
print(TimeQuick.timeit(5))


setup="""
import random

def mergeSort(x):

    if len(x) > 1:
        
        middle = len(x)//2
        L = x[:middle]
        R = msort(x[middle:])
        
        mergeSort(L)
        mergeSort(R)
        
        i = j = k =0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x[k] = L[i]
                i+=1
            else:
                x[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            x[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            x[k]=R[j]
            j+=1
            k+=1
            
def printList(x):
    for i in range(len(x)):
        print(x[i])
    print()
    
def MeasureThis(size):
    mylist=[]
    for i in range(size):
        mylist.append(random.randint(0,size))

"""
    
import timeit
TimeMerge=timeit.Timer("MeasureThis(1000)", setup=setup)
print (TimeMerge.timeit(5))

tm = [TimeMerge.timeit(1)]
tq = [TimeQuick.timeit(1)]

