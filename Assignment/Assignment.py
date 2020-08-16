def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)
#%%
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))
base=int(input("Enter the base number-"))
exp=int(input("Enter the exponential value-"))
print("Result:",power(base,exp))
#%%
def fibo_series(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo_series(n-1) + fibo_series(n-2))  
 
terms = int(input("How many terms? "))  
 
if terms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(terms):  
       print(fibo_series(i))  
#%%
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

n= int(input("enter your number-"))
print(factorial(n))
#%%

def main():
    string1 = input("enter first string")
    string2 = input("enter second string")
    print("First string: ", string1)
    print("Second string: ", string2)
    newString= string1 + string2
    print("string is",newString)
main()
#%%
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number1 = int(input('Please enter the first number: '))
    number2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)

    elif operation == '-':
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)

    elif operation == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif operation == '/':
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)

    else:
        print('You have not typed a valid operator, please run the program again.')

calculate()
#%%
def small(a,b):
    if (a>b):
        return a
    else:
        return b
a=int (input("enter first number"))
b=int (input("enter second number"))    
sum= lambda x,y:x+y
diff= lambda x,y: x-y
print("smallest of two numbers=",small(a,b),diff(a,b))
   