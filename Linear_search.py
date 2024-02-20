#linear search best tc=0(1) and worst-case, tc=o(n)
import numpy as np

def linear_search(ar,ele,n):
    for i in range(n):
        if ar[i] == ele:
            return i
    return -1
n=int(input("Enter number of elements to insert:"))
ar=np.zeros(n)
for i in range(n):
    ar[i]=int(input(f"Enter ele{i+1}:"))
ele=int(input("Enter the element you want to find:"))
k=linear_search(ar,ele,n)
if k!=-1:
    print(f"Element is found at index:{k}")
else:
    print("Not found in the list")