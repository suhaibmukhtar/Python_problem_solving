def pattern(n):
    a=0
    #rows
    for i in range(1,n+1):
        #spaces
        for j in range(n,i,-1):
            print(" ",end=" ")
        #star
        for k in range(i,2*i):#bcz last excluded
            print(k,end=" ")
            a=k
        a-=1
        for l in range(1,i):#less than i should run 1,1 means no execution
            print(a,end=" ")
            a-=1
        print()#newline
    #new loop for below task
    a=0
    for s in range(n-1,0,-1): #rows= less than row-1
        #space
        for j in range(s,n):
            print(" ",end=" ")
        #stars
        for h in range(s,2*s):
            print(h,end=" ")
            a=h #for next loop
        a-=1
        for p in range(s-1,0,-1):
            print(a,end=" ")
            a-=1
        print()



if __name__=='__main__':
    n=int(input('Enter the number of rows:'))
    pattern(n)