"""
* * * * *
* * * * _
* * * _ _
* * _ _ _
* _ _ _ _
"""
n=int(input('Enter the number of rows:'))
#rows
for row in range(n):
    #stars
    for col in range(0,n-(row+1)+1):
        print("*",end=" ")
    ##spaces
    for spa in range(0,row):
        print("_",end=" ")
    print()
