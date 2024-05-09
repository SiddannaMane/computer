def fact(n): 
 if n == 1: 
 return 1 
 else: 
 return (n * fact(n-1)) 
n=int(input("Enter the number:")) 
print("The factorial of a number is:",fact(n))

def fib(n): 
 if n<=1: 
 return n 
 return fib(n-1) + fib(n-2) 
n=int(input("Enter the range:")) 
print("The fibonacci value is:",fib(n))