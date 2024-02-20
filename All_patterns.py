
"""
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
"""
def reverse_pattern(n):
    for i in range(1,n+1):
        for j in range(n+1,i,-1):
            print(i,end=" ")
        print()
"""
6 5 4 3 2 
6 5 4 3
6 5 4 
6 5
6
"""

def reverse_pattern_dec(n):
    #rows
    for i in range(1,n+1):
        #columns always start with n+1
        for j in range(n+1,i,-1):
            print(j,end=" ")
        print()
#########################
"""
    *
   **
  ***
 ****
*****
"""
def inverted_right_triangle(n):
    #rows
    for i in range(1,n+1):
        #space
        for j in range(n,i,-1): # 3 2 1
            print(" ",end="")
        #stars
        for k in range(1,i+1):
            print("*",end="")
        #newline
        print()
"""
1
2 1
3 2 1
4 3 2 1
"""
def decreasing_pattern(n):
    #rows
    for i in range(1,n+1):
        #cols
        for j in range(i,0,-1):
            print(j,end="")
        #can include spaces also
        for k in range(n,i):
            print(" ",end="")
        print()#new line
"""
*
**
***
****
***
**
*
"""
if __name__=='__main__':
    n = int(input('Enter the number of Rows:'))
    ch=int(input('1.Print Reverse pattern\n2.Reverse But Decreasing\n3.Inverted Right Triangle\n4.Decreasing pattern\nEnter the Choice:'))
    if ch==1:
        reverse_pattern(n)
    elif ch==2:
        reverse_pattern_dec(n)
    elif ch==3:
        inverted_right_triangle(n)
    elif ch==4:
        decreasing_pattern(n)
    else:
        print('Enter the valid choice!')

