"""
* _ _ _ _
* * _ _ _
* * * _ _
* * * * _
* * * * *
"""
#rows=n  relation: row 1 star=1 row=2 star=2 so on, row 1 space=n-1, row2 space=n-2 so on
rows=int(input("Enter the number of rows:"))
for i in range(rows):
    # stars
    for j in range(0,i+1):
        print("*",end=" ")
    #spaces
    for k in range(rows-(i+1),0,-1):
        print("_",end=" ")
    #new line
    print()
