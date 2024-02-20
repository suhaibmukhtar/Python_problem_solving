## match case in python works like the switch case in python, which jumps the statement matching
#the condition

# Q1 Write a C program to print day of week name using switch case.
# e.g if 2 entered ans should be Tuesday
# Q2 Write a C program to input month number and print total number of days in month using switch...case. C program to find total number of days in a month using switch...case. Logic to print number of days in a month using switch...case in C programming.
# Example Input month number: 3   Total number of days = 31
#Q3 Write a C program to find maximum between two numbers using switch case.


def day_of_week(choice):
    match(choice):
        case 1:
            print(week[1])
        case 2:
            print(week[2])
        case 3:
            print(week[3])
        case 4:
            print(week[4])
        case 5:
            print(week[5])
        case 6:
            print(week[6])
        case 7:
            print(week[0])

#q2: Number of Days in month
def number_of_days(month,days):
    match month:
        case 1|3|5|7|8|10|12:
            print(days[2])
        case 4|6|9|11:
            print(days[1])
        case 2:
            print(days[0])
#Write a C program to find maximum between two numbers using switch case.
def maximum(a,b):
    larger=a+1
    for i in range(a+1,b):
        if i>larger:
            larger=i

    print('Maximum Number is:',larger)

#Menu
ch=int(input("1.Display the day of the Week\n2.The number of days in month\n3.Larger b/w the Two numbers\nChoice:"))
if ch==1:
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    choice = int(input('Enter the Day Of Week:'))
    day_of_week(choice)
elif ch==2:
    days=[28,30,31]
    month=int(input("Enter the Month:"))
    number_of_days(month,days)
elif ch==3:
    a=int(input('Enter the ist number:'))
    b=int(input('Enter the 2nd number:'))
    maximum(a,b)