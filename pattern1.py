"""
* * *
* * *
* * *
"""
#rows=n, columns=1,2,3,4,....,n columns = total number of rows for each row
n=int(input('Enter the number of rows:'))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()