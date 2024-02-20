"""
Bubble sort: the bubble sort pushes the maximum element at end of the unsorted array in the each pass
and performs n-1 passes to sort an array
"""
import numpy as np
n=int(input('Enter the number of element to insert in array:'))
ar=np.zeros(n)
for i in range(n):
    ar[i]=int(input(f'Enter the {i+1}th element of array:'))
## sort the array Using Selection Sort
for i in range(n-1):#bcz total passes =n-1
    #j runs like [0 to (n-2)] to [1 to (n-1)]
    for j in range(n-i-1): #as we perfoms pass size decreases
        if ar[j]>ar[j+1]:
            #swap
            ar[j],ar[j+1]=ar[j+1],ar[j]
#display the sorted array
print(ar)
