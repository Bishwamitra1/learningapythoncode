#Last time we learn an iterative eay to find a factorial number
#we are now finding a factorial with recursive way
#we must have understood the concept of function in python already
'''
#the code below demostate an iterative way to calculate the factorial of a given number
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
def main():
    number = int(input("Enter a number to find its factorial"))
    factorial_= factorial(number)
    print("The factorial of the given number is:"+ str(factorial_))
main()

