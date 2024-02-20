#display number from 1 to n
def display(i,n):
    if i==n+1:
        return
    print(i)
    i+=1
    display(i,n)
#tail-recursion
def tail_display(n):
    #base condtion
    if n==1:
        print(n,end="\n") #to display 1
        return
    #recursive condition
    tail_display(n-1)
    print(n)   #this statement will get executed after returning from function
if __name__=='__main__':
    n = int(input('Enter the number'))
    ch=int(input('1.Head recursion\n2.Tail Recursion\nEnter choice:'))
    if ch==1:
        display(1,n)
    elif ch==2:
        tail_display(n)
    else:
        print('Enter the Valid choice')