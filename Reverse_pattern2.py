"""
1 2 3 4 5
1 2 3 4 _
1 2 3 _ _
1 2 _ _ _
1 _ _ _ _
"""
n=int(input('Enter the number of rows:'))
#rows
for i in range(1,n+1):
    #cols
    for j in range(1,n-(i)+2):#starts from 1
        print(j,end="")
    for k in range(0,i-1):
        print("_",end="")
    print()