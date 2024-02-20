"""
Insertion Sort: The insertion sort works like take the element at index i and place it in its correct
position. order of complexity is 0(n^2)
"""
import numpy as np

n=int(input('Enter the number of element to insert in array:'))
ar=np.zeros(n)
for i in range(n):
    ar[i]=int(input(f'Enter the {i+1}th element of array:'))
#takes n-1 passes bcz 0th element is by default treated as sorted only used for comparison
#assume tht 0th element is already sorted
for i in range(1,n):
    j=i
    while(j>0 and ar[j-1]>ar[j]):
        #if true perform swapping otherwise not required
        temp = ar[j]
        ar[j] = ar[j - 1]
        ar[j - 1] = temp
        #decrease the index by 1 i.e. so that so compare it with element on left
        j-=1
#sorted array
print(ar)