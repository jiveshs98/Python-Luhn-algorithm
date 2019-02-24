# Checking validity of credit card numbers using luhn's algorithm

def sum_of_digits(n):
    sum=0
    while (n>0):
        t= n%10
        sum= sum+t
        n= n//10
    return sum


n= input("Enter your credit card number: ")
try:
    list_num= list(n)
    if len(list_num)==16:
        s1=0
        s2= 0

        for i in range(-1, -17,-1):     # Starting in reverse order
            digit= list_num[i]
            if i%2 == 0:                # Doubling every 2nd digit
                d= int(digit)*2
                if d>9:                 # Checking for 2-digit number
                    s1= s1 + sum_of_digits(d)
                else:
                    s1= s1 + d

            else:
                s2= s2+ int(digit)

        total= s1+s2


        if total % 10 == 0:
            print("\nThe given no. is valid.")
        else:
            print("\nThe given no. is not valid.")
    else:
        raise ValueError
except ValueError:
    print("\nError!! Invalid input. Please enter correct value.")
    print("\nPlease enter a 16-digit number only.")
