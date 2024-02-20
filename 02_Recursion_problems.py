## print name 5 times
#print linearly from 1 to n
#print from n to 1
#print linearly from 1 to n but backtrack
#print linearly from n to 1 but backtrack

#print name n times
def name(n,nam):
    #base case
    if n==1:
        print(nam) #when n==1 to display name at that time
        return
    print(nam)
    n-=1
    name(n,nam)
#display number from 1 to n
def one_to_n(i,n):
    #base case
    if i==n:
        print(i)
        return
    #recursive case
    print(i)
    one_to_n(i+1,n)

#display numbers from n to 1
def n_to_one(n):
    #base case
    if n==1:
        print(n)
        return
    print(n)
    n_to_one(n-1)
#one to n backtrack
def one_to_n_backtrack(i,n):
    if i==n+1:
        return
    print(i)
    one_to_n_backtrack(i+1,n)



if __name__=='__main__':
    n=int(input('Enter the number:'))
    ch=int(input('1.Print Name n times\n2.Print numbers from 1 to N\n3.Print numbers from N to 1\n4.Print numbers from 1 to N but bakctrack\n5.Print numbers from N to 1 but backtrack\nEnter your choice:'))
    if ch==1:
        nam=input('Enter your name:')
        name(n,nam)
    elif ch==2:
        one_to_n(1,n)
    elif ch==3:
        n_to_one(n)
    elif ch==4:
        one_to_n_backtrack(1,n)
    else:
        print('Enter a valid choice')