"""
In selection sort we look for the minimums and sort the array with ith index, in each pass we
try to sort the unsorted part of the array and perform n-1 passes to sort the array bcz last
element is sorted by default
"""
import numpy as np
n=int(input('Enter the number of element to insert in array:'))
ar=np.zeros(n)
for i in range(n):
    ar[i]=int(input(f'Enter the {i+1}th element of array:'))
## sort the array Using Selection Sort
for i in range(n-1):#bcz total passes =n-1
    min=i #index of min element to be swaped
    for j in range(i,n):
        if ar[min]>ar[j]:
            min=j
    #swap
    temp=ar[i]
    ar[i]=ar[min] #swap with smallest index
    ar[min]=temp
#display the sorted array
print(ar)
