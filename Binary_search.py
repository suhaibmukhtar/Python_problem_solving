#binary search
"""
The conditions of the binary search are
a) array must be sorted
b) takes logn time to find an element
c) element is always find at the middle of the array
"""
import numpy as np
n=int(input('Enter the number of elements to insert:'))
ar=np.zeros(n)
for i in range(n):
    ar[i]=int(input(f'Enter {i}th element:'))
#To make sure that array is sorted, we use sorting technique such as bubble sort
#n-1 passes
#Bubble sort
swaps=0
for i in range(n-1):
    for j in range(0,n-i-1): #bcz we copare j and j+1 otherwise out of index
        if ar[j]>ar[j+1]:
            temp=ar[j]
            ar[j]=ar[j+1]
            ar[j+1]=temp
            swaps+=1
    if swaps==0:
        break #already sorted
#using binary search
low=0
high=n-1
ele=int(input('Enter the elment you want to find:'))
while(low<=high):
    mid=int((low+high)/2)
    if ar[mid]==ele:
        print(f"Element is found at index:{mid}")
        break
    #element is present at left side of array
    elif ar[mid]>ele:
        low=low
        high=mid-1
    #element is present at right of array
    elif ar[mid]<ele:
        low=mid+1
        high=high
else:
    print("Not found!")
