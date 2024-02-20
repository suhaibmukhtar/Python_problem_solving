import math


def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


def reverse_number(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    return rev_num


def is_palindrome(num):
    return num == reverse_number(num)


def is_armstrong(num):
    order = count_digits(num)
    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** order
        temp //= 10
    return num == armstrong_sum


def divisors(num):
    divs = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divs.append(i)
            if i != num // i:
                divs.append(num // i)
    return divs


def main():
    choice = int(input(
        '1. Count the number of digits\n2. Reverse the Digits\n3. Check for Palindrome\n4. Check for Armstrong number\n5. List Divisors\nEnter choice: '))

    if choice == 1:
        num = int(input('Enter the number: '))
        count = count_digits(num)
        print(f"Number of digits in Number are: {count}")
    elif choice == 2:
        num = int(input('Enter the number: '))
        rev_num = reverse_number(num)
        print(f"The reverse of a Number is: {rev_num}")
    elif choice == 3:
        num = int(input('Enter the number: '))
        if is_palindrome(num):
            print(f"{num} is a Palindrome")
        else:
            print(f"{num} is not a Palindrome")
    elif choice == 4:
        num = int(input('Enter the number: '))
        if is_armstrong(num):
            print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is not an Armstrong number")
    elif choice == 5:
        num = int(input('Enter the number: '))
        divs = divisors(num)
        print(f"The divisors of {num} are: {divs}")
    else:
        print('Please Enter a Valid choice')


if __name__ == "__main__":
    main()
